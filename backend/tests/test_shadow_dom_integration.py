
import pytest
import asyncio
from playwright.async_api import Page
from app.core.accessibility_tree import AccessibilityTreeExtractor
from app.engines.structural_engine import StructuralEngine
from app.models.schemas import AuditRequest

@pytest.mark.asyncio
async def test_shadow_dom_piercing_integration(initialized_browser_manager):
    bm = initialized_browser_manager
    html_content = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Main Document Heading</h1>
        <div id="host"></div>
        <script>
            const host = document.getElementById('host');
            const shadow = host.attachShadow({mode: 'open'});
            shadow.innerHTML = `
                <h2>Shadow Heading</h2>
                <nav role="navigation">
                    <ul>
                        <li><a href="#">Shadow Link</a></li>
                    </ul>
                </nav>
                <div onclick="console.log('click')" role="button">Shadow Clickable</div>
            `;
        </script>
    </body>
    </html>
    """
    
    import base64
    data_uri = f"data:text/html;base64,{base64.b64encode(html_content.encode()).decode()}"
    
    async with bm.page_session() as page:
        await page.goto(data_uri)
        await page.wait_for_load_state("networkidle")
        
        extractor = AccessibilityTreeExtractor()
        data = await extractor.extract(page)
        data["page"] = page 
        
        headings = data["structure"]["headings"]["headings"]
        heading_texts = [h["text"] for h in headings]
        assert "Main Document Heading" in heading_texts
        assert "Shadow Heading" in heading_texts

        landmarks = data["structure"]["landmarks"]["landmarks"]
        landmark_roles = [l["role"] for l in landmarks]
        assert "navigation" in landmark_roles

        engine = StructuralEngine()
        request = AuditRequest(url=data_uri)
        issues = await engine.analyze(data, request)
        semantic_issues = [i for i in issues if i.issue_type == "clickable_non_semantic"]
        assert len(semantic_issues) > 0
        assert "Shadow Clickable" in semantic_issues[0].location.html or "[shadow-root]" in semantic_issues[0].location.selector

@pytest.mark.asyncio
async def test_youtube_shadow_dom_integration(initialized_browser_manager):
    bm = initialized_browser_manager
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    
    async with bm.page_session() as page:
        # YouTube is heavy, giving it more time
        await page.goto(url, wait_until="networkidle", timeout=60000)
        
        # Giving Polymer/Lit a moment to hydrate
        await asyncio.sleep(2)
        
        extractor = AccessibilityTreeExtractor()
        data = await extractor.extract(page)
        data["page"] = page # Required for StructuralEngine
        
        # Verifying we found headings
        headings = data["structure"]["headings"]["headings"]
        assert len(headings) > 0, "Should have found headings on YouTube"
        
        # At minimum, should have found landmarks
        landmarks = data["structure"]["landmarks"]["landmarks"]
        roles = [l["role"] for l in landmarks]
        assert len(roles) > 0, "Should have found landmarks on YouTube"
        
        # Checking if Shadow DOM is actually being used in this session
        has_shadow_roots = await page.evaluate("""
            () => !!Array.from(document.querySelectorAll('*')).find(el => el.shadowRoot || el._shadowRoot)
        """)
        
        selectors = [h["selector"] for h in headings] + [l["selector"] for l in landmarks]
        shadow_selectors = [s for s in selectors if "[shadow-root]" in s]
        
        print(f"YouTube Shadow DOM detected: {has_shadow_roots}")
        print(f"Shadow selectors found: {len(shadow_selectors)}")
        
        if has_shadow_roots:
            assert len(shadow_selectors) > 0, "Shadow roots were detected but not pierced!"
        else:
            print("YouTube is in Light DOM mode for this session. Skipping shadow piercing assertion.")

if __name__ == "__main__":
    pass
