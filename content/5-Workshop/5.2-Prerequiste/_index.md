---
title : "Prerequisites for the Workshop"
date: 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Required preparations for the workshop

Before starting the workshop, make sure you have the following ready:
- An AWS account with access to IAM, Lambda, API Gateway, S3, CloudFormation, CodePipeline, CodeBuild, Amplify, Cognito, CloudWatch, WAF, and CodeConnections.
- A GitHub repository containing the GameHub source code.
- A deployment branch such as `V1` or `main`.
- A clear project structure, especially if the repository is a monorepo with separate `backend/` and `frontend/` folders.
- Git, AWS CLI, AWS SAM CLI, and Python installed locally. If you are working with the Flutter frontend, prepare the Flutter SDK as well.

#### Environment checks

1. Open a terminal in the project root.
2. Verify the required tools:
```bash
aws --version
sam --version
git --version
python --version
```
3. Configure your AWS profile for the workshop:
```bash
aws configure --profile gamehub
```
4. Verify that the profile is working:
```bash
aws sts get-caller-identity --profile gamehub
```

#### Information to prepare before the workshop

Have the following details ready before you begin the deployment steps:
- `Region`, e.g. `ap-southeast-1`.
- `AWS profile`, e.g. `gamehub`.
- `Repository name`, e.g. `DTDuc04/DoAnMiniGame`.
- `Repository subfolder`, e.g. `backend` or `frontend`.
- `SSM Prefix`, e.g. `gamehub/` or leave it blank to use the default.
- `Git branch`, e.g. `V1`.
- `Template path`, e.g. `backend/codepipeline.yaml`.
- `Stack names`, e.g. `GameHub-dev`, `GameHub-prod`, `GameHubPipeline`.
- `Connection name` for GitHub in AWS CodeConnections, e.g. `GameHub`.
- Frontend environment variables such as `COGNITO_REGION`, `COGNITO_USER_POOL_ID`, and `API_GATEWAY_HTTP_URL`.

#### Quick setup

1. Install AWS CLI if needed:
```bash
pip install --user awscli
aws --version
```
2. Install AWS SAM CLI if needed:
```bash
pip install --user aws-sam-cli
sam --version
```
3. Configure the workshop profile:
```bash
aws configure --profile gamehub
```

#### Preparation checklist

- [x] AWS account and required permissions available
- [x] GitHub repository and deployment branch ready
- [x] AWS CLI and SAM CLI installed
- [x] AWS profile configured
- [x] Repository details, stack names, and environment variables prepared

#### Tips

- In a monorepo, keep `backend/` and `frontend/` clearly separated for easier pipeline and Amplify configuration.
- Use a dedicated deployment branch to control changes and reduce risk.
- Create separate profiles such as `gamehub-dev` and `gamehub-prod` if you plan to manage multiple environments.

Note: Add a screenshot of `aws configure`, `sam --version`, and the repository structure in `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.

