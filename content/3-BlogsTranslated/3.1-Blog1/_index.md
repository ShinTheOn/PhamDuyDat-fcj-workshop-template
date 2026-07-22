---
title : "How Synthesia Optimizes Generative AI Video Inference on Amazon EC2 G7e"
date : 2026-06-09
weight : 1
chapter : false
pre : " <b> 3.1. </b> "
---

### [Case Study] How Synthesia Optimizes Generative AI Video Inference on Amazon EC2 G7e Instances — Saving $900 per 1,000 Hours

When AI generates video, the GPU must stall after each small segment to wait for the host system to write data to disk before resuming execution. While it sounds minor, this aggregates to cause the GPU to sit completely idle 18% of the time.

Synthesia recently announced how they solved this exact bottleneck. GPU duty cycles surged to 99.9%, performance accelerated by 8.2%, and operational costs dropped by nearly $900 per 1,000 video hours—with absolute zero modifications to the core AI model.

#### What is the issue?
When generating video, the AI cannot process the entire video payload simultaneously due to extreme file sizes. Instead, it fragments the pipeline into smaller sequential segments known as **"chunks"**, processing a few frames per discrete iteration.

Under the legacy synchronous (sequential) approach:
- The GPU finishes processing chunk 1 &rarr; completely stalls
- Waits for the host system to finish writing data to a file
- Only then does it commence processing chunk 2

Real-world profiling data indicates that the GPU actively computes only 82% of the time, leaving 18% wasted as dead idle intervals. For elite cluster instances costing thousands of dollars per hour, this represents a massive operational drain.

#### What did Synthesia + AWS execute?
They titled the architecture the **Asynchronous Frame Generation Pipeline** — a complex name for a straightforward concept: keep the GPU computing continuously at peak capacity. Meanwhile, heavy file-writing and data transfer tasks are delegated to the CPU via parallel tracks, preventing the GPU from waiting.

Specifically, they deployed three core engineering pillars:
1. **Dual Processing Streams:** Decoupling GPU mathematical computation paths from data transfer paths, allowing both workflows to run concurrently without resource locking.
2. **Dedicated File-Writing Worker Thread:** Initializing an isolated background thread exclusively tasked with committing encoded video assets to disk, completely offloading the primary CPU thread so it can focus purely on scheduling kernel instructions to the GPU.
3. **Double Buffering Matrix:** Operating similarly to an alternating two-tray mechanism in a high-velocity kitchen. While the kitchen (GPU) fills Tray A with fresh data, the waiter (CPU Worker) is actively delivering Tray B to the tables—ensuring neither track obstructs the other.

#### Conclusion:
&rarr; Performance accelerated by 8.2%, the GPU maintains an uninterrupted computation line, and zero changes were required inside the core AI architecture.

#### Why does this matter?
You do not need an advanced engineering background to grasp the practical value of this optimization. As AI enterprises structurally optimize their massive infrastructure overhead, operating costs decline, naturally creating opportunities for more affordable consumer-facing AI service pricing tiers over time.

A particularly noteworthy detail from this case study is that the complete functional sample code has been published openly on GitHub. Anyone building generative video pipelines—regardless of their chosen model framework or underlying GPU hardware—can easily adapt these identical optimization mechanics.

#### Profile Timeline Visual Analysis

<img width="864" height="465" alt="image" src="https://github.com/user-attachments/assets/2d43193a-7d0c-4be7-8c20-ab57032c5aaa" />


*Caption: This exhibits the GPU entering stall phases—the empty gaps on the timeline highlight intervals where the GPU sits completely idle.*
<img width="865" height="460" alt="image" src="https://github.com/user-attachments/assets/78027a53-74fd-40eb-83cd-fe9e755eba48" />


*Caption: Post optimization—the GPU runs continuously without any empty waiting spaces. This is the structural disparity between 82% and 99.9% performance efficiency.*

> Original Technical Reference Blog: https://aws.amazon.com/blogs/architecture/how-synthesia-optimizes-generative-ai-video-inference-on-amazon-ec2-g7e-instances/
