---
title : "Step 4: Configure advanced settings and environment variables"
date: 2026-07-12
weight : 4
chapter : false
pre : " <b> 5.9.4. </b> "
---

#### Goal

In this step, you will open the advanced options in Amplify and add the environment variables required for the frontend build.

#### Instructions

![Image 1](/PhamDuyDat-fcj-workshop-template/images/5-Workshop/5.9-Amplify-frontend-deploy/anh5.png)

1. Scroll down and expand `Advanced settings`.
2. Options such as `Build instance type`, `Build image`, and `Cache key` are optional; you can keep the defaults or adjust them if needed.
3. In `Environment variables`, click `Add new` to add the required values.
4. Make sure variables such as `COGNITO_REGION`, `COGNITO_USER_POOL_ID`, and `API_GATEWAY_HTTP_URL` are added correctly.

#### Note

These environment variables must match the values referenced by the `amplify.yml` file during the build process.


