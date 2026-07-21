---
title : "Step 4: Wait for the system to associate and finish"
date: 2026-07-12
weight : 4
chapter : false
pre : " <b> 5.10.4. </b> "
---

#### Goal

In this step, you will wait for AWS to finish associating WAF with your Amplify application and verify the final status.

#### Instructions

![Image 1]({{ "/images/5-Workshop/5.10-Amplify-waf-protection/anh4.png" | relURL }})

1. After clicking `Add firewall`, the system returns to the Firewall management page.
2. The `Web Application Firewall` section may initially show `Associating`.
3. This process usually takes a few minutes while AWS initializes and applies the security rules.
4. Once completed, you can click `View WAF logs` to review allowed and blocked traffic.

#### Expected result

When the process finishes, your application will be protected by AWS WAF and ready for traffic monitoring and control.

