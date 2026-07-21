---
title : "Workshop Overview"
date : 2026-07-12
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### 1. Context and Problem Statement

This workshop builds the **backend for a real-time multiplayer game**, serving players through either a **Mobile App (Flutter)** or a **Web App (browser)**.

For a multiplayer game, the traditional REST API pattern (client asks, server answers) doesn't fit: the server needs to **actively push** match-state updates to every connected player the moment something happens (e.g., a player makes a move), instead of clients repeatedly polling — which wastes resources and adds latency that hurts gameplay.

Beyond the real-time requirement, the system also needs to solve for:
+ Securely authenticating players before they can join a match.
+ Infrastructure that scales automatically with the number of concurrent players, without pre-provisioning servers.
+ A CI/CD pipeline so the team can ship features and fixes quickly without manual console work.

#### 2. Specific Goals

+ Build a **bidirectional real-time channel** between clients and the backend using an **API Gateway WebSocket API**.
+ Authenticate players with **Amazon Cognito**, protecting every WebSocket connection with a **Lambda Authorizer**.
+ Store each player's `connectionId` and match state in **DynamoDB** with single-digit-millisecond read/write latency.
+ Automatically **broadcast** match-state updates to every connected player via the API Gateway Management API (`@connections`).
+ Host and distribute the frontend through **AWS Amplify** (Hosting + CDN), protected by **AWS WAF**, with domain routing via **Route 53**.
+ Automate deployment of the whole system (web + backend) with **GitHub Actions + AWS SAM** on every Git push.
+ Centralize operational monitoring through **CloudWatch** (Logs/Alarms).

#### 3. System Architecture (Architecture Diagram)

![architecture](/images/5-Workshop/5.1-Workshop-overview/architecture.png)

The architecture has 4 main layers inside AWS Cloud (region **ap-southeast-1**):

| Layer | Components | Function |
|---|---|---|
| **Edge Layer** | Route 53, AWS WAF, AWS Amplify | DNS resolution, filtering malicious traffic, hosting & distributing the web app via CDN |
| **Security Layer** | Amazon Cognito, IAM Role | User authentication, least-privilege permissions for the Lambda functions |
| **Serverless Game Layer** | API Gateway (WebSocket), 3 Lambda functions (`$connect`, Game Logic, `$disconnect`), DynamoDB, CloudWatch | Connection management, real-time game logic, state storage, monitoring |
| **CI/CD Layer** | GitHub Actions, AWS SAM | Automated build & deploy for both web and backend from source |

**Main processing flow (16 steps):**

*Loading the web app*
1. The user (Mobile App/Web App) accesses the system's domain.
2. Route 53 resolves DNS and routes the request to AWS WAF.
3. AWS WAF filters malicious traffic, then forwards the request to AWS Amplify to fetch the web files.
4. AWS Amplify returns the web app (SPA) to the browser/app.

*User authentication*
5. The client calls the `/auth/*` endpoint to log in through Amazon Cognito and receive a token (JWT).

*Establishing the real-time connection*
6. Using that token, the client connects **directly over WSS** to the API Gateway WebSocket endpoint (bypassing Amplify).
7. API Gateway invokes the **Lambda Authorizer** to validate the token against Cognito before accepting the connection.
8. If valid, the `$connect` route fires and invokes the `$connect` Lambda.
9. The `$connect` Lambda stores the player's `connectionId` in DynamoDB (Connections table).

*Real-time game logic*
10. When a player performs an in-game action, the client sends an event over the WebSocket; API Gateway routes it to the Game Logic Lambda.
11. The Game Logic Lambda reads/writes match state in DynamoDB (Games table).
12. The Game Logic Lambda calls the API Gateway Management API to **push via `@connections`**, broadcasting the new state to every player connected to that match.

*Disconnecting*
13. When a player leaves or drops the connection, the `$disconnect` route fires and invokes the `$disconnect` Lambda.
14. The `$disconnect` Lambda removes that `connectionId` from DynamoDB.

*CI/CD*
15. A developer pushes code to the GitHub repo, triggering GitHub Actions.
16. GitHub Actions builds and deploys with AWS SAM: **(16a)** deploys the web app to Amplify, **(16b)** deploys the backend (API Gateway, Lambda, DynamoDB…).

Throughout the system, each Lambda function runs under its own **Execution Role** (least-privilege IAM Role), and logs from the serverless layer flow to **CloudWatch** for monitoring.

#### 4. Why These Services

| AWS Service | Role | Why It Was Chosen |
|---|---|---|
| Route 53 | DNS for the system's domain | Managed DNS, low latency, integrates natively with Amplify/CloudFront |
| AWS WAF | Filters malicious traffic at the edge | Blocks common attacks (SQLi, XSS, bad bots) before they reach Amplify, without running a firewall yourself |
| AWS Amplify | Web hosting & CDN | Built-in CI/CD, global CDN, HTTPS, custom domains — faster than hand-building S3 + CloudFront |
| Amazon Cognito | User authentication | Managed user pool, issues JWTs, integrates directly with a Lambda Authorizer — no need to build auth from scratch |
| API Gateway (WebSocket) | Bidirectional real-time channel | Unlike REST, WebSocket lets the server actively push data — required for a multiplayer game, avoids polling |
| AWS Lambda | Runs `$connect`/Game Logic/`$disconnect` | Serverless, scales automatically with concurrent connections, pay-per-invocation — better suited to a game's uneven traffic than EC2, which bills even while idle |
| Amazon DynamoDB | Stores connectionIds & match state | Single-digit-millisecond latency, scales horizontally, on-demand mode fits spiky game traffic — a better fit than RDS, which struggles with connection pooling across many concurrent Lambdas |
| CloudWatch | Logs & Alarms | Native integration with Lambda/API Gateway, easy to alarm on errors or abnormal traffic without extra tooling |
| AWS SAM | Infrastructure as Code & CI/CD | Purpose-built for serverless, more concise than raw CloudFormation, integrates cleanly with GitHub Actions |

{{% notice note %}}
For each service, it's worth naming the alternative you considered but didn't choose — WebSocket API vs. REST + polling, Lambda vs. EC2/ECS, DynamoDB vs. RDS — to make the trade-off explicit between cost, operational complexity, and the low-latency requirements of a real-time game.
{{% /notice %}}

#### 5. Security and Operations

+ **IAM:** each Lambda (`$connect`, Game Logic, `$disconnect`) has its own Execution Role, granted only the DynamoDB and API Gateway Management API actions it actually needs — the principle of least privilege.
+ **Authentication:** every WebSocket connection must carry a valid token (obtained in step 5), verified by the Lambda Authorizer against Cognito before API Gateway accepts the `$connect` — there are no anonymous connections.
+ **Edge protection:** AWS WAF sits in front of Amplify to filter malicious traffic before it reaches the app.
+ **Monitoring:** logs from the serverless game layer flow to CloudWatch; set alarms when Lambda error/throttle rates exceed a threshold.
+ **Scalability:** Lambda scales automatically with concurrent WebSocket events; DynamoDB on-demand scales with read/write traffic; API Gateway WebSocket supports thousands of concurrent connections; the Amplify CDN distributes the web app globally.
