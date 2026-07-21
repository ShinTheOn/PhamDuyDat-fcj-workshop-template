---
title : "Các điều kiện tiên quyết"
date : 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### 1. Tài khoản & Khu vực (Account & Region)

+ Tài khoản AWS đã kích hoạt billing (tài khoản cá nhân hoặc tài khoản được cấp bởi chương trình FCJ).
+ Region triển khai: **`ap-southeast-1` (Singapore)** — toàn bộ resource trong sơ đồ (Amplify, API Gateway, Lambda, DynamoDB, Cognito…) đều được tạo trong region này.
+ Một domain đã đăng ký sẵn nếu muốn dùng Route 53 trỏ về Amplify với custom domain; nếu chưa có, có thể dùng domain mặc định do Amplify cấp để test trước.

#### 2. Công cụ cần cài đặt

| Công cụ | Phiên bản tối thiểu | Dùng để |
|---|---|---|
| AWS CLI | v2.x | Đăng nhập & thao tác AWS qua `aws configure` |
| AWS SAM CLI | mới nhất | Build & deploy backend (API Gateway, Lambda, DynamoDB) bằng IaC |
| Git | bất kỳ | Clone source code, push lên GitHub để trigger GitHub Actions |
| Node.js | 18.x trở lên | Runtime cho 3 Lambda function (`$connect`, Game Logic, `$disconnect`) — đổi sang Python/Java nếu bạn chọn runtime khác |
| Flutter SDK | mới nhất | Build & chạy Mobile App (nếu bạn phát triển tiếp phần client) |
| Docker | mới nhất (tuỳ chọn) | Container build khi `sam build` cần đóng gói dependencies |

Kiểm tra đã cài đặt thành công:
```bash
aws --version
sam --version
git --version
node --version
```

#### 3. Quyền hạn IAM cần thiết

Gắn policy sau (hoặc tương đương) vào IAM user/role dùng để deploy workshop này bằng AWS SAM:

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
⚠️ Đây là policy cho môi trường **lab/học tập**. Với production, hãy giới hạn `Resource` về đúng ARN của từng resource (stack, bucket, table, function…) thay vì dùng `*`, theo đúng nguyên tắc đặc quyền tối thiểu.
{{% /notice %}}

#### 4. Kiến thức nền tảng nên biết trước

+ Khái niệm **WebSocket API** và điểm khác biệt so với REST API (kết nối liên tục hai chiều thay vì request/response rời rạc).
+ **IAM** cơ bản: Role, Policy, Execution Role, nguyên tắc least privilege.
+ **DynamoDB** cơ bản: partition key, chế độ on-demand capacity.
+ Luồng xác thực **JWT/OAuth2** với Cognito User Pool.
+ Kiến thức **CI/CD** cơ bản: cấu trúc GitHub Actions workflow, cú pháp `template.yaml` của AWS SAM.
