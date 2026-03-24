# AccessLens: The Development Journey

This document chronicles the evolution of AccessLens, from a FOSS project idea to a comprehensive accessibility auditing framework.

## Phase 1: Inception & Architectural Blueprint
**Date:** March 1st, 2026

The journey began with the selection of our FOSS topic. We established our primary planning hub on Notion, mapping out every technical detail and feature requirement. We divided the team to focus on our strengths:
- **Backend Team:** Upanshi and Sansriti
- **Frontend Team:** Toyesh and Sara

**Key Milestone:** API structure and JSON formats were finalized and shared with the frontend team to enable parallel development.

> [!TIP]
> **Strategic Prioritization:** We focused Phase 1 on establishing a rock-solid core auditing engine (6 base engines). Once core functionality was stable, we incrementally added advanced features like **Shadow DOM traversal** (March 23rd, commit `0ca0c15`) and **SSRF network configuration**, demonstrating iterative development practices.

---

## Phase 2: The Holi Break Sprint
**Date:** March 2nd – March 10th, 2026

With lab tests looming, we utilized the Holi break for a massive development push. 
- **Commit `ce8323a`:** Luna initialized the modular project structure.
- **Commit `fa5afac`:** Placeholder files added to organize empty directories.

The backend team focused on core engine logic while the frontend team built the initial UI components.

> [!IMPORTANT]
> **Intensive Development Sprint:** The Holi break provided a dedicated development window, where we decided to even live on coffee and sleepless nights. We leveraged this concentrated time to implement all seven analysis engines and establish the core API infrastructure.

---

## Phase 3: The 15,000 Line Mystery & Integration
**Date:** March 11th – March 12th, 2026

On March 11th, we committed the bulk of our backend work (`6d95455`). On March 12th, the team held a meetup to integrate the frontend. To avoid merge conflicts across four different environments, we used a USB drive to combine the files.

**The "WTH" Moment:** After integration, we saw a staggering **15,000+ lines** of changes!
- **Mystery Solved:** Upon investigation, we realized ~6,000 lines were from `package-lock.json` and ~5,000 were from `.txt` log files used by the backend team to track feature progress.

**Key Milestone:** Backend and frontend successfully integrated (`9bf304e`).

> [!NOTE]
> **Strategic Decision (USB Integration):** To minimize merge conflicts while maintaining parallel velocity across 4 laptops with different environments, we used a **USB transfer** for the March 12th integration. This was a pragmatic decision that prevented environment-specific issues that git merges would have introduced across multiple local setups.

---

## Phase 4: Balancing Acts & Feature Polishing
**Date:** March 13th – March 22nd, 2026

Between March 13th and 17th, the team managed lab tests while troubleshooting integration bugs.
- **Commit `77add95`:** Resolved critical `ai_contextual=0` issues.
- **Commit `7772c24`:** Luna added engine alias mapping and cleaned API responses.
- **March 22nd:** A flurry of updates including Docker optimization (`7e3c855`), license creation (`84f99a9`), and a revised README (`fb98afc`).

---

## Phase 5: The Final Push & Demo Readiness
**Date:** March 23rd – Present

With mid semester exams starting on March 24th, we hit the ground running as soon as lab tests finished.
- **Commit `0ca0c15` (March 23rd):** Significant enhancements including Shadow DOM files integration, SSRF network config changes, and AI engine improvements.

**Current Status:** All core features are integrated and working. The demo is scheduled for March 25th, marking the culmination of our "Holi to Exams" sprint.

> [!IMPORTANT]
> **Final Integration & Demo Readiness:** By March 23rd, all core features were complete and tested. The March 25th demo was scheduled to occur before final assessments, ensuring the team could demonstrate the complete system before commitments shifted elsewhere.

---

## Development By The Numbers
- **Total Commits:** 36 (March 1-23, 2026)
- **Lines of Code:** ~44,500 total lines (including ~6,000 lines in `package-lock.json`)
- **Test Coverage:** 86% test coverage
- **Documentation:** All docs with every minute detail captured.
- **Team Velocity:** 4 developers, ~23 development days, 7 engine systems

---
*Created by the AccessLens Team: Upanshi Mittal, Sansriti Mishra, Toyesh Gupta, and Sara Jain.*
