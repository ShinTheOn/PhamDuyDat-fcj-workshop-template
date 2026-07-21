---
title : "Step 2: Connect the repository and branch"
date: 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.9.2. </b> "
---

#### Goal

In this step, you will select the correct repository and branch so Amplify can automatically monitor and deploy the frontend.

#### Instructions

![Image 1]({{ "/images/5-Workshop/5.9-Amplify-frontend-deploy/anh3.png" | relURL }})

1. `Select repository`: choose the repository that contains your frontend source code, for example `DTDuc04/DoAnMiniGame`.
2. `Select branch`: choose the Git branch that should trigger deployment, for example `V1`.
3. If your app uses a monorepo structure, enable `My app is a monorepo` and enter the frontend folder in `Monorepo root directory`, for example `frontend`.
4. If your repository is a single independent app, you can skip the monorepo option.

#### Note

Selecting the correct repository and branch is essential because Amplify uses them as the source for every new build.

