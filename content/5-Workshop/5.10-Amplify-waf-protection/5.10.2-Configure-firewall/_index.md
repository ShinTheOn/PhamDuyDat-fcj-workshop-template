---
title : "Step 2: Configure the firewall options"
date: 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.10.2. </b> "
---

#### Goal

In this step, you will choose the appropriate WAF configuration and enable the recommended protection features.

#### Instructions

![Image 1]({{ "/images/5-Workshop/5.10-Amplify-waf-protection/anh2.png" | relURL }})

On the `Add firewall` page, configure the following options:

1. `Choose configuration`: select `Create new` if you want to create a new WAF configuration, or `Use existing WAF configuration` if one already exists.
2. `Recommended protection`: enable `Enable Amplify-recommended Firewall protection`.
3. This feature helps you:
   - protect against common web security vulnerabilities based on OWASP Top 10,
   - block bots and vulnerability scanners,
   - block malicious IP addresses based on Amazon threat intelligence data.
4. You can also enable advanced options such as restricting access to the default domain, allowing or blocking specific IPs, or filtering by country if needed.

#### Note

Advanced options are optional and can be left at the default setting if you do not need complex rules yet.

