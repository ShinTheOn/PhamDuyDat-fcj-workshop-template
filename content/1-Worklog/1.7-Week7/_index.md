---
title: "Internship Worklog Week 7"
date: 2026-05-29
weight: 7
chapter: false
pre: "<b> 1.7. </b>"
---

### Week 7 Objectives:
* Analyze cloud financial management workflows and optimize platform utilization to eliminate resource waste.
* Deploy comprehensive data protection frameworks using automated multi-tier backup schedules.
* Configure and validate fast disaster recovery pipelines under simulated infrastructure failure events.

### Tasks Implemented This Week:

| Day | Task Details | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Researching Lab 17]:** Evaluated core Cost Optimization principles, leveraging AWS Trusted Advisor and AWS Compute Optimizer metrics. | 29/05/2026 | 29/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Practicing Lab 17]:** Measured cluster resource efficiency and audited infrastructure environments to identify and delete unattached EBS volumes. | 30/05/2026 | 30/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Researching Lab 18]:** Explored managed Backup & Recovery architectures, defining RPO and RTO parameters within the AWS Backup console. | 31/05/2026 | 31/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Practicing Lab 18 - Part 1]:** Initialized a secure Backup Vault and structured automated Backup Plans targeting active Linux EC2 nodes and EBS blocks. | 01/06/2026 | 01/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Practicing Lab 18 - Part 2]:** Programmed backup lifecycle rules to systematically transition stale infrastructure snapshots into low-cost Cold Storage classes. | 02/06/2026 | 02/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Practicing Lab 18 - Part 3]:** Simulated production data loss scenarios, executed full volume Restore processes, and completed staging resource teardowns. | 03/06/2026 | 03/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Daily Progress Details

**Tasks Completed on 02/06 (Focus Area: Lab 18):**
* Successfully completed the lifecycle policy design for centralized infrastructure backup configurations.
* Formulated automated pipelines to migrate aging snapshot files into archival cold tiers after specified retention periods to optimize long-term storage cost footprints.

**Planned Tasks for 03/06 (Focus Area: Lab 18):**
* Execute a controlled termination of an active compute instance to simulate an abrupt server hardware outage.
* Trigger emergency point-in-time recovery tasks from the latest instance image stored inside the Backup Vault, confirm system data integrity post-recovery, and completely purge the testing setup to preserve credits.

---

### Accomplishments in Week 7:

* **Cloud Financial Governance & Asset Optimization (Lab 17):**
    * Mastered infrastructure profiling strategies to execute systematic resource right-sizing based on concrete utilization telemetry.
    * Gained practical capabilities using cloud advisory toolsets to identify and remediate hidden operational spending leaks.
* **Enterprise Data Resiliency & Backup Engineering (Lab 18):**
    * Developed full competency structuring centralized backup strategies, ensuring high asset availability and disaster recovery readiness.
    * Attained hands-on skills aligning Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) to match standard business continuity goals.
* **Operational Disaster Readiness & Observability Standards:**
    * Advanced technical problem-solving skills by manually validating real-world backup restore operations under simulated emergency states.
    * Consistently carried out thorough environment cleanup workflows post-lab execution, keeping engineering progress documentation synced onto GitHub.
