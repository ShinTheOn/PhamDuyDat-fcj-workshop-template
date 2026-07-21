---
title : "Chuẩn bị trước Workshop"
date: 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Yêu cầu chuẩn bị trước workshop

Trước khi triển khai workshop, bạn cần chuẩn bị đầy đủ các yếu tố sau:
- Tài khoản AWS đã đăng nhập và có quyền sử dụng các dịch vụ: IAM, Lambda, API Gateway, S3, CloudFormation, CodePipeline, CodeBuild, Amplify, Cognito, CloudWatch, WAF và CodeConnections.
- Một repository trên GitHub chứa mã nguồn GameHub.
- Một nhánh Git dùng cho deployment, ví dụ `V1` hoặc `main`.
- Cấu trúc thư mục rõ ràng, đặc biệt nếu dự án là monorepo gồm `backend/` và `frontend/`.
- Máy tính cài sẵn Git, AWS CLI, AWS SAM CLI và Python. Nếu frontend dùng Flutter, nên chuẩn bị sẵn Flutter SDK để build và kiểm tra cấu hình.

#### Kiểm tra môi trường

1. Mở terminal tại thư mục gốc của dự án.
2. Kiểm tra các công cụ cần thiết:
```powershell
aws --version
sam --version
git --version
python --version
```
3. Cấu hình profile AWS cho workshop:
```powershell
aws configure --profile gamehub
```
4. Xác nhận profile hoạt động:
```powershell
aws sts get-caller-identity --profile gamehub
```

#### Thông tin cần chuẩn bị trước workshop

Bạn nên có sẵn các thông tin sau trước khi làm các bước thực hiện:
- `Region`: ví dụ `ap-southeast-1`.
- `AWS profile`: ví dụ `gamehub`.
- `Repository name`: ví dụ `DTDuc04/DoAnMiniGame`.
- `Repository subfolder`: ví dụ `backend` hoặc `frontend`.
- `SSM Prefix`: ví dụ `gamehub/` hoặc để trống nếu dùng mặc định.
- `Git branch`: ví dụ `V1`.
- `Template path`: ví dụ `backend/codepipeline.yaml`.
- `Stack names`: ví dụ `GameHub-dev`, `GameHub-prod`, `GameHubPipeline`.
- `Connection name` cho GitHub trên AWS CodeConnections: ví dụ `GameHub`.
- Các biến môi trường frontend như `COGNITO_REGION`, `COGNITO_USER_POOL_ID`, `API_GATEWAY_HTTP_URL`, v.v.

#### Hướng dẫn cài đặt nhanh

1. Cài AWS CLI nếu cần:
```powershell
pip install --user awscli
aws --version
```
2. Cài AWS SAM CLI nếu cần:
```powershell
pip install --user aws-sam-cli
sam --version
```
3. Cấu hình profile workshop:
```powershell
aws configure --profile gamehub
```

#### Checklist chuẩn bị

- [x] Có tài khoản AWS và quyền phù hợp
- [x] Có repository GitHub và nhánh deploy
- [x] Đã cài AWS CLI và SAM CLI
- [x] Đã cấu hình profile AWS
- [x] Đã chuẩn bị thông tin repo, branch, stack name và biến môi trường

#### Gợi ý

- Nếu repository là monorepo, nên tách riêng `backend/` và `frontend/` để cấu hình pipeline và Amplify dễ hơn.
- Dùng branch deploy riêng để kiểm soát thay đổi và giảm rủi ro.
- Nếu triển khai nhiều môi trường, có thể tạo profile riêng như `gamehub-dev` và `gamehub-prod`.

Note (hình ảnh): Thêm ảnh minh họa cho `aws configure`, `sam --version` và cấu trúc repository tại `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.

