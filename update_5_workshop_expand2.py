import pathlib
root = pathlib.Path(r"c:\Baocao\fcj-workshop-template")
contents = {
    "content/5-Workshop/_index.vi.md": r"""---
title : "Workshop"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

#### Giới thiệu tổng quan

Workshop này giúp bạn xây dựng một quy trình triển khai dự án GameHub serverless từ đầu đến cuối. Nội dung tập trung vào:
- Khởi tạo pipeline với AWS SAM.
- Cấu hình các stage Dev/Prod.
- Kết nối GitHub với AWS CodePipeline.
- Thêm kiểm thử và giám sát.
- Triển khai frontend bằng AWS Amplify.

#### Lợi ích học được

- Hiểu rõ cách SAM tự động sinh cấu hình cho pipeline.
- Biết cách định nghĩa và quản lý stage trong CI/CD.
- Có thể triển khai frontend tĩnh từ một repo monorepo lên Amplify.
- Nắm cách theo dõi tình trạng ứng dụng thông qua CloudWatch.

#### Thực hành

Bạn sẽ làm việc với dự án GameHub gồm hai phần chính:
1. Backend serverless: Lambda + API Gateway + SAM.
2. Frontend tĩnh: Flutter web triển khai bằng Amplify.

#### Lưu ý

- Thay mọi ví dụ `GameHub` bằng tên dự án thực tế của bạn nếu cần.
- Cấu hình và file template có thể khác tùy theo cách bạn chia repo.
""",
    "content/5-Workshop/_index.md": r"""---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---


#### Workshop summary

This workshop demonstrates how to build an end-to-end CI/CD workflow for the GameHub serverless application.
It covers:
- bootstrapping a deployment pipeline with AWS SAM,
- configuring Dev and Prod stages,
- connecting GitHub to AWS CodePipeline,
- adding automated testing and monitoring,
- deploying the frontend with AWS Amplify.

#### Learning outcomes

- Understand how SAM generates pipeline configuration.
- Learn how to manage pipeline stage definitions.
- Deploy a Flutter web frontend in Amplify.
- Monitor serverless application health with CloudWatch.

#### Scope

You will work with a sample GameHub app consisting of:
1. backend serverless services managed by SAM,
2. a static frontend hosted by AWS Amplify.
""",
    "content/5-Workshop/5.1-Workshop-overview/_index.vi.md": r"""---
title : "Giới thiệu Workshop"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Mục tiêu Workshop

Trong workshop này bạn sẽ:
- xây dựng một pipeline CI/CD cho backend serverless,
- cấu hình Dev và Prod stage,
- kết nối GitHub với CodePipeline,
- triển khai frontend tĩnh bằng Amplify,
- thêm kiểm thử và giám sát.

#### Nội dung chi tiết

1. Khởi tạo pipeline bằng `sam pipeline init --bootstrap`.
2. Cấu hình thông tin repository, template và stage.
3. Thêm bước kiểm thử tự động trong pipeline.
4. Thiết lập giám sát CloudWatch cho Lambda và API Gateway.
5. Triển khai frontend Flutter web với Amplify.

#### Kiến trúc GameHub

GameHub được mô hình hóa dưới dạng serverless:
- Lambda function xử lý business logic.
- API Gateway cung cấp endpoint HTTP.
- AWS Cognito hoặc custom auth làm xác thực.
- AWS Amplify hosting phục vụ frontend tĩnh.

#### Lưu ý

- Các ví dụ sử dụng tên `GameHub`, nhưng bạn có thể thay bằng tên dự án của mình.
- Phần backend và frontend có thể được đặt trong cùng một repo hoặc tách riêng.
- Luôn kiểm tra profile và region trước khi chạy lệnh SAM.

Note (hình ảnh): Chèn ảnh mô hình kiến trúc hệ thống tại vị trí này để trực quan (hình: `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg`).
""",
    "content/5-Workshop/5.1-Workshop-overview/_index.md": r"""---
title : "Workshop Overview"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Workshop goals

In this workshop you will:
- build a CI/CD pipeline for a serverless backend,
- configure Dev and Prod stages,
- link GitHub with CodePipeline,
- deploy a static frontend with Amplify,
- add testing and monitoring.

#### What you will learn

1. How to initialize a pipeline with `sam pipeline init --bootstrap`.
2. How to configure repository, template path, and stage settings.
3. How to add automated test execution to the pipeline.
4. How to set up CloudWatch monitoring for Lambda and API Gateway.
5. How to deploy a Flutter web frontend to Amplify.

#### GameHub architecture

The GameHub sample is modeled as a serverless app with:
- AWS Lambda functions for application logic,
- Amazon API Gateway for HTTP APIs,
- AWS Cognito or custom auth for user login,
- AWS Amplify hosting for the frontend.

#### Notes

- The examples use the project name `GameHub`; replace it with your actual app name.
- Your backend and frontend may be stored in a monorepo or separate repositories.
- Always validate AWS profile and region before running SAM commands.

Note: Add an architecture diagram here to make the workflow clearer. Use `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg` as a placeholder.
""",
    "content/5-Workshop/5.2-Prerequiste/_index.vi.md": r"""---
title : "Chuẩn bị"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Yêu cầu trước khi bắt đầu

Trước khi thiết lập pipeline và triển khai frontend, bạn cần có:
- Tài khoản AWS với quyền tạo CloudFormation, S3, IAM, CodePipeline, CodeBuild, Amplify, CloudWatch.
- AWS CLI và AWS SAM CLI cài đặt và cấu hình.
- GitHub repository chứa mã nguồn GameHub.
- Thông tin branch deploy và cấu trúc thư mục trong repo.

#### Kiểm tra môi trường

1. Mở terminal ở thư mục gốc của dự án.
2. Kiểm tra phiên bản AWS CLI và SAM CLI:
```
aws --version
sam --version
```
3. Cấu hình profile AWS nếu cần:
```
aws configure --profile gamehub
```
4. Xác nhận profile hoạt động:\n```
aws sts get-caller-identity --profile gamehub
```

#### Thông tin cần chuẩn bị

- `Region`: ví dụ `ap-southeast-1`.
- `Repository subfolder`: ví dụ `backend` hoặc `frontend`.
- `SSM Prefix`: ví dụ `gamehub/`.
- `Git branch`: ví dụ `main` hoặc `V1`.
- `Template file path`: ví dụ `backend/template.yaml`.
- `Stack name`: ví dụ `GameHub-dev`, `GameHub-prod`, `GameHubPipeline`.

#### Hướng dẫn cài đặt nhanh

1. Cài SAM CLI nếu chưa có:
```powershell
pip install --user aws-sam-cli
sam --version
```
2. Cài AWS CLI nếu cần:
```powershell
pip install --user awscli
aws --version
```
3. Cấu hình profile workshop:
```powershell
aws configure --profile gamehub
```

#### Lời khuyên

- Nếu repo là monorepo, giữ `backend/` và `frontend/` tách biệt rõ ràng.
- Dùng branch riêng cho deploy và giữ stable branch để test.
- Nếu cần đa môi trường, tạo profile `gamehub-dev` và `gamehub-prod`.

Note (hình ảnh): Thêm ảnh chụp màn hình `aws configure` và `sam --version` tại `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.
""",
    "content/5-Workshop/5.2-Prerequiste/_index.md": r"""---
title : "Prerequisites"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Required preparations

Before you bootstrap the pipeline and deploy the frontend, make sure you have:
- an AWS account with permissions for CloudFormation, S3, IAM, CodePipeline, CodeBuild, Amplify, and CloudWatch,
- AWS CLI and AWS SAM CLI installed and configured,
- a GitHub repository containing the GameHub code,
- branch and repository structure details for deployment.

#### Environment checks

1. Open a terminal at the repo root.
2. Verify AWS CLI and SAM CLI versions:
```bash
aws --version
sam --version
```
3. Configure an AWS profile:
```bash
aws configure --profile gamehub
```
4. Confirm the profile works:
```bash
aws sts get-caller-identity --profile gamehub
```

#### Information to collect

- `Region`, e.g. `ap-southeast-1`.
- `Repository subfolder`, e.g. `backend` or `frontend`.
- `SSM Prefix`, e.g. `gamehub/`.
- `Git branch`, e.g. `main` or `V1`.
- `Template file path`, e.g. `backend/template.yaml`.
- `Stack names`, e.g. `GameHub-dev`, `GameHub-prod`, `GameHubPipeline`.

#### Quick setup

1. Install SAM CLI if needed:
```bash
pip install --user aws-sam-cli
sam --version
```
2. Install AWS CLI if needed:
```bash
pip install --user awscli
aws --version
```
3. Configure the workshop profile:
```bash
aws configure --profile gamehub
```

#### Tips

- In a monorepo, keep `backend/` and `frontend/` clearly separated.
- Use a dedicated deploy branch so changes are easier to manage.
- Create profile aliases such as `gamehub-dev` and `gamehub-prod` for multiple environments.

Note: Add a screenshot of `aws configure` and `sam --version` output in `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.
""",
    "content/5-Workshop/5.3-S3-vpc/_index.vi.md": r"""---
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

#### Bước 2: Thiết lập Stage Dev

Khi SAM hỏi thông tin cho stage Dev, điền như sau:
- `Stage configuration name`: `dev`
- `Select a credential source`: `2` (default named profile)
- `Enter the region`: `ap-southeast-1` hoặc region bạn dùng.
- `Enter your profile name`: nếu cần, nhập `gamehub`.
- Các ARN và artifact buckets: nhấn `Enter` để SAM tạo tự động.
- `Does your application contain any IMAGE type Lambda functions?`: `n`

#### Bước 3: Thiết lập Stage Prod

1. Chọn cấu hình cho stage Prod.
2. `Stage configuration name`: `prod`.
3. `Select a credential source`: `2` hoặc `1`.
4. `Enter the region`: cùng region hoặc region khác tùy chiến lược deploy.

#### Bước 4: Kiểm tra cấu trúc file

Trước khi commit, kiểm tra file pipeline:
```
ls pipeline
```
File cần tồn tại:
- `pipeline/samconfig.toml`
- `pipeline/codepipeline.yaml`
- `buildspec_deploy.yml`

#### Ghi chú chi tiết

- `sam pipeline init --bootstrap` sẽ bootstrap một S3 artifact bucket và các tài nguyên cần thiết khác.
- SAM cũng tạo một file `samconfig.toml` chứa cấu hình stage để bạn dễ sửa sau.
- Nếu bạn dùng repo mono, hãy kiểm tra kỹ `repository root path` và `template path`.

#### Commit và push

```bash
git add pipeline/*
git commit -m "chore(ci): add sam pipeline config for GameHub"
git push origin main
```

Note (hình ảnh): Chèn ảnh từng bước `sam pipeline init` và file list `ls pipeline/` vào `images/5-Workshop/5.3-S3-vpc/sam-init.svg`.
""",
    "content/5-Workshop/5.3-S3-vpc/_index.md": r"""---
title : "Initialize SAM Pipeline"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Step 1: Initialize the pipeline

1. Open a terminal in the project root.
2. Run:
```bash
sam pipeline init --bootstrap
```

3. Provide the following example answers:
- `Select a pipeline template`: `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: `y`

#### Step 2: Configure the Dev stage

When SAM prompts for Dev stage values, use:
- `Stage configuration name`: `dev`
- `Select a credential source`: `2` (default named profile)
- `Enter the region`: `ap-southeast-1` or your chosen region.
- If asked for profile, enter `gamehub`.
- For role ARNs and artifact bucket prompts, press `Enter` to let SAM create defaults.
- `Does your application contain any IMAGE type Lambda functions?`: `n`

#### Step 3: Configure the Prod stage

1. Configure the Prod stage if you use a two-stage pipeline.
2. `Stage configuration name`: `prod`.
3. `Select a credential source`: `2` or `1` depending on your profile.
4. `Enter the region`: same region or a different region as needed.

#### Step 4: Verify generated files

Before committing, check the pipeline folder:
```bash
ls pipeline
```
Required files include:
- `pipeline/samconfig.toml`
- `pipeline/codepipeline.yaml`
- `buildspec_deploy.yml`

#### Notes

- `sam pipeline init --bootstrap` bootstraps an S3 artifact bucket and related resources.
- SAM also creates `samconfig.toml` for stage configuration and runtime settings.
- In a monorepo, verify the repository root path and template path carefully.

#### Commit and push

```bash
git add pipeline/*
git commit -m "chore(ci): add sam pipeline config for GameHub"
git push origin main
```

Note: Add a placeholder image for the init flow in `images/5-Workshop/5.3-S3-vpc/sam-init.svg`.
""",
    "content/5-Workshop/5.4-S3-onprem/_index.vi.md": r"""---
title : "Cấu hình Repository và Stage"
date : 2024-01-01 
weight : 4 
chapter : false
pre : " <b> 5.4. </b> "
---

#### Mục tiêu

Phần này giúp bạn cấu hình repository và stage đúng cách để pipeline SAM hoạt động chính xác.

#### Những gì cần kiểm tra

- `Repository subfolder`: đường dẫn tới backend, ví dụ `backend`.
- `Template path`: đường dẫn tới SAM template, ví dụ `backend/template.yaml`.
- `SSM Prefix`: ví dụ `gamehub/`.
- `Stack name` Dev/Prod: `GameHub-dev`, `GameHub-prod`.
- `Git branch`: `main`, `V1` hoặc branch deploy thực tế.

#### Hướng dẫn cấu hình

1. Khi SAM yêu cầu repository root path, nhập `backend` nếu backend nằm trong thư mục backend.
2. Nếu repo là monorepo, chỉ rõ thư mục backend cho pipeline để tránh trỏ nhầm frontend.
3. Đảm bảo `template path` chỉ tới file SAM/CloudFormation đúng.

#### Quản lý stage

- Dev stage: dùng để kiểm thử và deploy nhanh.
- Prod stage: dùng để triển khai phiên bản production sau khi test.
- Giữ tên stage đồng nhất với tên stack để dễ quản lý.

#### Kiểm tra cấu hình

- Mở `pipeline/samconfig.toml` và xác nhận `stage` và `region`.
- Mở `pipeline/codepipeline.yaml` để kiểm tra nếu template được cấu hình đúng.

#### Lời khuyên commit

```bash
git add .
git commit -m "ci: add sam pipeline configuration for GameHub"
git push origin main
```

Note (hình ảnh): Thêm ảnh `pipeline file list` và `samconfig preview` vào `images/5-Workshop/5.4-S3-onprem/pipeline-files.svg`.
""",
    "content/5-Workshop/5.4-S3-onprem/_index.md": r"""---
title : "Configure Repository and Stage"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Goal

This section helps you configure the repository path and pipeline stage settings so the SAM-generated pipeline works correctly.

#### What to verify

- `Repository subfolder`: path to the backend, e.g. `backend`.
- `Template path`: path to the SAM template, e.g. `backend/template.yaml`.
- `SSM Prefix`: e.g. `gamehub/`.
- `Stack names`: `GameHub-dev`, `GameHub-prod`.
- `Git branch`: `main`, `V1`, or another deployment branch.

#### Configuration steps

1. When SAM asks for repository root path, enter `backend` if the backend is in that folder.
2. In a monorepo, point the pipeline to the backend folder only to avoid including frontend code.
3. Make sure the `template path` points to the correct SAM or CloudFormation file.

#### Stage management

- Dev stage is for testing and fast deploys.
- Prod stage is for stable production deployments.
- Keep stage names aligned with stack names for easy tracking.

#### Verify settings

- Inspect `pipeline/samconfig.toml` for stage names and region.
- Inspect `pipeline/codepipeline.yaml` to confirm the template reference.

#### Commit suggestion

```bash
git add .
git commit -m "ci: add sam pipeline configuration for GameHub"
git push origin main
```

Note: Add a placeholder image for the pipeline file list and samconfig preview in `images/5-Workshop/5.4-S3-onprem/pipeline-files.svg`.
""",
    "content/5-Workshop/5.5a-Testing/_index.vi.md": r"""---
title : "Kiểm thử và Pipeline Testing"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Mục tiêu

Thêm bước kiểm thử tự động vào pipeline để phát hiện lỗi trước khi triển khai lên môi trường tiếp theo.

#### Nội dung nên có

- Tạo stage `Test` trong pipeline.
- Dùng CodeBuild để chạy unit test và integration test.
- Thực hiện test trên backend và frontend nếu có.
- Dừng pipeline khi test fail.

#### Cấu hình buildspec

Đặt các lệnh test trong `buildspec_deploy.yml`:
```yaml
version: 0.2
phases:
  install:
    commands:
      - pip install -r requirements.txt
  build:
    commands:
      - pytest tests/
artifacts:
  files:
    - '**/*'
```

#### Nếu dùng Node.js

Thêm các lệnh tương ứng:
```yaml
phases:
  install:
    commands:
      - npm ci
  build:
    commands:
      - npm test
```

#### Lời khuyên

- Chia test thành unit test và integration test.
- Nếu pipeline quá chậm, chỉ chạy các test quan trọng nhất.
- Xem log CodeBuild để tìm nguyên nhân thất bại.
- Đặt tên rõ ràng cho stage và build project.

#### Kết quả kiểm thử

- Nếu test success, pipeline tiếp tục sang bước deploy.
- Nếu test fail, pipeline dừng và ghi log lỗi rõ ràng.

Note (hình ảnh): Thêm ảnh `test-run.png` vào `images/5-Workshop/5.5a-Testing/` để minh họa output test.
""",
    "content/5-Workshop/5.5a-Testing/_index.md": r"""---
title : "Testing and Pipeline Validation"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Goal

Add an automated test stage to the pipeline so failures are caught before deployment.

#### What this section covers

- Adding a `Test` stage in CodePipeline.
- Using AWS CodeBuild to run unit and integration tests.
- Stopping deployment on test failures.
- Verifying backend and frontend test results.

#### Example buildspec

Place your test commands in `buildspec_deploy.yml`:
```yaml
version: 0.2
phases:
  install:
    commands:
      - pip install -r requirements.txt
  build:
    commands:
      - pytest tests/
artifacts:
  files:
    - '**/*'
```

#### Node.js example

If your frontend or tests use Node.js:
```yaml
phases:
  install:
    commands:
      - npm ci
  build:
    commands:
      - npm test
```

#### Best practices

- Separate unit tests and integration tests.
- Run only the most important coverage in early pipeline stages.
- Use CodeBuild logs to diagnose failures.
- Name stages and projects clearly.

#### Expected outcome

- test success continues the pipeline to deploy,
- test failure stops the pipeline and surfaces the failure cause.

Note: Add a placeholder image for the test run in `images/5-Workshop/5.5a-Testing/test-run.svg`.
""",
    "content/5-Workshop/5.5b-Monitoring/_index.vi.md": r"""---
title : "Giám sát & Logging"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Mục tiêu

Thiết lập giám sát để quan sát trạng thái hoạt động của GameHub sau khi deploy.\n
#### Nội dung chính

- Bật CloudWatch Logs cho Lambda và API Gateway.
- Tạo metric filter cho lỗi và latency cao.
- Cấu hình alarm khi có sự cố.
- Gửi thông báo qua SNS hoặc email.

#### Các bước thực hiện

1. Mở CloudWatch Console.\n2. Vào Logs > Log groups.\n3. Chọn log group của Lambda hoặc API Gateway.\n4. Tạo metric filter cho lỗi, ví dụ `ERROR` hoặc `5xx` status.\n5. Tạo alarm dựa trên metric filter.\n
#### Gợi ý cấu hình

- Alarm Lambda error rate > 1% trong 5 phút.\n- Alarm API Gateway `5xx` rate > 5% trong 5 phút.\n- Alarm when any deployment stage fails.\n
#### Kết nối thông báo

- Dùng SNS topic để gửi email hoặc Slack.\n- Đặt tên rõ ràng cho alarm, ví dụ `GameHub-Lambda-Error-Alarm`.\n- Kiểm tra dashboard CloudWatch định kỳ.\n
Note (hình ảnh): Thêm ảnh `cloudwatch-alarms.png` vào `images/5-Workshop/5.5b-Monitoring/`.
""",
    "content/5-Workshop/5.5b-Monitoring/_index.md": r"""---
title : "Monitoring & Logging"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Goal

Set up monitoring so you can observe GameHub application health after deployment.

#### Key coverage

- Enable CloudWatch Logs for Lambda and API Gateway.
- Create metric filters for errors and latency.
- Configure alarms for incidents.
- Send notifications using SNS or email.

#### Steps to implement

1. Open CloudWatch Console.
2. Go to Logs > Log groups.
3. Select the Lambda or API Gateway log group.
4. Create a metric filter for error patterns such as `ERROR` or HTTP `5xx`.\n5. Create an alarm based on the metric filter.

#### Recommended alerts

- Lambda error rate > 1% over 5 minutes.
- API Gateway `5xx` rate > 5% over 5 minutes.
- Deployment failure in CodePipeline.

#### Notifications

- Use an SNS topic to send email or Slack alerts.
- Name alarms clearly, e.g. `GameHub-Lambda-Error-Alarm`.
- Review the CloudWatch dashboard regularly.

Note: Add a placeholder image for CloudWatch alarms in `images/5-Workshop/5.5b-Monitoring/cloudwatch-alarms.svg`.
""",
    "content/5-Workshop/5.5-Policy/_index.vi.md": r"""---
title : "Tạo CodePipeline trên AWS Console"
date : 2024-01-01
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Mục tiêu

Thiết lập CodePipeline trên AWS Console để kết nối GitHub, build và deploy application.

#### Tạo kết nối GitHub

1. Mở AWS Console → `Developer Tools` → `Connections`.
2. Nhấn `Create connection`.
3. Chọn `GitHub` và xác thực tài khoản.\n4. Chọn repository của GameHub.\n5. Đảm bảo kết nối hiển thị `Available`.

#### Tạo pipeline mới

1. Mở CodePipeline Console.\n2. Chọn `Create pipeline`.\n3. Chọn `Use a blueprint` hoặc `Start from scratch`.\n4. Source provider: `GitHub (version 2)`.\n5. Chọn connection, repository, branch.\n6. Thêm stage Build với CodeBuild dùng `buildspec_deploy.yml`.\n7. Thêm stage Deploy với CloudFormation trỏ tới `pipeline/codepipeline.yaml`.

#### Lưu ý khi dùng SAM

- Nếu bạn đã chạy `sam pipeline init`, hãy tái sử dụng `codepipeline.yaml` do SAM tạo.\n- Lưu ARN connection để dùng khi tự động hoá.\n- Kiểm tra đường dẫn template và branch có khớp với repository.

Note (hình ảnh): Chụp màn hình `Create pipeline` và `Connection ARN` vào `images/5-Workshop/5.5-Policy/`.
""",
    "content/5-Workshop/5.5-Policy/_index.md": r"""---
title : "Create CodePipeline in AWS Console"
date : 2024-01-01
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Goal

Build a CodePipeline in the AWS Console that connects GitHub to your deployment workflow.

#### Create the GitHub connection

1. Open AWS Console → Developer Tools → Connections.
2. Click `Create connection`.
3. Select `GitHub` and authorize the repository.\n4. Choose the GameHub repository.\n5. Verify the status is `Available`.

#### Create the pipeline

1. Open CodePipeline Console.\n2. Click `Create pipeline`.\n3. Choose `Use a blueprint` or `Start from scratch`.\n4. Select `GitHub (version 2)` as the source provider.\n5. Select the connection, repository, and branch.\n6. Add a build stage with CodeBuild using `buildspec_deploy.yml` from your repo.\n7. Add a deploy stage with CloudFormation pointing to `pipeline/codepipeline.yaml`.

#### Notes

- If you initialized the pipeline with `sam pipeline init`, reuse the generated `codepipeline.yaml` file.\n- Save the connection ARN for later automation.\n- Confirm that the template path and branch match your repository structure.

Note: Add UI screenshots for the pipeline setup in `images/5-Workshop/5.5-Policy/create-pipeline.svg` and `images/5-Workshop/5.5-Policy/connection-arn.svg`.
""",
    "content/5-Workshop/5.6-Cleanup/_index.vi.md": r"""---
title : "Triển khai Frontend với AWS Amplify"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Mục tiêu

Triển khai frontend tĩnh của GameHub bằng AWS Amplify và thiết lập cấu hình build phù hợp.

#### Bước 1: Khởi tạo ứng dụng trên Amplify

1. Vào Amplify Console.\n2. Nhấn `Deploy an app`.\n3. Chọn `GitHub` và xác thực repository.\n4. Chọn branch deploy, ví dụ `V1`.

#### Bước 2: Cấu hình repo monorepo

1. Nếu repo là monorepo, bật `My app is a monorepo`.\n2. Nhập `frontend` vào `Monorepo root directory`.\n
#### Bước 3: Cấu hình build cho Flutter web

Sử dụng file `amplify.yml` sau để build Flutter web:\n```yaml\nversion: 1\napplications:\n  - frontend:\n      phases:\n        build:\n          commands:\n            - ORIGINAL_DIR=$(pwd)\n            - which xz || sudo yum install -y xz\n            - cd /tmp\n            - wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.0-stable.tar.xz\n            - tar xf flutter_linux_3.22.0-stable.tar.xz\n            - export PATH="$PATH:/tmp/flutter/bin"\n            - cd $ORIGINAL_DIR\n            - flutter doctor\n            - flutter config --enable-web\n            - flutter channel stable\n            - flutter upgrade\n            - flutter pub get\n            - flutter build web --release --dart-define=COGNITO_REGION=$COGNITO_REGION --dart-define=COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID --dart-define=COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID --dart-define=API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL --dart-define=API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL\n      artifacts:\n        baseDirectory: build/web\n        files:\n          - "**/*"\n      cache:\n        paths: []\n    appRoot: frontend\n```

#### Bước 4: Biến môi trường

Thêm các biến sau trong Amplify Console:\n- `COGNITO_REGION`\n- `COGNITO_USER_POOL_ID`\n- `COGNITO_CLIENT_ID`\n- `API_GATEWAY_HTTP_URL`\n- `API_GATEWAY_WS_URL`\n- `LOCAL_API_URL`\n- `USE_LOCAL_BACKEND`\n- `APK_DOWNLOAD_URL`

#### Bước 5: Xem lại và deploy

1. Kiểm tra cấu hình app và branch.\n2. Nhấn `Save and deploy`.\n3. Amplify sẽ tự động build và host frontend.

Note (hình ảnh): Thêm ảnh `amplify-setup.png` vào `images/5-Workshop/5.6-Cleanup/amplify-setup.svg`.
""",
    "content/5-Workshop/5.6-Cleanup/_index.md": r"""---
title : "Deploy Frontend with AWS Amplify"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Goal

Deploy the GameHub frontend and configure build settings in AWS Amplify.

#### Step 1: Initialize the Amplify app

1. Open Amplify Console.\n2. Click `Deploy an app`.\n3. Select `GitHub` and authorize the repository.\n4. Choose the deployment branch, e.g. `V1`.

#### Step 2: Configure a monorepo

1. If your repository is a monorepo, enable `My app is a monorepo`.\n2. Set `Monorepo root directory` to `frontend`.

#### Step 3: Build configuration for Flutter web

Use the following `amplify.yml` configuration:\n```yaml\nversion: 1\napplications:\n  - frontend:\n      phases:\n        build:\n          commands:\n            - ORIGINAL_DIR=$(pwd)\n            - which xz || sudo yum install -y xz\n            - cd /tmp\n            - wget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.0-stable.tar.xz\n            - tar xf flutter_linux_3.22.0-stable.tar.xz\n            - export PATH="$PATH:/tmp/flutter/bin"\n            - cd $ORIGINAL_DIR\n            - flutter doctor\n            - flutter config --enable-web\n            - flutter channel stable\n            - flutter upgrade\n            - flutter pub get\n            - flutter build web --release --dart-define=COGNITO_REGION=$COGNITO_REGION --dart-define=COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID --dart-define=COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID --dart-define=API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL --dart-define=API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL\n      artifacts:\n        baseDirectory: build/web\n        files:\n          - "**/*"\n      cache:\n        paths: []\n    appRoot: frontend\n```

#### Step 4: Environment variables\n
Add the following Amplify environment variables:\n- `COGNITO_REGION`\n- `COGNITO_USER_POOL_ID`\n- `COGNITO_CLIENT_ID`\n- `API_GATEWAY_HTTP_URL`\n- `API_GATEWAY_WS_URL`\n- `LOCAL_API_URL`\n- `USE_LOCAL_BACKEND`\n- `APK_DOWNLOAD_URL`

#### Step 5: Review and deploy\n
1. Review the app settings.\n2. Click `Save and deploy`.\n3. Amplify will build and host the frontend.

Note: Add a placeholder image for Amplify setup in `images/5-Workshop/5.6-Cleanup/amplify-setup.svg`.
""",
}
for rel, text in contents.items():
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')
print('Wrote expanded workshop files')

