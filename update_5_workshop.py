from pathlib import Path
base = Path('content/5-Workshop')
files = {
    '5.2-Prerequiste/_index.vi.md': '''---
title : "Chuẩn bị"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Yêu cầu trước khi bắt đầu

Trước khi thiết lập pipeline và triển khai frontend, bạn cần chuẩn bị:
- Tài khoản AWS với quyền tạo CodePipeline, CloudFormation, IAM, S3, CodeCommit, Amplify và các dịch vụ liên quan.
- AWS CLI và AWS SAM CLI đã cài đặt trên máy.
- GitHub account và repository chứa mã nguồn.
- Tên nhánh Git dùng deploy và đường dẫn tới file template deployment trong mã nguồn.
- Thông tin thư mục dự án nếu repository là monorepo.

#### Kiểm tra ban đầu

1. Mở Terminal tại thư mục gốc của dự án.
2. Kiểm tra phiên bản AWS CLI và SAM CLI:
```
aws --version
sam --version
```
3. Cấu hình AWS CLI nếu cần:
```
aws configure
```

#### Thông tin cần có

- `region`: ví dụ `ap-southeast-1`
- `subfolder path` của dự án backend nếu repo là monorepo, ví dụ `backend`
- `SSM Prefix`: tên lưu metadata như `Monorepo` hoặc nhấn Enter để dùng mặc định
- `CodeCommit repository name`: ví dụ `GameHub`
- `Git branch` dùng deploy: ví dụ `V1`
- `Template file path`: ví dụ `backend/codepipeline.yaml`
- `Stack name` cho Dev/Prod: ví dụ `GameHub-dev` và `GameHub-prod`
''',
    '5.3-S3-vpc/_index.vi.md': '''---
title : "Khởi tạo Pipeline SAM"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Bước 1: Khởi tạo Pipeline

1. Mở Terminal tại thư mục gốc của dự án.
2. Chạy lệnh:
```
sam pipeline init --bootstrap
```
3. Thực hiện các lựa chọn ban đầu:
- `Select a pipeline template`: chọn `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: chọn `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: chọn `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: nhập `y`

#### Bước 2: Thiết lập Stage Dev (Stage 1)

Khi hệ thống yêu cầu thông tin cho stage Dev, điền như sau:
- `Stage configuration name`: nhập `dev`
- `Select a credential source`: chọn `2` (default named profile)
- `Enter the region`: nhập mã vùng AWS, ví dụ `ap-southeast-1`
- Các ARN (IAM user, execution role, artifact bucket...): nhấn `Enter` để bỏ qua
- `Does your application contain any IMAGE type Lambda functions?`: nhập `n`

#### Bước 3: Xác nhận và tạo tài nguyên

1. Kiểm tra lại bảng tóm tắt (Summary) và nhấn `Enter` để xác nhận.
2. Khi được hỏi `Should we proceed with the creation? [y/N]`, nhập `y`.
3. Chờ cho đến khi hiển thị `Successfully created!`.

#### Ghi chú

- Các file cấu hình pipeline như `codepipeline.yaml` và `buildspec_deploy.yml` sẽ được tạo tại local.
- Bạn cần đẩy các file này lên Git sau khi cấu hình xong.
''',
    '5.6-Cleanup/_index.vi.md': '''---
title : "Triển khai Frontend với AWS Amplify"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Hướng dẫn Deploy Frontend bằng AWS Amplify

##### Bước 1: Khởi tạo ứng dụng trên AWS Amplify
1. Truy cập AWS Amplify Console.
2. Nhấn `Deploy an app`.
3. Chọn source provider: `GitHub`.
4. Nhấn `Next`.

##### Bước 2: Liên kết Repository và Branch
1. Chọn repository chứa mã nguồn dự án.
2. Chọn branch Git muốn deploy, ví dụ `V1`.
3. Nếu repository là monorepo, tích chọn `My app is a monorepo` và nhập `frontend` vào `Monorepo root directory`.

##### Bước 3: Cấu hình App Settings và file `amplify.yml`
1. Nhập `App name` cho ứng dụng frontend.
2. Điền lệnh build và tên thư mục output.
3. Chỉnh sửa `amplify.yml` với cấu hình Flutter sau:
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
            - echo "=== BUILDING FRONTEND IN ORIGINAL DIRECTORY ==="
            - ls -la
            - mkdir -p assets
            - |
              echo "=== AMPLIFY BUILD ENV CONFIGS ==="
              echo "COGNITO_USER_POOL_ID is $COGNITO_USER_POOL_ID"
              echo "API_GATEWAY_WS_URL is $API_GATEWAY_WS_URL"
              echo "API_GATEWAY_HTTP_URL is $API_GATEWAY_HTTP_URL"
              echo "================================="
              echo "COGNITO_REGION=$COGNITO_REGION" > assets/config.env
              echo "COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID" >> assets/config.env
              echo "COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID" >> assets/config.env
              echo "API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL" >> assets/config.env
              echo "LOCAL_API_URL=$LOCAL_API_URL" >> assets/config.env
              echo "USE_LOCAL_BACKEND=$USE_LOCAL_BACKEND" >> assets/config.env
              echo "APK_DOWNLOAD_URL=$APK_DOWNLOAD_URL" >> assets/config.env
            - flutter pub get
            - |
              flutter build web --release \
                --dart-define=COGNITO_REGION=$COGNITO_REGION \
                --dart-define=COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID \
                --dart-define=COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID \
                --dart-define=API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL \
                --dart-define=API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL
      artifacts:
        baseDirectory: build/web
        files:
          - "**/*"
          - 'assets/config.env'
      cache:
        paths: []
    appRoot: frontend
```

##### Bước 4: Cấu hình biến môi trường
1. Mở rộng phần `Advanced settings`.
2. Thêm biến môi trường phù hợp với `amplify.yml`.
- Ví dụ: `COGNITO_REGION`, `COGNITO_USER_POOL_ID`, `API_GATEWAY_HTTP_URL`, `API_GATEWAY_WS_URL`, `LOCAL_API_URL`, `USE_LOCAL_BACKEND`, `APK_DOWNLOAD_URL`.

##### Bước 5: Kiểm tra và triển khai
1. Nhấn `Next` để chuyển sang trang Review.
2. Kiểm tra lại toàn bộ cấu hình.
3. Nhấn `Save and deploy`.

AWS Amplify sẽ tự động kéo code, cài đặt Flutter và triển khai trang web frontend của bạn.
'''
}
for relative, content in files.items():
    path = base / relative
    path.write_text(content, encoding='utf-8')
    print('updated', path)
