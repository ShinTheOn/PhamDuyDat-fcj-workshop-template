import pathlib
root = pathlib.Path(r"c:\Baocao\fcj-workshop-template")
files = {
    "content/5-Workshop/_index.vi.md": """---
title : "Workshop"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

#### Giới thiệu tổng quan

Workshop này giúp bạn xây dựng một quy trình triển khai dự án GameHub serverless từ đầu đến cuối. Nội dung tập trung vào:
- Khởi tạo pipeline với AWS SAM và AWS CodePipeline.
- Cấu hình các stage Dev/Prod và thông tin repository.
- Thêm kiểm thử tự động và giám sát.
- Triển khai frontend với AWS Amplify.

#### Lợi ích học được

- Hiểu cách SAM sinh cấu hình pipeline và stage.
- Biết cách thiết lập môi trường deploy cho Dev và Prod.
- Kết nối GitHub với AWS và cấu hình pipeline thủ công.
- Triển khai toàn vẹn backend + frontend cho GameHub.

#### Phương pháp thực hành

Bạn sẽ học bằng cách làm theo từng bước, từ cài đặt công cụ đến deploy hoàn chỉnh:
1. Chuẩn bị quyền và công cụ AWS.
2. Khởi tạo pipeline SAM.
3. Cấu hình repository, stage và template path.
4. Thêm bước kiểm thử và giám sát pipeline.
5. Thiết lập CodePipeline trên AWS Console.
6. Triển khai frontend bằng Amplify.

#### Lưu ý

- Các ví dụ dùng tên dự án `GameHub`; hãy thay thế bằng tên tương ứng nếu cần.
- Nếu mã nguồn nằm trong monorepo, hãy chỉ rõ thư mục `backend/` và `frontend/` chính xác.
- Luôn kiểm tra profile AWS và region trước khi chạy lệnh SAM.
""",
    "content/5-Workshop/_index.md": """---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---


#### Workshop summary

This workshop teaches you how to build an end-to-end CI/CD workflow for the GameHub serverless application. It covers:
- bootstrapping a deployment pipeline with AWS SAM,
- configuring Dev and Prod stages,
- connecting GitHub to AWS CodePipeline,
- adding automated testing and monitoring,
- deploying the frontend with AWS Amplify.

#### Learning outcomes

- Understand how SAM generates pipeline configurations.
- Learn how to manage stage definitions and environment settings.
- Deploy a Flutter web frontend in Amplify.
- Monitor serverless app health with CloudWatch.

#### Scope

You will work with a sample GameHub app composed of:
1. backend serverless services managed by SAM,
2. a static frontend hosted by AWS Amplify.
""",
    "content/5-Workshop/5.1-Workshop-overview/_index.vi.md": """---
title : "Giới thiệu Workshop"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Mục tiêu Workshop

Trong phần này, bạn sẽ biết cách:
- Khởi tạo pipeline CI/CD cho backend serverless bằng AWS SAM.
- Cấu hình Dev và Prod stage.
- Kết nối GitHub với CodePipeline.
- Triển khai frontend với AWS Amplify.
- Thêm kiểm thử và giám sát trong pipeline.

#### Nội dung chính

1. Khởi tạo pipeline bằng `sam pipeline init --bootstrap`.
2. Cấu hình repository, template path và stage.
3. Thêm stage kiểm thử tự động.
4. Thiết lập giám sát CloudWatch cho Lambda và API Gateway.
5. Triển khai frontend Flutter web với Amplify.

#### Kiến trúc GameHub

GameHub được xây dựng như một ứng dụng serverless:
- Lambda function xử lý logic,
- API Gateway cung cấp endpoint HTTP,
- AWS Cognito hoặc custom auth quản lý đăng nhập,
- AWS Amplify hosting phục vụ frontend tĩnh.

#### Lưu ý

- Tên `GameHub` là ví dụ; hãy thay bằng tên dự án của bạn.
- Nếu backend và frontend cùng trong một repository, xác định rõ thư mục riêng.
- Kiểm tra profile và region AWS trước khi chạy lệnh SAM.

Note (hình ảnh): Chèn ảnh mô hình kiến trúc hệ thống tại vị trí này để trực quan. Thư mục placeholder: `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg`.
""",
    "content/5-Workshop/5.1-Workshop-overview/_index.md": """---
title : "Workshop Overview"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Workshop goals

In this section, you will learn how to:
- initialize a CI/CD pipeline for a serverless backend with AWS SAM,
- configure Dev and Prod stages,
- connect GitHub with CodePipeline,
- deploy a static frontend via AWS Amplify,
- add testing and monitoring to the deployment flow.

#### Key content

1. Initialize the pipeline using `sam pipeline init --bootstrap`.
2. Configure repository paths, template files, and stage settings.
3. Add an automated test stage.
4. Set up CloudWatch monitoring for Lambda and API Gateway.
5. Deploy a Flutter web frontend in Amplify.

#### GameHub architecture

The GameHub sample is a serverless app with:
- AWS Lambda functions for business logic,
- Amazon API Gateway for HTTP endpoints,
- AWS Cognito or custom authentication for users,
- AWS Amplify hosting for the frontend.

#### Notes

- The project name `GameHub` is an example; replace it with your own project name.
- If your backend and frontend are in one repo, use clear folder separation.
- Verify your AWS profile and region before running SAM commands.

Note: Add an architecture diagram here to make the workflow clearer. Placeholder: `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg`.
""",
    "content/5-Workshop/5.2-Prerequiste/_index.vi.md": """---
title : "Chuẩn bị"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Yêu cầu trước khi bắt đầu

Trước khi bắt đầu pipeline và deployment, hãy đảm bảo bạn có:
- Tài khoản AWS với quyền CloudFormation, S3, IAM, CodePipeline, CodeBuild, Amplify và CloudWatch.
- AWS CLI và AWS SAM CLI đã cài đặt và cấu hình.
- Repository trên GitHub chứa mã nguồn GameHub.
- Quy ước branch và cấu trúc thư mục rõ ràng.

#### Kiểm tra môi trường

1. Mở terminal tại thư mục gốc.
2. Kiểm tra phiên bản AWS CLI và SAM CLI:
```
aws --version
sam --version
```
3. Cấu hình profile AWS:
```
aws configure --profile gamehub
```
4. Xác nhận profile hoạt động:
```
aws sts get-caller-identity --profile gamehub
```

#### Thông tin cần chuẩn bị

- `Region`: ví dụ `ap-southeast-1`.
- `Repository subfolder`: ví dụ `backend` hoặc `frontend`.
- `SSM Prefix`: ví dụ `gamehub/`.
- `Git branch`: ví dụ `main` hoặc `V1`.
- `Template path`: ví dụ `backend/template.yaml`.
- `Stack names`: `GameHub-dev`, `GameHub-prod`, `GameHubPipeline`.

#### Hướng dẫn cài đặt nhanh

1. Cài SAM CLI nếu cần:
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

#### Gợi ý

- Nếu repository là monorepo, giữ `backend/` và `frontend/` tách biệt.
- Dùng branch deploy riêng để kiểm soát thay đổi.
- Tạo profile `gamehub-dev` và `gamehub-prod` nếu bạn triển khai nhiều môi trường.

Note (hình ảnh): Thêm ảnh `aws configure` và `sam --version` tại `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.
""",
    "content/5-Workshop/5.2-Prerequiste/_index.md": """---
title : "Prerequisites"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Required preparations

Before starting the pipeline and deployment, ensure you have:
- an AWS account with permissions for CloudFormation, S3, IAM, CodePipeline, CodeBuild, Amplify, and CloudWatch,
- AWS CLI and AWS SAM CLI installed and configured,
- a GitHub repository containing your GameHub source code,
- a clear branch strategy and repository layout.

#### Environment checks

1. Open a terminal in the repo root.
2. Verify AWS CLI and SAM CLI versions:
```bash
aws --version
sam --version
```
3. Configure your AWS profile:
```bash
aws configure --profile gamehub
```
4. Verify the profile works:
```bash
aws sts get-caller-identity --profile gamehub
```

#### Information to prepare

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
- Use a dedicated deploy branch to manage change flows.
- Create profile aliases like `gamehub-dev` and `gamehub-prod` for multiple environments.

Note: Add a screenshot of `aws configure` and `sam --version` output in `images/5-Workshop/5.2-Prerequiste/aws-config.svg`.
""",
    "content/5-Workshop/5.3-S3-vpc/_index.vi.md": """---
title : "Khởi tạo Pipeline SAM"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Bước 1: Khởi tạo Pipeline

1. Mở Terminal tại thư mục gốc dự án.
2. Chạy lệnh:
```
sam pipeline init --bootstrap
```

3. Trả lời các câu hỏi sau:
- `Select a pipeline template`: `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: `y`

#### Bước 2: Thiết lập dev stage

Khi được hỏi thông tin cho stage Dev:
- `Stage configuration name`: `dev`
- `Select a credential source`: `2` (default named profile)
- `Enter the region`: `ap-southeast-1` hoặc region của bạn
- Nếu yêu cầu profile, nhập `gamehub`
- Khi hỏi ARN/roles/artifact buckets, nhấn `Enter` để SAM tạo tự động
- `Does your application contain any IMAGE type Lambda functions?`: `n`

#### Bước 3: Thiết lập prod stage

1. Chọn cấu hình cho stage Prod.
2. `Stage configuration name`: `prod`.
3. `Select a credential source`: `2` hoặc `1`.
4. `Enter the region`: cùng region hoặc region khác tùy chiến lược vận hành.

#### Bước 4: Kiểm tra file pipeline

Chạy:
```
ls pipeline
```
Các file cần có:
- `pipeline/samconfig.toml`
- `pipeline/codepipeline.yaml`
- `buildspec_deploy.yml`

#### Ghi chú

- `sam pipeline init --bootstrap` tạo các tài nguyên bootstrap như S3 artifact bucket.
- `samconfig.toml` chứa cấu hình stage và profile.
- Bạn có thể chỉnh sửa `samconfig.toml` sau khi init để tùy chỉnh stage.

#### Commit và push

```bash
git add pipeline/*
git commit -m "chore(ci): add sam pipeline config for GameHub"
git push origin main
```

Note (hình ảnh): Thêm ảnh `sam pipeline init` và `ls pipeline/` trong `images/5-Workshop/5.3-S3-vpc/sam-init.svg`.
""",
    "content/5-Workshop/5.3-S3-vpc/_index.md": """---
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

3. Answer the prompts as follows:
- `Select a pipeline template`: `1` (AWS Quick Start Pipeline Templates)
- `Select CI/CD system`: `5` (AWS CodePipeline)
- `Which pipeline template would you like to use?`: `2` (Two-stage pipeline)
- `Do you want to go through stage setup process now?`: `y`

#### Step 2: Configure the Dev stage

When prompted for the Dev stage:
- `Stage configuration name`: `dev`
- `Select a credential source`: `2` (default named profile)
- `Enter the region`: `ap-southeast-1` or your chosen region
- If prompted for profile, enter `gamehub`
- For role and artifact bucket prompts, press `Enter` to let SAM create defaults
- `Does your application contain any IMAGE type Lambda functions?`: `n`

#### Step 3: Configure the Prod stage

1. Configure the Prod stage if you use a two-stage pipeline.
2. `Stage configuration name`: `prod`.
3. `Select a credential source`: `2` or `1`.
4. `Enter the region`: same region or a different region depending on your deployment strategy.

#### Step 4: Verify the pipeline files

Run:
```bash
ls pipeline
```
The expected files include:
- `pipeline/samconfig.toml`
- `pipeline/codepipeline.yaml`
- `buildspec_deploy.yml`

#### Notes

- `sam pipeline init --bootstrap` bootstraps an S3 artifact bucket and related resources.
- `samconfig.toml` contains stage and profile settings.
- You can edit `samconfig.toml` after initialization to customize stage parameters.

#### Commit and push

```bash
git add pipeline/*
git commit -m "chore(ci): add sam pipeline config for GameHub"
git push origin main
```

Note: Add a placeholder image for the init flow in `images/5-Workshop/5.3-S3-vpc/sam-init.svg`.
""",
    "content/5-Workshop/5.4-S3-onprem/_index.vi.md": """---
title : "Cấu hình Repository và Stage"
date : 2024-01-01 
weight : 4 
chapter : false
pre : " <b> 5.4. </b> "
---

#### Mục tiêu

Phần này giúp bạn cấu hình chính xác repository và stage để pipeline SAM hoạt động ổn định.

#### Những thông tin quan trọng

- `Repository subfolder`: thư mục chứa backend, ví dụ `backend`.
- `Template path`: đường dẫn tới file SAM/CloudFormation, ví dụ `backend/template.yaml`.
- `SSM Prefix`: ví dụ `gamehub/`.
- `Stack name` Dev/Prod: `GameHub-dev`, `GameHub-prod`.
- `Git branch`: `main`, `V1`, hoặc nhánh deploy.

#### Chi tiết cấu hình

1. Khi SAM hỏi `Repository root path`, nhập `backend` nếu backend ở đó.
2. Nếu repository là monorepo, đảm bảo chỉ trỏ pipeline tới thư mục backend.
3. Kiểm tra `template path` trỏ đúng file SAM template.

#### Quản lý stage

- Dev stage để thử nghiệm nhanh và deploy tự động.
- Prod stage để deploy khi đã kiểm thử ổn định.
- Giữ tên stage và stack nhất quán cho dễ theo dõi.

#### Kiểm tra lại

- Mở `pipeline/samconfig.toml` và kiểm tra `stage`/`region`.
- Mở `pipeline/codepipeline.yaml` để xác nhận template path.
- Nếu cần, điều chỉnh `samconfig.toml` rồi chạy lại pipeline.

#### Gợi ý commit

```bash
git add .
git commit -m "ci: add sam pipeline configuration for GameHub"
git push origin main
```

Note (hình ảnh): Thêm ảnh `pipeline file list` và `samconfig preview` vào `images/5-Workshop/5.4-S3-onprem/pipeline-files.svg`.
""",
    "content/5-Workshop/5.4-S3-onprem/_index.md": """---
title : "Configure Repository and Stage"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Goal

This section helps you configure the repository and stage settings exactly so the SAM pipeline runs correctly.

#### Important details

- `Repository subfolder`: the backend folder, e.g. `backend`.
- `Template path`: the SAM or CloudFormation template path, e.g. `backend/template.yaml`.
- `SSM Prefix`: e.g. `gamehub/`.
- `Stack names`: `GameHub-dev`, `GameHub-prod`.
- `Git branch`: `main`, `V1`, or your deployment branch.

#### Configuration steps

1. When SAM asks for `Repository root path`, enter `backend` if your backend is stored there.
2. In a monorepo, point the pipeline to the backend folder only.
3. Ensure the `template path` points to the correct SAM template file.

#### Stage management

- Dev stage is for testing and fast deployments.
- Prod stage is for stable production deployments.
- Keep stage and stack names aligned for easier tracking.

#### Verify settings

- Review `pipeline/samconfig.toml` for stage and region values.
- Review `pipeline/codepipeline.yaml` to confirm the template reference.
- Adjust `samconfig.toml` if you need to change stage names or regions.

#### Commit recommendation

```bash
git add .
git commit -m "ci: add sam pipeline configuration for GameHub"
git push origin main
```

Note: Add placeholder images for the pipeline file list and samconfig preview in `images/5-Workshop/5.4-S3-onprem/pipeline-files.svg`.
""",
    "content/5-Workshop/5.5-Policy/_index.vi.md": """---
title : "Tạo CodePipeline trên AWS Console"
date : 2024-01-01
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Mục tiêu

Thiết lập CodePipeline trên AWS Console để kết nối GitHub, build và deploy ứng dụng GameHub.

#### Tạo kết nối GitHub

1. Mở AWS Console → `Developer Tools` → `Connections`.
2. Nhấn `Create connection`.
3. Chọn `GitHub` và cấp quyền truy cập.
4. Chọn repository của GameHub.
5. Đảm bảo trạng thái kết nối là `Available`.

#### Tạo pipeline trên Console

1. Mở CodePipeline Console.
2. Chọn `Create pipeline`.
3. Chọn `Use a blueprint` hoặc `Start from scratch`.
4. Source provider: `GitHub (version 2)`.
5. Chọn connection, repository và branch.
6. Thêm stage Build với CodeBuild dùng `buildspec_deploy.yml`.
7. Thêm stage Deploy với CloudFormation trỏ tới `pipeline/codepipeline.yaml`.

#### Lưu ý khi dùng SAM

- Nếu bạn đã chạy `sam pipeline init`, tái sử dụng `codepipeline.yaml` do SAM tạo.
- Lưu ARN connection để sử dụng trong tự động hoá.
- Kiểm tra template path và branch có khớp với repo.

#### Kết nối với các phần khác

- Trước khi tạo pipeline, hãy hoàn thành cấu hình stage trong SAM.
- Thêm kiểm thử và giám sát để pipeline hoạt động toàn diện.

Note (hình ảnh): Chụp màn hình `Create pipeline` và `Connection ARN` vào `images/5-Workshop/5.5-Policy/`.
""",
    "content/5-Workshop/5.5-Policy/_index.md": """---
title : "Create CodePipeline in AWS Console"
date : 2024-01-01
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Goal

Set up a CodePipeline in the AWS Console that connects GitHub with your GameHub deployment workflow.

#### Create the GitHub connection

1. Open AWS Console → Developer Tools → Connections.
2. Click `Create connection`.
3. Select `GitHub` and authorize the repository.
4. Choose the GameHub repo.
5. Confirm the connection status is `Available`.

#### Create the pipeline

1. Open CodePipeline Console.
2. Click `Create pipeline`.
3. Choose `Use a blueprint` or `Start from scratch`.
4. Select `GitHub (version 2)` as the source provider.
5. Select the connection, repository, and branch.
6. Add a build stage with CodeBuild using `buildspec_deploy.yml`.
7. Add a deploy stage with CloudFormation pointing to `pipeline/codepipeline.yaml`.

#### Notes

- If you initialized the pipeline with `sam pipeline init`, reuse the generated `codepipeline.yaml` file.
- Save the connection ARN for automation.
- Confirm that the template path and branch match your repo structure.

#### Pipeline polish

- Add test and monitoring stages for a production-ready flow.
- Document the pipeline stage names and stack naming conventions.
- Use a stable branch for production deploys.

Note: Add UI screenshots for pipeline creation in `images/5-Workshop/5.5-Policy/create-pipeline.svg` and `images/5-Workshop/5.5-Policy/connection-arn.svg`.
""",
    "content/5-Workshop/5.5a-Testing/_index.vi.md": """---
title : "Kiểm thử và Pipeline Testing"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Mục tiêu

Thêm bước kiểm thử tự động vào pipeline để phát hiện lỗi trước khi deploy ứng dụng.

#### Nội dung chi tiết

- Tạo stage `Test` trong pipeline.
- Dùng CodeBuild để chạy unit test và integration test.
- Dừng pipeline nếu kiểm thử thất bại.
- Báo cáo kết quả kiểm thử rõ ràng.

#### Cấu hình buildspec

Sử dụng `buildspec_deploy.yml` để chạy test:
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

#### Với Node.js

Nếu bạn dùng Node.js hoặc frontend test:
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

- Phân chia test thành unit và integration.
- Chạy test quan trọng ở stage đầu để tiết kiệm thời gian.
- Xem CodeBuild logs để tìm nguyên nhân lỗi.
- Dùng kết quả kiểm thử làm gate trước deploy.

#### Kết quả

- Test pass: pipeline tiếp tục tới deploy.
- Test fail: pipeline dừng và báo lỗi.

Note (hình ảnh): Thêm ảnh `test-run.png` vào `images/5-Workshop/5.5a-Testing/`.
""",
    "content/5-Workshop/5.5a-Testing/_index.md": """---
title : "Testing and Pipeline Validation"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Goal

Add an automated test stage to the pipeline so failures are caught before deployment.

#### Detailed coverage

- Create a `Test` stage in CodePipeline.
- Use AWS CodeBuild for unit and integration tests.
- Fail deployments if tests fail.
- Surface test results clearly in the pipeline.

#### Example buildspec

Place test commands in `buildspec_deploy.yml`:
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

For Node.js or frontend tests:
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

- Separate unit and integration tests.
- Run the most important tests early.
- Use CodeBuild logs for debugging.
- Name stages and projects clearly.

#### Expected behavior

- test success continues the pipeline,
- test failure stops the pipeline and shows the failure reason.

Note: Add a placeholder image for the test run in `images/5-Workshop/5.5a-Testing/test-run.svg`.
""",
    "content/5-Workshop/5.5b-Monitoring/_index.vi.md": """---
title : "Giám sát & Logging"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Mục tiêu

Thiết lập giám sát và logging để theo dõi trạng thái ứng dụng GameHub sau khi triển khai.

#### Nội dung chi tiết

- Bật CloudWatch Logs cho Lambda và API Gateway.
- Tạo metric filters cho lỗi và latency.
- Cấu hình alarm khi phát hiện sự cố.
- Gửi cảnh báo bằng SNS hoặc email.

#### Hướng dẫn từng bước

1. Mở CloudWatch Console.
2. Vào Logs > Log groups.
3. Chọn log group của Lambda hoặc API Gateway.
4. Tạo metric filter cho các mẫu lỗi như `ERROR` hoặc HTTP `5xx`.
5. Tạo alarm dựa trên metric filter.

#### Gợi ý cảnh báo

- Lambda error rate vượt 1% trong 5 phút.
- API Gateway `5xx` rate vượt 5% trong 5 phút.
- CodePipeline deployment fail.

#### Kết nối thông báo

- Dùng SNS topic để gửi email hoặc Slack.
- Đặt tên alarm rõ ràng, ví dụ `GameHub-Lambda-Error-Alarm`.
- Kiểm tra dashboard CloudWatch định kỳ.

Note (hình ảnh): Thêm ảnh `cloudwatch-alarms.png` vào `images/5-Workshop/5.5b-Monitoring/`.
""",
    "content/5-Workshop/5.5b-Monitoring/_index.md": """---
title : "Monitoring & Logging"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Goal

Set up monitoring so you can observe GameHub application health after deployment.

#### Detailed coverage

- Enable CloudWatch Logs for Lambda and API Gateway.
- Create metric filters for errors and latency.
- Configure alarms for incidents.
- Send notifications via SNS or email.

#### Implementation steps

1. Open CloudWatch Console.
2. Go to Logs > Log groups.
3. Select the Lambda or API Gateway log group.
4. Create a metric filter for failure patterns such as `ERROR` or HTTP `5xx`.
5. Create an alarm based on the metric filter.

#### Recommended alarms

- Lambda error rate > 1% over 5 minutes.
- API Gateway `5xx` rate > 5% over 5 minutes.
- CodePipeline deployment failures.

#### Notifications

- Use an SNS topic to send email or Slack alerts.
- Name alarms clearly, e.g. `GameHub-Lambda-Error-Alarm`.
- Review the CloudWatch dashboard regularly.

Note: Add a placeholder image for CloudWatch alarms in `images/5-Workshop/5.5b-Monitoring/cloudwatch-alarms.svg`.
""",
    "content/5-Workshop/5.6-Cleanup/_index.vi.md": """---
title : "Triển khai Frontend với AWS Amplify"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Mục tiêu

Triển khai frontend tĩnh của GameHub bằng AWS Amplify và cấu hình build phù hợp.

#### Bước 1: Khởi tạo app Amplify

1. Vào Amplify Console.
2. Nhấn `Deploy an app`.
3. Chọn `GitHub` làm source provider.
4. Xác thực GitHub và chọn repository.

#### Bước 2: Chọn branch và thư mục

1. Chọn nhánh deploy, ví dụ `V1`.
2. Nếu repo là monorepo, bật `My app is a monorepo`.
3. Nhập `frontend` vào `Monorepo root directory`.

#### Bước 3: Cấu hình build

Sử dụng cấu hình sau để build Flutter web trên Amplify:
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
            - flutter pub get
            - flutter build web --release --dart-define=COGNITO_REGION=$COGNITO_REGION --dart-define=COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID --dart-define=COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID --dart-define=API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL --dart-define=API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL
      artifacts:
        baseDirectory: build/web
        files:
          - "**/*"
      cache:
        paths: []
    appRoot: frontend
```

#### Bước 4: Biến môi trường

Thêm biến sau trong Amplify Console:
- `COGNITO_REGION`
- `COGNITO_USER_POOL_ID`
- `COGNITO_CLIENT_ID`
- `API_GATEWAY_HTTP_URL`
- `API_GATEWAY_WS_URL`
- `LOCAL_API_URL`
- `USE_LOCAL_BACKEND`
- `APK_DOWNLOAD_URL`

#### Bước 5: Review và deploy

1. Kiểm tra cấu hình ứng dụng.
2. Nhấn `Save and deploy`.
3. Amplify sẽ tự động build và deploy frontend.

#### Kết quả

- Frontend được host dưới URL Amplify.
- Mỗi lần push lên branch deploy sẽ kích hoạt build tự động.

Note (hình ảnh): Thêm ảnh `amplify-setup.png` vào `images/5-Workshop/5.6-Cleanup/amplify-setup.svg`.
""",
    "content/5-Workshop/5.6-Cleanup/_index.md": """---
title : "Deploy Frontend with AWS Amplify"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

#### Goal

Deploy the GameHub frontend using AWS Amplify and configure the build process.

#### Step 1: Initialize the Amplify app

1. Open Amplify Console.
2. Click `Deploy an app`.
3. Select `GitHub` as the source provider.
4. Authorize the repo and choose the branch.

#### Step 2: Choose branch and folder

1. Select the deployment branch, e.g. `V1`.
2. If the repo is a monorepo, enable `My app is a monorepo`.
3. Set `Monorepo root directory` to `frontend`.

#### Step 3: Build configuration for Flutter web

Use this configuration to build Flutter web in Amplify:
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
            - flutter pub get
            - flutter build web --release --dart-define=COGNITO_REGION=$COGNITO_REGION --dart-define=COGNITO_USER_POOL_ID=$COGNITO_USER_POOL_ID --dart-define=COGNITO_CLIENT_ID=$COGNITO_CLIENT_ID --dart-define=API_GATEWAY_WS_URL=$API_GATEWAY_WS_URL --dart-define=API_GATEWAY_HTTP_URL=$API_GATEWAY_HTTP_URL
      artifacts:
        baseDirectory: build/web
        files:
          - "**/*"
      cache:
        paths: []
    appRoot: frontend
```

#### Step 4: Environment variables

Add these Amplify environment variables:
- `COGNITO_REGION`
- `COGNITO_USER_POOL_ID`
- `COGNITO_CLIENT_ID`
- `API_GATEWAY_HTTP_URL`
- `API_GATEWAY_WS_URL`
- `LOCAL_API_URL`
- `USE_LOCAL_BACKEND`
- `APK_DOWNLOAD_URL`

#### Step 5: Review and deploy

1. Review the app settings.
2. Click `Save and deploy`.
3. Amplify will build and host the frontend.

#### Result

- The frontend will be hosted at an Amplify URL.
- Every push to the deploy branch triggers a build.

Note: Add a placeholder image for Amplify setup in `images/5-Workshop/5.6-Cleanup/amplify-setup.svg`.
""",
}

for path, content in files.items():
    full_path = root / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding='utf-8')
print(f"Wrote {len(files)} updated workshop files")

