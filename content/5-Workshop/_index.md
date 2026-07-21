---
title : "Clean up resources"
date : 2026-07-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Resource Cleanup Strategy

Follow these sequential steps to delete all initialized infrastructure resources and avoid incurring unwanted maintenance costs:

1. Navigate to **Hosted Zones** in the left menu of the **Route 53** console. Click on the Hosted Zone name `s3.us-east-1.amazonaws.com`. Click **Delete** and confirm by typing the keyword `delete`.

![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)

2. Navigate to **Resolver Rules** in the Route 53 console. Select the rule named `myS3Rule`. Click **Disassociate** to remove this rule from **"VPC Onprem"**, then select the rule again and click **Delete** to completely remove it.

![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)

3. Open the **AWS CloudFormation** console and delete the two stacks deployed for this workshop by clicking the **Delete** button:
   * **`PLOnpremSetup`**
   * **`PLCloudSetup`**

![delete stack](/images/5-Workshop/5.6-Cleanup/delete-stack.png)

4. Clean up and delete the Amazon S3 buckets:
   * Open the **Amazon S3** console.
   * Select the specific S3 bucket created for this lab, click **Empty** and confirm to clear all objects inside.
   * Once the bucket is empty, click **Delete** and re-type the exact bucket name to permanently remove the storage resource.

![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)
