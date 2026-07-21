---
title : "Test the Gateway Endpoint"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.3.2 </b> "
---

#### Create S3 bucket

1. Navigate to **S3 management console**
2. In the Bucket console, choose **Create bucket**

![Create bucket](/images/5-Workshop/5.3-S3-vpc/create-bucket.png)

3. In **the Create bucket console**
+ **Name the bucket**: choose a name that hasn't been given to any bucket globally (hint: lab number and your name)

![Bucket name](/images/5-Workshop/5.3-S3-vpc/bucket-name.png)

+ Leave other fields as they are (default)
+ Scroll down and choose **Create bucket**

![Create](/images/5-Workshop/5.3-S3-vpc/create-button.png) 

+ Successfully create S3 bucket.

![Success](/images/5-Workshop/5.3-S3-vpc/bucket-success.png)

#### Connect to EC2 with Session Manager

+ For this workshop, you will use **AWS Session Manager** to access several **EC2 instances**. **Session Manager** is a fully managed **AWS Systems Manager** capability that allows you to manage your **Amazon EC2 instances** and on-premises virtual machines (VMs) through an interactive browser-based shell. Session Manager provides secure and auditable instance management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

+ For a deeper understanding of Session Manager, see the First cloud journey [Lab](https://000058.awsstudygroup.com/1-introduce/).

1. In the **AWS Management Console**, start typing ```Systems Manager``` in the quick search box and press **Enter**:

![system manager](/images/5-Workshop/5.3-S3-vpc/sm.png)

2. From the **Systems Manager** menu, find **Node Management** in the left menu and click **Session Manager**:

![system manager](/images/5-Workshop/5.3-S3-vpc/sm1.png)

3. Click **Start Session**, and select **the EC2 instance** named **Test-Gateway-Endpoint**. 
{{% notice info %}}
This EC2 instance is already running in "VPC Cloud" and will be used to test connectivity to Amazon S3 through the Gateway endpoint you just created (s3-gwe). {{% /notice %}}

![Start session](/images/5-Workshop/5.3-S3-vpc/start-session.png)

**Session Manager** will open a new browser tab with a shell prompt: `sh-4.2 $`

![Success](/images/5-Workshop/5.3-S3-vpc/start-session-success.png)

You have successfully started a session. In the next step, we will create an S3 bucket and a file in it.

#### Create a file and upload it to the S3 bucket

1. Change to the `ssm-user` home directory by typing `cd ~` in the CLI.

![Change user's dir](/images/5-Workshop/5.3-S3-vpc/cli1.png)

2. Create a new file to use for testing with the command `fallocate -l 1G testfile.xyz`, which will create a 1GB file named `testfile.xyz`.

![Create file](/images/5-Workshop/5.3-S3-vpc/cli-file.png)

3. Upload the file to the S3 bucket with the command `aws s3 cp testfile.xyz s3://your-bucket-name`. Replace `your-bucket-name` with the name of the S3 bucket that you created earlier.

![Uploaded](/images/5-Workshop/5.3-S3-vpc/uploaded.png)

You have successfully uploaded the file to your S3 bucket. You can now terminate the session.

#### Check the object in the S3 bucket

1. Navigate to the S3 console.  
2. Click the name of your S3 bucket.
3. In the bucket console, you will see the file you uploaded to your S3 bucket.

![Check S3](/images/5-Workshop/5.3-S3-vpc/check-s3-bucket.png)

#### Section summary

Congratulations on completing access to S3 from VPC. In this section, you created a Gateway endpoint for Amazon S3 and used the AWS CLI to upload an object. The upload worked because the Gateway endpoint allowed communication to S3 without needing an Internet Gateway attached to "VPC Cloud". This demonstrates the functionality of the Gateway endpoint as a secure path to S3 without traversing the Public Internet.













