---
title: "Internship Worklog Week 6"
date: 2026-05-22
weight: 6
chapter: false
pre: "<b> 1.6. </b>"
---

### Week 6 Objectives:
* Analyze enterprise-grade shared file storage solutions capable of concurrent multi-node mounting across distinct hosts.
* Master automated systems administration frameworks to orchestrate remote bulk configuration and patch deployments.
* Optimize centralized workflows for securing infrastructure parameter architectures and system secrets.

### Tasks Implemented This Week:

| Day | Task Details | Start Date | Completion Date | Reference Material |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Researching Lab 15]:** Studied the operational mechanics of Amazon EFS (Elastic File System) shared network storage, contrasting it with EBS and S3. | 22/05/2026 | 22/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Practicing Lab 15]:** Provisioned an Amazon EFS architecture, configured Mount Targets, and concurrently attached the shared drive across multiple running EC2 nodes. | 23/05/2026 | 23/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Researching Lab 16]:** Explored the AWS Management Tools landscape, focusing on auditing the core capabilities of AWS Systems Manager (SSM). | 24/05/2026 | 24/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Practicing Lab 16 - Part 1]:** Configured standard IAM roles for SSM Agents and established secure terminal sessions onto active Linux hosts without relying on traditional SSH key methods. | 25/05/2026 | 25/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Practicing Lab 16 - Part 2]:** Utilized SSM Run Command to deploy bulk application software setups remotely across node instances and managed secrets using SSM Parameter Store. | 26/05/2026 | 26/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Practicing Lab 16 - Part 3]:** Tested real-time automated operating system patching sequences using Patch Manager and completed staging resource decommissioning routines. | 27/05/2026 | 27/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Daily Progress Details

**Tasks Completed on 26/05 (Focus Area: Lab 16):**
* Successfully completed the secure aggregation and encryption of internal environmental variables and database connection strings within the managed SSM Parameter Store vault.
* Dispatched parallel script executions to a wide fleet of remote targets using the SSM Run Command module, mitigating manual host access requirements.

**Planned Tasks for 27/05 (Focus Area: Lab 16):**
* Construct automated routine patch orchestration plans to scan and implement critical operating system updates on active EC2 fleets with Patch Manager.
* Validate generated security compliance logs to guarantee patch alignment, then cleanly dismantle experimental file stores and compute endpoints to stay within internship account credit limits.

---

### Accomplishments in Week 6:

* **Shared Network Storage Implementation (Lab 15):**
    * Mastered shared network mount topologies for distributed Linux nodes, solving synchronization problems across decoupled environments.
    * Attained practical competencies managing throughput parameters based on data access tier demands.
* **Bulk Enterprise Infrastructure Automation (Lab 16):**
    * Transformed asset deployment workflows by replacing independent server configuration patterns with modern centralized remote execution strategies.
    * Enforced higher infrastructure security controls by completely blocking standard public network inbound SSH rules via the implementation of Session Manager paths.
* **Standardized Secret Management & Operational Engineering:**
    * Achieved full mastery over encrypting configuration properties and variables across corporate cloud application systems.
    * Rigorously maintained staging asset teardown pipelines upon completing evaluations, systematically pushing all engineering documentation updates to GitHub.
