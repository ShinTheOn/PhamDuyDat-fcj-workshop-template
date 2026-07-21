---
title : "Bước 3: Cấu hình App Settings và file amplify.yml"
date: 2026-07-12
weight : 3
chapter : false
pre : " <b> 5.9.3. </b> "
---

#### Mục tiêu

Trong bước này, bạn sẽ đặt tên ứng dụng, cấu hình build settings và chèn nội dung cho file `amplify.yml` phù hợp cho Flutter Web.

#### Hướng dẫn

![alt text](image.png)

1. `App name`: nhập tên nhận diện cho frontend của bạn.
2. Điền lệnh build và thư mục output phù hợp với dự án.
3. Trong mục `Build settings`, nhấn `Edit YML file` rồi thay bằng cấu hình sau:

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
              echo "API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL" >> assets/config.env
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

#### Kết quả mong đợi

Sau khi cấu hình đúng, Amplify sẽ biết cách build frontend Flutter Web của bạn trong môi trường cloud.
