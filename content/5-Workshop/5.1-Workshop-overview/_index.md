---
title : "Workshop Overview"
date: 2026-07-12
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Workshop objectives

In this workshop, you will build and deploy a GameHub serverless application on AWS by:
- initializing a CI/CD pipeline for the backend with AWS SAM,
- configuring Dev and Prod environments for deployment,
- connecting your GitHub repository to AWS CodePipeline through AWS CodeConnections,
- deploying the backend with CloudFormation and the frontend with AWS Amplify,
- protecting the frontend with AWS WAF and monitoring the application with Amazon CloudWatch.

#### Key content

1. Initialize the pipeline with `sam pipeline init --bootstrap`.
2. Set up Dev and Prod stages, repository settings, template paths, stack names, and deployment branches.
3. Connect GitHub to CodePipeline so code changes can automatically trigger deployment.
4. Deploy a Flutter web frontend on AWS Amplify and configure environment variables for the build.
5. Strengthen application security with AWS WAF and monitor the system through CloudWatch.

#### Architecture and technologies

GameHub is a serverless application built on Amazon services:
- AWS Lambda handles business logic.
- Amazon API Gateway provides HTTP/WebSocket APIs.
- Amazon Cognito manages user authentication.
- AWS Amplify hosts the frontend web app.
- AWS CodePipeline and AWS SAM support CI/CD.
- AWS WAF protects the application from common web attacks.

#### Notes

- The project name `GameHub` is an example; replace it with your own project name.
- If your backend and frontend live in the same repository, keep their folders clearly separated.
- Verify your AWS profile and region before running SAM commands.

Note: Add an architecture diagram here to make the workflow clearer. Placeholder: `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg`.

