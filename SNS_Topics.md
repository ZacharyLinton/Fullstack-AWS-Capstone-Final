1. S3: If there are any 4xx or 5xx errors on the bucket, send an SNS notification to the web app owner.
2. CloudFront: If there is a high level of 4xx or 5xx errors on the distribution, send an SNS notification to the web app owner.
3. Lambda: If the function execution time exceeds a certain threshold or there is a high level of errors, send an SNS notification to the web app owner.
4. API Gateway: If there is a high level of 5xx errors on the API Gateway, send an SNS notification to the web app owner.
