---
title : "Configure the Dev Stage"
date: 2026-07-12
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Goal

This section walks you through the detailed setup of the Development stage for the SAM pipeline, including the stage name, credential source, AWS region, and the default values that AWS SAM can create automatically.

#### Step 1: Enter the Dev stage information

When the setup wizard asks for the Development environment settings, follow the options below:

1. `Stage configuration name`: enter `dev`
2. `Select a credential source`: choose `2` (default named profile)
3. `Enter the region`: enter your AWS region, for example `ap-southeast-1`
4. If prompted for a profile, enter `gamehub` if you already configured one
5. When the wizard asks for values such as ARN, IAM user, execution role, or artifact bucket, press `Enter` to skip them. AWS SAM will create these resources automatically
6. `Does your application contain any IMAGE type Lambda functions?`: enter `n` (No)

> Note: This step is important because the Dev stage is the first environment used to test and deploy the application before moving on to Prod.

#### Step 2: Understand the key choices

- `Stage configuration name = dev`: helps distinguish the development environment from the production environment.
- `default named profile`: allows SAM to use the AWS profile already configured on your machine.
- `Enter the region`: must match the AWS region you are using to avoid issues with stack or bucket creation.
- Pressing `Enter` for ARM, role, or bucket values: lets SAM bootstrap the necessary resources automatically.
- Selecting `n` for IMAGE type Lambda: fits most applications that do not use container-based Lambda images.

#### Step 3: Double-check before continuing

After entering the information, verify the following:
- The stage name is `dev`
- The region matches your AWS environment
- The AWS profile is confirmed to work
- There are no access or IAM configuration issues

#### Expected result

Once the setup is complete, you are ready to continue with the next stage of the pipeline workflow, where the Dev environment will be used as the initial deployment target.

![Ảnh 1]({{ "/images/5-Workshop/5.4-Stage-setup/anh1.png" | relURL }})


