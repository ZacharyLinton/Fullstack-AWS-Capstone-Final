S3: If there are any 4xx or 5xx errors on the bucket, send an SNS notification to the web app owner.
CloudFront: If there is a high level of 4xx or 5xx errors on the distribution, send an SNS notification to the web app owner.
Lambda: If the function execution time exceeds a certain threshold or there is a high level of errors, send an SNS notification to the web app owner.
API Gateway: If there is a high level of 5xx errors on the API Gateway, send an SNS notification to the web app owner.