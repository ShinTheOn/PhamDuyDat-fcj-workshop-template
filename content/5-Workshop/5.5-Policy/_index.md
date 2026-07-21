---
title : "Configure AWS SAM Pipeline"
date : 2026-07-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### AWS SAM CI/CD Pipeline Automation Overview

In this section, we will build a complete Continuous Integration and Continuous Deployment (CI/CD) pipeline workflow for the Serverless application using the AWS SAM CLI Pipeline. This workflow automates the entire software delivery lifecycle, from source code unit testing and infrastructure packaging to final application distribution.

The operational architecture flow of the CI/CD pipeline:
* Step 1: The GitHub repository receives a new Git Push event.
* Step 2: AWS CodePipeline automatically triggers the Source stage to pull the latest codebase.
* Step 3: AWS CodePipeline transitions to the UpdatePipeline stage to update the structural pipeline resources.
* Step 4: AWS CodeBuild initiates the UnitTest phase to execute automated testing suites.
* Step 5: AWS CodeBuild triggers the BuildAndPackage phase to compile backend artifacts.
* Step 6: AWS CloudFormation automatically deploys and updates the underlying Serverless resources natively.

---

#### Detailed Deployment Steps

##### Step 1: Initialize and Secure Environment Parameters
Before configuring the operational pipeline workflow, we need to securely store sensitive deployment parameters in a centralized management environment.
1. Navigate to the AWS Systems Manager console > Select Parameter Store from the left navigation panel.
2. Click Create parameter and configure the parameters as follows:
   * Name: /prod/super-admin-email
   * Type: Choose SecureString to encrypt the configuration value.
   * Value: Enter your dedicated system administrator email address.
3. Click Create parameter to complete the initialization.

![Parameter Store verification succeeded]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cb30346a-c85c-469b-848a-c12f1d74650f" />

##### Step 2: Provision Pipeline Infrastructure for the Testing Environment
Utilize the AWS SAM CLI toolsuite to automatically spin up underlying system deployment elements (Execution Roles, S3 Artifact Buckets) dedicated to the testing stage.
1. Open a local Terminal terminal window at the root directory of your project space.
2. Run the initialization command for the Testing stage: sam pipeline bootstrap
3. Provide the technical choices required by the interactive terminal prompt:
   * Configuration name: Input Testing as the target deployment stage identifier.
   * Target Account Stage: Select the associated account execution layer stage.
   * Target Region: Set the target deployment area to ap-southeast-1 (Singapore).
   * Permissions: Choose the native IAM (default) permissions provider.
4. Confirm resource execution to invoke CloudFormation to handle infrastructure allocations.

![Testing environment bootstrap execution completed]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/cc8d0aed-53e5-4494-bfbf-f2fd86c13d2c" />

##### Step 3: Provision Pipeline Infrastructure for the Production Environment (Prod)
Continue initializing separate, isolated continuous delivery resources for your production target environment to achieve environment decoupling.
1. In the terminal session, execute the bootstrap initialization command for the second time: sam pipeline bootstrap
2. Input the parameter selections dedicated to the Production environment infrastructure:
   * Input Prod as the absolute target deployment stage name.
   * Choose ap-southeast-1 as the primary operational landing zone region.
   * Associate the architecture with the pre-provisioned Pipeline User details to finish the setup lifecycle.

![Production environment bootstrap execution completed]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ff65f777-b8a0-493c-856f-48c29c5d7786" />

##### Step 4: Establish Secure CodeStar Connections
To allow AWS CodePipeline to automatically listen for and capture commits pushed to GitHub, establish an authorized secure source connection.
1. Navigate to the AWS CodePipeline console > Expand Developer Tools > Click Connections.
2. Locate the designated deployment association matching your application identifier (e.g., GameHub).
3. Verify that the current operational connection status displays a green Available tag, confirming GitHub App handshake permissions.

![CodeStar source repository connection successful]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/534c08d0-47c5-4b42-a89d-4b0f92a5d40c" />

##### Step 5: Verify Continuous Integration Pipeline Executions
Push fresh application commits to your GitHub repository to trigger the automated delivery pipeline lifecycle.
1. Execute the standard Git sequence to push local updates to the main branch repository:
git add .
git commit -m "deploy: trigger serverless sam pipeline workflow"
git push origin main
2. Access the main AWS CodePipeline dashboard and open the designated pipeline called Gamehub-Pipeline to watch the automation build blocks.
3. Track execution stability across the 4 key structural stages: Source, UpdatePipeline, UnitTest, and BuildAndPackage.

![Gamehub-Pipeline execution flow succeeded]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/094c24c4-4f57-410b-8e22-cef2eaf8a5bf" />

##### Step 6: Validate CodeBuild Project Tasks Statuses
1. Switch over to the AWS CodeBuild dashboard view > Click Build projects.
2. Audit the detailed processing status of the 4 granular task instances. The Latest build status column tracking column for all entries must display a green check mark stating Succeeded.

![AWS CodeBuild sub-projects compilation tasks succeeded]<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/04a3332a-4a5f-4f76-8dad-4897940ab8e2" />
