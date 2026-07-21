---
title : "Clean up resources after the workshop"
date: 2026-07-12
weight : 11
chapter : false
pre : " <b> 5.11. </b> "
---

#### Goal

In this section, you will remove the AWS resources created during the workshop so that your environment stays organized and you avoid unnecessary charges.

#### Why cleanup matters

After the workshop, services such as AWS CodePipeline, AWS CloudFormation, AWS Amplify, AWS WAF, CodeConnections, and related S3 buckets may continue to run and incur costs. It is therefore important to delete the resources you no longer need in the correct order.

#### Cleanup principles

Follow the reverse order of the setup process:

1. Delete the frontend application in Amplify.
2. Remove the WAF association and delete the Web ACL if it is no longer needed.
3. Delete the pipeline and the related CloudFormation stacks.
4. Remove any leftover buckets, roles, policies, and CodeConnections.

#### Step 1: Delete the frontend application in AWS Amplify


1. Open the AWS Amplify Console.
2. Select the frontend application you deployed during the workshop.
3. Open `App settings` or `Actions` and choose `Delete app`.
4. Confirm the action to remove the app from the Amplify environment.

#### Step 2: Remove WAF and delete the security configuration


1. Open the AWS WAF console or the Amplify Firewall section.
2. Delete any Web ACLs, rule groups, or firewall associations linked to the application.
3. If you created a dedicated WAF configuration for the workshop, remove it after detaching it from the app.

#### Step 3: Delete the pipeline and CloudFormation stacks


1. Open AWS CodePipeline and delete the pipeline you created for the workshop.
2. In the AWS CloudFormation console, select the related stacks such as the Dev stack, Prod stack, or the bootstrap stack created by the SAM pipeline.
3. Click `Delete` to remove each stack.
4. If an S3 bucket was created by the stack, empty the bucket first if AWS requires it before deletion.

#### Step 4: Remove CodeConnections and related resources


1. Go to `Developer Tools` → `Settings` → `Connections` and delete the GitHub connection you created.
2. Open the IAM console and remove any roles or policies created for the pipeline or deployment.
3. If you created CloudWatch log groups, S3 buckets, or other auxiliary resources for the workshop, delete or clean them up as needed.

#### Important note

- Before deleting anything, make sure you are not going to need the data or logs for reporting or evaluation.
- Some resources may remain in a deleting state for a few minutes while AWS finishes the cleanup process.
- If you want to keep the data but stop paying for the service, you can pause or retain the resources instead of deleting them completely.

#### Expected result

After completing these steps, your workshop environment will be cleaned up, costs will be reduced, and no extra AWS resources will remain from the practice session.
