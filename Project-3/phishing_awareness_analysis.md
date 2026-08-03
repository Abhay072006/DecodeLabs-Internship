# Phishing Awareness Analysis

## Introduction

Phishing is a cyber attack where attackers impersonate trusted organizations to steal sensitive information such as usernames, passwords, banking details, or personal information.

The purpose of this project is to analyze phishing emails, identify red flags, and explain why they are unsafe.

## Sample 1: Fake PayPal Email

### Email

From: support-paypal@paypa1-security.com

Subject: Urgent! Your PayPal account has been suspended.

Dear Customer,

We detected unusual activity on your account.
Click the link below within 24 hours to verify your account.

http://paypal-security-login.xyz

Failure to verify will permanently suspend your account.

Thank you,
PayPal Security Team

---

### Red Flags Identified

- Urgent subject line.
- 24-hour deadline creates pressure.
- Fake sender email (`paypa1` instead of `paypal`).
- Suspicious website link.
- Generic greeting ("Dear Customer").

### Why is it Unsafe?

The email attempts to scare the user into clicking a fake website. The sender address and website are not official. Entering login credentials on the fake website could lead to account compromise.

### Safe Action

- Do not click the link.
- Open the official PayPal app or website directly.
- Verify account notifications through the official account.

## Sample 2: Fake Internship Selection Email

### Email

From: hr@reva-careers.com

Subject: Important: Internship Selection List Released

Dear Student,

Congratulations!

You have been selected for the final internship round.

Please download the attached file "Internship_List.pdf.exe" and complete your verification today.

If you fail to verify before 6:00 PM, your offer will be cancelled.

Regards,
HR Team

---

### Red Flags Identified

- Suspicious sender email.
- Generic greeting ("Dear Student").
- Double extension attachment (`.pdf.exe`).
- Urgent deadline (6:00 PM).
- Threat of offer cancellation.

### Why is it Unsafe?

The attachment is an executable (`.exe`) file disguised as a PDF document. Running it could install malware or steal sensitive information.

### Safe Action

- Do not download or open the attachment.
- Verify the internship through the official website or HR contact.
- Delete or report the email if it is confirmed to be phishing.
  
## Sample 3: Fake Amazon Delivery Email
### Email

From: support@amazon.com

Subject: Your Amazon Order Has Been Delayed

Hello Abhay,

We apologize for the delay in delivering your recent order.

To track your package, please click the link below:

https://amazon.com.track-order-login.info

Thank you for shopping with Amazon.

Amazon Customer Support


### Red Flags Identified

- Fake tracking link.
- Domain tries to imitate Amazon.
- Link does not point to the official Amazon website.

### Why is it Unsafe?

The email redirects users to a fake website that may steal login credentials or personal information.

### Safe Action

- Do not click the link.
- Open the official Amazon app or website directly.
- Check order status from the official account.

## Sample 4: Fake Google Security Alert

### Email

From: security@google-support.com

Subject: Security Alert: Unusual Sign-in Attempt Detected

Hi Abhay,

We detected a login attempt from a new device in another country.

If this wasn't you, please secure your account immediately by clicking the link below:

https://accounts.google.com.verify-user-login.net

You have 30 minutes to verify your identity, or your Gmail account will be permanently disabled.

Thank you,

Google Security Team

### Red Flags Identified

- Fake sender domain.
- Urgent security warning.
- Fake Google verification link.
- 30-minute deadline.
- Threat of permanent account suspension.

### Why is it Unsafe?

The email attempts to create panic and redirect users to a fake login page to steal their Google account credentials.

### Safe Action

- Do not click the link.
- Open Gmail using the official website or app.
- Verify account security through Google's official Security page.

## Conclusion

This project improved my understanding of phishing attacks by helping me identify suspicious links, fake sender addresses, urgent language, malicious attachments, and social engineering techniques. I also learned the importance of verifying emails through official websites and avoiding untrusted links or attachments.
