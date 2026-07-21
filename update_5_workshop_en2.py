import pathlib
root = pathlib.Path(r"c:\Baocao\fcj-workshop-template")
files = {
    "content/5-Workshop/_index.md": r"""---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---


# GameHub Serverless CI/CD Workshop

#### Workshop scope

This workshop shows how to build a serverless deployment pipeline for a sample GameHub application using AWS SAM, AWS CodePipeline, and AWS Amplify. The backend is based on AWS Lambda + API Gateway managed by AWS SAM, and the frontend is deployed as a static web app in Amplify.

#### Content

1. [Workshop overview](5.1-Workshop-overview/)
2. [Prerequisites](5.2-Prerequiste/)
3. [Initialize SAM Pipeline](5.3-S3-vpc/)
4. [Configure Repository and Stage](5.4-S3-onprem/)
5. [Testing and Pipeline Validation](5.5a-Testing/)
6. [Monitoring & Logging](5.5b-Monitoring/)
7. [Create CodePipeline in AWS Console](5.5-Policy/)
8. [Deploy Frontend with AWS Amplify](5.6-Cleanup/)
""",
    "content/5-Workshop/5.1-Workshop-overview/_index.md": r"""---
title : "Workshop Overview"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### About this workshop

This workshop uses the GameHub sample project to demonstrate a serverless deployment workflow. The backend is deployed with AWS SAM and AWS CodePipeline, while the frontend is deployed using AWS Amplify.

The goal is to help you understand how to:
- scaffold a two-stage SAM pipeline,
- configure repository and stage metadata,
- add automated tests and monitoring,
- deploy a Flutter web frontend with Amplify.

#### GameHub architecture

GameHub is modeled as a serverless application with:
- AWS Lambda functions for application logic,
- Amazon API Gateway for HTTP APIs,
- AWS Cognito or custom auth for user access,
- AWS Amplify hosting for the frontend.

Note: Add a system architecture diagram here to make the workflow easier to follow. Use `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg` as a placeholder.
""",
    "content/5-Workshop/5.2-Prerequiste/_index.md": r"""---
title : "Prerequisites"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Required tools

- AWS CLI installed and configured.
- AWS SAM CLI installed.
- Git and a GitHub repository with your GameHub project.
- A valid AWS account and permissions to deploy CloudFormation, CodePipeline, CodeBuild, S3, IAM, and CloudWatch resources.
- If you use Flutter web, install Flutter and enable web build support.

#### AWS configuration

1. In your terminal, verify the AWS CLI and SAM CLI versions:
```bash
aws --version
sam --version
```
2. Configure AWS credentials for the account you will use:
```bash
aws configure --profile gamehub
```
3. If you are using a shared profile, use the profile name when running SAM commands.

#### Repository expectations

- `backend/` contains the SAM application and `template.yaml`.
- `frontend/` contains the frontend source code.
- `pipeline/` will be created by `sam pipeline init`.
- Branches such as `main` or `V1` are used for CodePipeline triggers.

Note: Add an image of `aws configure` and `sam --version` output in `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.
""",
    "content/5-Workshop/5.3-S3-vpc/_index.md": r"""---
title : "Initialize SAM Pipeline"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Step 1: Initialize the pipeline

Open a terminal at the root of the GameHub repository and run:
```bash
sam pipeline init --bootstrap
```

When prompted, use the following example values:
- `Select a pipeline template`: `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: `y`

For the Dev stage:
- `Stage configuration name`: `dev`
- `Select a credential source`: `2` (default named profile) and enter `gamehub` if you configured that profile.
- `Enter the region`: `ap-southeast-1` or your preferred region.
- When asked for role ARNs or artifact buckets, press `Enter` to let SAM create them.
- `Does your application contain any IMAGE type Lambda functions?`: `n`

After initialization, SAM generates pipeline files such as `pipeline/samconfig.toml`, `pipeline/codepipeline.yaml`, and `buildspec_deploy.yml`.

#### Commit and push

```bash
git add pipeline/*
git commit -m "chore(ci): add sam pipeline configuration for GameHub"
git push origin main
```

Note: Add a visual placeholder for the init flow in `images/5-Workshop/5.3-S3-vpc/sam-init.svg`.
""",
    "content/5-Workshop/5.4-S3-onprem/_index.md": r"""---
title : "Configure Repository and Stage"
date : 2024-01-01 
weight : 4 
chapter : false
pre : " <b> 5.4. </b> "
---

#### Stage configuration details

When SAM asks for repository and stage settings, use values that match your GameHub project structure. Example values:
- `Repository subfolder`: `backend` or the applicable path where the SAM template lives.
- `Stack name for dev`: `GameHub-dev`.
- `Stack name for prod`: `GameHub-prod`.
- `SSM prefix`: `gamehub/`.
- `Git branch`: `main` or `V1`.
- `SAM template path`: `backend/template.yaml` or `backend/template.yml`.

#### Recommendation

- Keep all pipeline configuration and stage definitions in the `pipeline/` folder.
- Use descriptive stack names so you can identify the stage in CloudFormation and the AWS Console.

#### Commit after configuration

```bash
git add .
git commit -m "ci: add sam pipeline configuration for GameHub"
git push origin main
```

Note: Add a pipeline file placeholder image in `images/5-Workshop/5.4-S3-onprem/pipeline-files.svg`.
""",
    "content/5-Workshop/5.5a-Testing/_index.md": r"""---
title : "Testing and Pipeline Validation"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Purpose

This section explains how to add automated testing to your CI/CD pipeline so that code changes are validated before deployment.

#### What to do

- Add a `Test` stage to your SAM pipeline or CodePipeline.
- Configure a CodeBuild project that installs dependencies and runs unit or integration tests.
- Fail the pipeline if tests do not pass.

#### Example buildspec snippet
```yaml
version: 0.2
phases:
  install:
    commands:
      - pip install -r requirements.txt
      - npm install
  build:
    commands:
      - pytest tests/
      - npm test
artifacts:
  files:
    - '**/*'
```

Note: Add a screenshot placeholder for the test run in `images/5-Workshop/5.5a-Testing/test-run.svg`.
""",
    "content/5-Workshop/5.5b-Monitoring/_index.md": r"""---
title : "Monitoring & Logging"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Purpose

This section reviews how to set up monitoring for the GameHub application, including logs, metrics, and alerts.

#### Key actions

- Enable CloudWatch Logs for Lambda functions and API Gateway.
- Create CloudWatch metric filters for errors and latency.
- Configure alarms for failed deployments, high error rates, or slow API responses.
- Optionally integrate alarms with SNS or email notifications.

#### Monitoring checklist

- Lambda logs are forwarded to CloudWatch.
- API Gateway execution logs are enabled.
- Alarms are set for `5xx` errors and function error rates.
- Notifications are routed to your email or Slack via SNS.

Note: Add an image placeholder for CloudWatch alarms in `images/5-Workshop/5.5b-Monitoring/cloudwatch-alarms.svg`.
""",
    "content/5-Workshop/5.5-Policy/_index.md": r"""---
title : "Create CodePipeline in AWS Console"
date : 2024-01-01
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Create a GitHub connection

1. Open the AWS Console and navigate to Developer Tools > Connections.
2. Click `Create connection`.
3. Select `GitHub` and authorize access to your repository.
4. After authorization, confirm the connection status is `Available`.

#### Configure CodePipeline

1. Open Developer Tools > CodePipeline > Pipelines.
2. Click `Create pipeline`.
3. Choose `Use a blueprint` or `Start from scratch` as needed.
4. Set the source provider to `GitHub (version 2)` and choose your repository and branch.
5. Add a build stage using AWS CodeBuild with `buildspec_deploy.yml` from your repo.
6. Add a deploy stage using CloudFormation and point to `pipeline/codepipeline.yaml` or your template path.

#### Notes

- If you initialized the pipeline with `sam pipeline init`, reuse the generated `codepipeline.yaml` file.
- Save the connection ARN and use it for future automation.

Note: Add UI placeholder images in `images/5-Workshop/5.5-Policy/create-pipeline.svg` and `images/5-Workshop/5.5-Policy/connection-arn.svg`.
""",
    "content/5-Workshop/5.6-Cleanup/_index.md": r"""---
title : "Deploy Frontend with AWS Amplify"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Deploy the frontend app

1. Open AWS Amplify Console.
2. Click `Deploy an app`.
3. Select `GitHub` as the source provider and connect the repository.
4. Choose the frontend branch (for example `V1`).
5. If your repo is a monorepo, enable `My app is a monorepo` and set the root directory to `frontend`.

#### Configure build settings

Use this `amplify.yml` example for Flutter web builds:
```yaml
version: 1
applications:
  - frontend:
      phases:
        build:
          commands:
            - ORIGINAL_DIR=$(pwd)
            - which xz || sudo yum install -y xz
            - cd /tmp
            - wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.0-stable.tar.xz
            - tar xf flutter_linux_3.22.0-stable.tar.xz
            - export PATH="$PATH:/tmp/flutter/bin"
            - cd $ORIGINAL_DIR
            - flutter doctor
            - flutter config --enable-web
            - flutter channel stable
            - flutter upgrade
            - flutter pub get
            - flutter build web --release --dart-define=COGNITO_REGION=$COGNITO_REGION --dart-define=COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID --dart-define=COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID --dart-define=API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL --dart-define=API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL
      artifacts:
        baseDirectory: build/web
        files:
          - "**/*"
      cache:
        paths: []
    appRoot: frontend
```

#### Environment variables

Set the following Amplify environment variables:
- `COGNITO_REGION`
- `COGNITO_USER_POOL_ID`
- `COGNITO_CLIENT_ID`
- `API_GATEWAY_HTTP_URL`
- `API_GATEWAY_WS_URL`
- `LOCAL_API_URL`
- `USE_LOCAL_BACKEND`
- `APK_DOWNLOAD_URL`

#### Finalize deployment

1. Review the Amplify app settings.
2. Click `Save and deploy`.
3. Amplify will build and host the frontend using the source code from GitHub.

Note: Add a setup placeholder image in `images/5-Workshop/5.6-Cleanup/amplify-setup.svg`.
""",
}
for rel, text in files.items():
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
print('Wrote', len(files), 'English workshop files')

