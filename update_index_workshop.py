from pathlib import Path
content = '''---
title: "Workshop CI/CD với AWS SAM và AWS Amplify"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---




# Thiết lập CI/CD với AWS SAM, AWS CodePipeline và AWS Amplify

#### Tổng quan

Trong workshop này, bạn sẽ học cách:
- Khởi tạo pipeline CI/CD bằng AWS SAM (`sam pipeline init --bootstrap`).
- Cấu hình source và stage Dev/Prod cho ứng dụng.
- Kết nối AWS CodePipeline với GitHub qua AWS CodeConnections.
- Tạo pipeline trên AWS Console từ template CloudFormation.
- Triển khai frontend bằng AWS Amplify.

#### Nội dung

1. [Giới thiệu workshop](5.1-Workshop-overview/)
2. [Chuẩn bị](5.2-Prerequiste/)
3. [Khởi tạo pipeline SAM](5.3-S3-vpc/)
4. [Cấu hình Repository và Stage](5.4-S3-onprem/)
5. [Tạo CodePipeline trên AWS Console](5.5-Policy/)
6. [Triển khai Frontend với AWS Amplify](5.6-Cleanup/)
'''
Path('content/5-Workshop/_index.vi.md').write_text(content, encoding='utf-8')
print('wrote content/5-Workshop/_index.vi.md')

