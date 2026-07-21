---
title : "Step 3: Configure app settings and the amplify.yml file"
date: 2026-07-12
weight : 3
chapter : false
pre : " <b> 5.9.3. </b> "
---

#### Goal

In this step, you will set the application name, configure the build settings, and provide the custom `amplify.yml` content for a Flutter Web project.

#### Instructions

![Image 1](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.9-Amplify-frontend-deploy/anh4.png)

1. `App name`: enter a recognizable name for your frontend application.
2. Fill in the build command and output directory according to your project structure.
3. In `Build settings`, click `Edit YML file` and replace it with the following configuration:

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

#### Expected result

Once configured correctly, Amplify will know how to build your Flutter Web frontend in the cloud.


