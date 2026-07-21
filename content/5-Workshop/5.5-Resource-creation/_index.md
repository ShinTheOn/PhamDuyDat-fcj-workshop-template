---
title : "Confirm and Create Resources"
date: 2026-07-12
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Goal

In this section, you will continue the pipeline setup by reviewing the configuration carefully before AWS creates the actual resources. This is a critical step to ensure the deployment workflow runs smoothly.

#### Step 3: Confirm and create the resources

After you have entered the required information for the stages and pipeline settings, the system will display a summary screen so you can review everything before creating resources.

1. The system will show a configuration summary table (Summary).
2. Review each item carefully, including the stage names, region, profile, template path, stack name, and the resources that will be created automatically.
3. If everything looks correct, press `Enter` to continue.
4. At the prompt `Should we proceed with the creation? [y/N]`, enter `y` to confirm resource creation.
5. Wait for the process to complete. When it finishes successfully, you will see the message `Successfully created!`.


#### What to check before creating

Before pressing `y`, make sure the following are correct:
- The stage names `dev` and `prod` are set properly.
- The AWS region matches your deployment environment.
- The AWS profile is configured and has permission to create stacks, buckets, roles, and other required resources.
- The template path and stack name point to the correct project files.
- If values such as ARN, role, or bucket are left blank, SAM will create them automatically, but you should still verify that the defaults make sense for your setup.

#### Why this confirmation step matters

When you choose `y`, AWS SAM will:
- Create the bootstrap resources required for the pipeline.
- Create the stacks needed for the Dev and Prod environments.
- Set up the initial deployment configuration and pipeline files.

If the process completes successfully, you will see `Successfully created!`, which indicates the pipeline configuration and resources are ready for the next step.

#### Expected result

After this step, you will have:
- A pipeline configuration ready for further customization or GitHub integration.
- AWS resources created automatically for deployment.
- A foundation prepared for the next phase of the workflow.

![Ảnh 1]({{ "/images/5-Workshop/5.5-Resource-creation/anh1.png" | relURL }})

![Ảnh 2]({{ "/images/5-Workshop/5.5-Resource-creation/anh2.png" | relURL }})

