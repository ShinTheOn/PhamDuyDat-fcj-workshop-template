---
title : "Create a Pipeline in the AWS Console"
date: 2026-07-12
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Goal

This section walks you through creating a new pipeline in the AWS Console using a CloudFormation template and connecting it to the GitHub repository you configured earlier.

#### Step 6: Initialize and configure CodePipeline in the AWS Console

Once the GitHub connection is ready, you can create a pipeline directly from the AWS Console to automate build and deployment.

![Ảnh 1](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.8-Pipeline-console-setup/anh1.png)

##### 1. Choose the deployment type and template

![Ảnh 2](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.8-Pipeline-console-setup/anh2.png)

1. In the left navigation pane, go to `Developer Tools` → `CodePipeline` → `Pipelines`.
2. Click `Create pipeline`.
3. On the initial configuration page:
   - `Category`: select `Deployment`.
   - `Template`: choose `Deploy to CloudFormation (Deploy your cloud formation template)`.
4. Click `Next`.

##### 2. Set up the source stage

![Ảnh 3](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.8-Pipeline-console-setup/anh3.png)

Connect the GitHub repository that you linked earlier:

1. `Source provider`: choose `GitHub (via GitHub App)`.
2. `Connection`: select the GitHub connection you created in the previous step.
3. `Repository name`: choose the correct repository for your project, for example `DTDuc04/DoAnMiniGame`.
4. `Default branch`: enter the branch that should trigger deployment, for example `V1`.
5. `Output artifact format`: keep the default `CodePipeline default` value.
6. Click `Next`.

##### 3. Configure the template parameters

![Ảnh 4](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.8-Pipeline-console-setup/anh4.png)

Fill in the details that identify the pipeline and CloudFormation stack:

1. `CodePipelineName`: give the pipeline a recognizable name, for example `DeployToCloudFormationService`.
2. `StackName`: enter the CloudFormation stack name, for example `GameHub`.
3. `TemplatePath`: provide the path to the YAML template file in your repository, for example `backend/codepipeline.yaml`.
4. `OutputFileName`: specify the output filename, for example `output.json`.

##### 4. Review permissions and finish setup

![Ảnh 5](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.8-Pipeline-console-setup/anh5.png)

1. Scroll down to `CloudFormationResourcePermissions` and review the default permissions granted to CloudFormation.
2. `RetentionPolicy`: choose what should happen when the stack is deleted, for example `Delete`.
3. Review the information in the `Preview` section.
4. Click `Create pipeline from template` in the lower-right corner.

#### Expected result

After the pipeline is created, CodePipeline will automatically run the build and deployment workflow whenever code is pushed to the `V1` branch on GitHub.

#### Important note

- Make sure the repository name and branch name match your actual project.
- If the pipeline does not start immediately, wait a few minutes for AWS to finish the initialization process.


