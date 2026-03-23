def get_shadow_piercing_script():
    """Returns a script that can pierce shadow roots recursively and generate robust selectors."""
    return """
    (function() {
        /**
         * Recursively finds elements matching a selector, including those inside shadow roots.
         * Uses TreeWalker for performance on complex pages like YouTube.
         */
        window._accessLensPierce = function(root = document, selector = '*') {
            const elements = Array.from(root.querySelectorAll(selector));
            
            // recursive piercing
            try {
                const walker = document.createTreeWalker(root, 1 /* NodeFilter.SHOW_ELEMENT */);
                let n;
                while (n = walker.nextNode()) {
                    const shadow = n.shadowRoot || n._shadowRoot;
                    if (shadow) {
                        elements.push(...window._accessLensPierce(shadow, selector));
                    }
                }
            } catch (e) {
                // Fallback for environments where TreeWalker might fail on ShadowRoot
                const all = root.querySelectorAll('*');
                for (let i = 0; i < all.length; i++) {
                    const el = all[i];
                    const shadow = el.shadowRoot || el._shadowRoot;
                    if (shadow) {
                        elements.push(...window._accessLensPierce(shadow, selector));
                    }
                }
            }
            return elements;
        };

        /**
         * Generates a unique CSS selector for an element, crossing shadow boundaries with [shadow-root] markers.
         */
        window._accessLensGetSelector = function(el) {
            if (!el || el.nodeType !== 1) return '';
            
            const path = [];
            let current = el;
            
            while (current) {
                // Check if current is a ShadowRoot
                const isShadowRoot = current.nodeType === 11 || 
                                   (current.toString && current.toString() === '[object ShadowRoot]');
                                   
                if (isShadowRoot && current.host) {
                    path.unshift(`[shadow-root]`);
                    current = current.host;
                    continue;
                }
                
                if (current.nodeType !== 1) { // Not an element
                    if (!current.parentNode && current !== document) {
                        try {
                            const root = current.getRootNode ? current.getRootNode() : null;
                            if (root && root !== current && root.host) {
                                path.unshift(`[shadow-root]`);
                                current = root.host;
                                continue;
                            }
                        } catch(e) {}
                    }
                    current = current.parentNode;
                    continue;
                }

                let tagName = (current.tagName || "").toLowerCase();
                if (!tagName) {
                    current = current.parentNode;
                    continue;
                }

                let selector = tagName;
                if (current.id) {
                    selector += `#${CSS.escape(current.id)}`;
                } else {
                    const parent = current.parentNode;
                    if (parent && parent.children) {
                        const siblings = Array.from(parent.children).filter(c => c.tagName === current.tagName);
                        if (siblings.length > 1) {
                            const index = siblings.indexOf(current) + 1;
                            selector += `:nth-of-type(${index})`;
                        }
                    }
                }

                path.unshift(selector);
                current = current.parentNode;
            }
            
            return path.join(' > ');
        };
    })();
    """
def get_query_elements_script():
    """Returns a helper script that provides window._accessLensQuery for easier element selection."""
    return """
    (function() {
        window._accessLensQuery = function(selector) {
            return window._accessLensPierce(document, selector);
        };
    })();
    """