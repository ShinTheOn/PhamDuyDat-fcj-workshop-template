---
title : "Initialize CI/CD Pipeline"
date: 2026-07-12
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Objectives

In this section, you will initialize the initial pipeline configuration for the GameHub backend using AWS SAM and AWS CodePipeline. This step establishes the foundation for the build, deployment, and Dev/Prod environment management workflow.

#### Step 1: Initialize the pipeline

1. Open a terminal in the project root.
2. Run the following command to start the pipeline initialization process:
```bash
sam pipeline init --bootstrap
```
3. When prompted, choose the following options:
- `Select a pipeline template`: choose `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: choose `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: choose `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: enter `y` (Yes)

> Note: This step creates the initial pipeline structure, including the template files and bootstrap resources needed for deployment on AWS.

#### Step 2: Configure the Dev stage

After selecting `y`, AWS SAM will begin setting up the first stage for the development environment.

1. `Stage configuration name`: enter `dev`
2. `Select a credential source`: choose `2` (default named profile)
3. `Enter the region`: enter `ap-southeast-1` or the AWS region you are using
4. If prompted for a profile, enter `gamehub`
5. When asked about ARNs, IAM roles, artifact buckets, or related resources, press `Enter` to let SAM use the default values
6. `Does your application contain any IMAGE type Lambda functions?`: enter `n`

> Note: If you are unsure which value to enter, using the default option by pressing Enter is usually the simplest way to continue.

#### Step 3: Configure the Prod stage

Once the Dev stage is completed, the wizard will continue by helping you configure the second stage for the production environment.

1. `Stage configuration name`: enter `prod`
2. `Select a credential source`: choose the same option as in the Dev stage
3. `Enter the region`: use the same region as Dev or choose another region if you want to separate environments

#### Step 4: Verify the initialization result

After the process finishes, verify the generated pipeline folder with:
```bash
ls pipeline
```

You should see the following important files:
- `pipeline/samconfig.toml`
- `pipeline/codepipeline.yaml`
- `buildspec_deploy.yml`

#### Expected result

- The pipeline has been successfully initialized with AWS SAM.
- The pipeline configuration files are present in the `pipeline` folder.
- You are now ready for the next steps, including GitHub integration, stage configuration, and deployment.

#### Notes

- `sam pipeline init --bootstrap` creates bootstrap resources such as the S3 artifact bucket.
- `samconfig.toml` stores the stage, profile, and deployment-related configuration.
- You can edit this file after initialization if you need to customize it for your environment.

![Ảnh 1](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.3-Pipeline-setup/anh1.png)

![Ảnh 2](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.3-Pipeline-setup/anh2.png)




