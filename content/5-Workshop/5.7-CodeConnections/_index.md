---
title : "Connect GitHub to AWS CodePipeline"
date: 2026-07-12
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Goal

This section explains how to connect AWS CodePipeline to GitHub using AWS CodeConnections so the pipeline can automatically retrieve source code and start deployment.

#### Step 5: Connect AWS CodePipeline to GitHub using AWS CodeConnections

To allow the pipeline to fetch code from GitHub automatically, you need to create a secure connection between AWS and your GitHub account.

##### 5.1. Create the connection in AWS

![Ảnh 1](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.7-CodeConnections/anh1.png)

1. In the AWS Console, go to `Developer Tools` → `Settings` → `Connections`.
2. Click `Create connection`.

##### 5.2. Configure the provider information

![Ảnh 2](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.7-CodeConnections/anh2.png)

1. `Select a provider`: choose `GitHub`.
2. `Connection name`: enter a name such as `GameHub`.
3. Click `Connect to GitHub`.

##### 5.3. Authenticate and grant access on GitHub

![Ảnh 3](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.7-CodeConnections/anh3.png)

1. The browser will redirect you to the GitHub authentication page.
2. Make sure you are signed in to the correct GitHub account.
3. Enter your password or complete any required two-factor authentication.
4. Click `Confirm` to allow AWS to access your repository.

##### 5.4. Verify the connection is ready

![Ảnh 4](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.7-CodeConnections/anh4.png)

1. After successful authentication, you will be redirected back to AWS and see the success message `Connection GameHub created successfully`.
2. Check the `Status` field. If it shows `Available` in green, the connection is ready to use.

#### Expected result

When this step is complete, you will have a secure connection between AWS and GitHub, allowing CodePipeline to pull source code automatically for deployment.

#### Important note

- Use a short, recognizable connection name such as `GameHub`.
- If the connection does not show `Available`, wait a few minutes and check again.


