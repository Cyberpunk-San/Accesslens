
from typing import List, Dict, Any
from ..models.schemas import UnifiedIssue, IssueSeverity, ConfidenceLevel

class ConfidenceCalculator:


    @staticmethod
    def calculate_confidence(
        source: str,
        factors: Dict[str, float],
        base_confidence: float = 100.0
    ) -> float:

        weights = {
            "wcag_deterministic": {
                "detection_reliability": 0.5,
                "context_clarity": 0.2,
                "pattern_match": 0.1,
                "evidence_quality": 0.2
            },
            "structural": {
                "detection_reliability": 0.3,
                "context_clarity": 0.3,
                "pattern_match": 0.2,
                "evidence_quality": 0.2
            },
            "contrast": {
                "detection_reliability": 0.4,
                "context_clarity": 0.3,
                "pattern_match": 0.1,
                "evidence_quality": 0.2
            },
            "ai_contextual": {
                "detection_reliability": 0.2,
                "context_clarity": 0.3,
                "pattern_match": 0.2,
                "evidence_quality": 0.3
            }
        }

        source_weights = weights.get(source, weights["wcag_deterministic"])

        weighted_score = sum(
            factors.get(factor, 1.0) * weight
            for factor, weight in source_weights.items()
        )


        confidence = min(100, max(0, weighted_score * 100))

        return round(confidence, 2)

    @staticmethod
    def confidence_to_level(score: float) -> ConfidenceLevel:

        if score >= 95:
            return ConfidenceLevel.HIGH
        elif score >= 70:
            return ConfidenceLevel.MEDIUM
        else:
            return ConfidenceLevel.LOW

class ImpactScorer:
    """
    Calculates a qualitative accessibility score based on the severity and type of issues.
    Prioritizes CRITICAL barriers (P0) over minor aesthetic issues.
    """
    
    SEVERITY_WEIGHTS = {
        IssueSeverity.CRITICAL: 25.0,  # 4 Criticals = 0 score
        IssueSeverity.SERIOUS:  10.0,
        IssueSeverity.MODERATE:  2.0,
        IssueSeverity.MINOR:     0.5
    }

    @classmethod
    def calculate_score(cls, issues: List[UnifiedIssue]) -> float:
        """
        Uses a non-linear deduction model. 
        Deducts per unique issue type/pattern to avoid score=0 on large pages with many twins.
        """
        if not issues:
            return 100.0

        total_deduction = 0.0
        seen_patterns = set()

        # Sort issues so more severe ones are processed first for deduplication logic if needed
        sorted_issues = sorted(issues, key=lambda i: cls.SEVERITY_WEIGHTS.get(i.severity, 0), reverse=True)

        for issue in sorted_issues:
            # Create a pattern key based on issue type and a simplified selector or title
            # This allows grouping 400 identical contrast issues into 1 'pattern' for scoring.
            pattern_key = f"{issue.issue_type}:{issue.title[:30]}"
            
            weight = cls.SEVERITY_WEIGHTS.get(issue.severity, 0.5)
            
            if pattern_key not in seen_patterns:
                # First time seeing this pattern = Full deduction
                total_deduction += weight
                seen_patterns.add(pattern_key)
            else:
                # Repeated pattern = Diminishing deduction (prevents score from being killed by repetitive bugs)
                total_deduction += (weight * 0.05) # Only 5% additional penalty for duplicates

        # Final score calculation with a floor of 0
        # A score of 0 should represent a truly unusable experience (multiple Criticals)
        final_score = max(0, 100 - total_deduction)
        
        return round(final_score, 2)

class SeverityMapper:


    SEVERITY_MATRIX = {
        "missing_alt": {
            "impact": IssueSeverity.CRITICAL,
            "wcag": "1.1.1",
            "description": "Images missing alternative text"
        },
        "low_contrast": {
            "impact": IssueSeverity.SERIOUS,
            "wcag": "1.4.3",
            "description": "Text contrast below 4.5:1"
        },
        "empty_button": {
            "impact": IssueSeverity.CRITICAL,
            "wcag": "4.1.2",
            "description": "Button has no accessible name"
        },
        "heading_skip": {
            "impact": IssueSeverity.MODERATE,
            "wcag": "1.3.1",
            "description": "Heading level skipped"
        },
        "missing_landmark": {
            "impact": IssueSeverity.SERIOUS,
            "wcag": "1.3.1",
            "description": "Missing landmark regions"
        }
    }

    @classmethod
    def get_severity(cls, issue_type: str, context: Dict[str, Any] = None) -> IssueSeverity:

        base = cls.SEVERITY_MATRIX.get(
            issue_type,
            {"impact": IssueSeverity.MINOR}
        )

        if context and context.get("user_impact", "").lower() == "blocking":
            return IssueSeverity.CRITICAL

        return base["impact"]