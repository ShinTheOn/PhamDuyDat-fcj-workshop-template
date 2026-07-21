---
title : "Connect GitHub to AWS CodePipeline"
date: 2026-07-12
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Goal

This section explains how to connect AWS CodePipeline to GitHub using AWS CodeConnections so the pipeline can automatically retrieve source code and start deployment.

#### Step 5: Connect AWS CodePipeline to GitHub using AWS CodeConnections

To allow the pipeline to fetch code from GitHub automatically, you need to create a secure connection between AWS and your GitHub account.

##### 5.1. Create the connection in AWS

1. In the AWS Console, go to `Developer Tools` → `Settings` → `Connections`.
2. On the main page, click `Create connection`.
3. The console will prompt you to select a provider. Choose `GitHub`.

> Note: This connection is required because CodePipeline cannot access your GitHub repository without it.

##### 5.2. Configure the provider information

1. `Select a provider`: choose `GitHub`.
2. `Connection name`: enter a name such as `GameHub`.
3. Click `Connect to GitHub` to begin the authentication process.

> Note: Use a clear and memorable name so it is easy to identify later in AWS.

##### 5.3. Authenticate and grant access on GitHub

1. The browser will redirect you to the GitHub authentication page.
2. Make sure you are signed in to the correct GitHub account.
3. Enter your password or complete any required two-factor authentication.
4. Click `Confirm` to allow AWS to access your repository.

> Note: If you manage multiple GitHub accounts or organizations, confirm that you are giving access to the correct repository owner.

##### 5.4. Verify the connection is ready

1. After successful authentication, you will be redirected back to AWS and see the success message `Connection GameHub created successfully`.
2. Go back to the `Connections` page and check the status.
3. If the status shows `Available` in green, the connection is ready to be used by the pipeline.

#### Expected result

When this step is complete, you will have a secure connection between AWS and GitHub, enabling CodePipeline to pull source code automatically for deployment.

#### Important note

- Keep the connection name and ARN handy for future pipeline configuration.
- If the status does not change to `Available`, wait a few minutes and check again.



