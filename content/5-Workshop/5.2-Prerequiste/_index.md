---
title : "Prerequisites"
date : 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### 1. Account & Region

+ An AWS account with billing enabled (personal account or one provided by the FCJ program).
+ Deployment region: **`ap-southeast-1` (Singapore)** — every resource in the diagram (Amplify, API Gateway, Lambda, DynamoDB, Cognito…) is created in this region.
+ A registered domain if you want Route 53 to point a custom domain at Amplify; otherwise you can use Amplify's default domain for testing first.

#### 2. Tools to Install

| Tool | Minimum Version | Used For |
|---|---|---|
| AWS CLI | v2.x | Authenticate & interact with AWS via `aws configure` |
| AWS SAM CLI | latest | Build & deploy the backend (API Gateway, Lambda, DynamoDB) as IaC |
| Git | any | Clone the source and push to GitHub to trigger GitHub Actions |
| Node.js | 18.x or later | Runtime for the 3 Lambda functions (`$connect`, Game Logic, `$disconnect`) — swap for Python/Java if you chose a different runtime |
| Flutter SDK | latest | Build & run the Mobile App (if you're continuing client-side development) |
| Docker | latest (optional) | Container build when `sam build` needs to package dependencies |

Verify your installation:
```bash
aws --version
sam --version
git --version
node --version
```

#### 3. Required IAM Permissions

Attach the following policy (or an equivalent) to the IAM user/role used to deploy this workshop with AWS SAM:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WorkshopDeployPermissions",
            "Effect": "Allow",
            "Action": [
                "cloudformation:*",
                "s3:*",
                "lambda:*",
                "apigateway:*",
                "execute-api:ManageConnections",
                "dynamodb:*",
                "cognito-idp:*",
                "amplify:*",
                "route53:*",
                "route53domains:*",
                "wafv2:*",
                "logs:*",
                "cloudwatch:*",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:AttachRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListRolePolicies",
                "iam:PassRole"
            ],
            "Resource": "*"
        }
    ]
}
```

{{% notice warning %}}
⚠️ This policy is for a **lab/learning environment**. For production, scope `Resource` down to the exact ARNs of each resource (stack, bucket, table, function…) instead of `*`, following the principle of least privilege.
{{% /notice %}}

#### 4. Recommended Background Knowledge

+ The concept of a **WebSocket API** and how it differs from REST (a persistent bidirectional connection vs. discrete request/response calls).
+ Basic **IAM**: Roles, Policies, Execution Roles, least privilege.
+ Basic **DynamoDB**: partition keys, on-demand capacity mode.
+ The **JWT/OAuth2** authentication flow with a Cognito User Pool.
+ Basic **CI/CD** knowledge: GitHub Actions workflow structure, AWS SAM's `template.yaml` syntax.
