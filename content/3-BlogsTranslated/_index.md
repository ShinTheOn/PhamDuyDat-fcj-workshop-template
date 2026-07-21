---
title: "Translated Blogs"
date: 2026-07-09
weight: 3
chapter: false
pre: " <b> 3. </b> "
---


### [Blog 1 - How Synthesia Optimizes Video Generation AI on Amazon EC2 G7e](3.1-Blog1/)
This post analyzes a technical solution called the *Asynchronous Frame Generation Pipeline*, jointly developed by Synthesia and AWS. By decoupling the GPU computing workload and leveraging the CPU to write data in parallel through a memory buffer queue mechanism, the system pushed GPU efficiency from 82% to a maximum of 99.9%. This solution increases video processing speeds by 8.2% and saves up to $900 in infrastructure operating costs per 1,000 video rendering hours—all without requiring any modifications to the core AI model architecture.

### [Blog 2 - Automated Patient Record Digitization with AI](3.2-Blog2/)
This blog introduces an automated pipeline architecture designed to convert and digitize traditional scanned PDF medical records into structured data. The system harnesses the artificial intelligence power of Amazon Bedrock Data Automation to extract over 50 core clinical data attributes, then utilizes the serverless AWS Lambda service to map the data into the globally recognized FHIR R4 healthcare standard before securely storing it in AWS HealthLake to optimize data query and exchange workflows.

### [Blog 3 - How AWS Optimizes AI for Autonomous Field Robots](3.3-Blog3/)
This post explores how agritech company Aigen collaborated with the AWS SageMaker AI ecosystem to successfully deploy machine learning models onto resource-constrained hardware (Edge AI) onboard solar-powered weeding robots. The post dives into three core architectural solutions: automating image data labeling using foundation vision models (SAM2, Grounding DINO) combined with Active Learning; model distillation and INT8 quantization into a lightweight 2MB TFLite format; and establishing an automated closed-loop feedback system for continuous over-the-air updates via Amazon S3.
