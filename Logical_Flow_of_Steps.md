Create an S3 bucket to host your web app files, such as the HTML file, CSS file, and JavaScript file.
Upload your web app files to the S3 bucket.
Configure the S3 bucket to be public and to host static website content.
Create a Lambda function to handle form submissions from your web app.
Configure an API Gateway to integrate with your Lambda function and enable your web app to send data to the Lambda function.
Create an IAM policy to allow the API Gateway to call the Lambda function and access any other necessary resources, such as the DynamoDB table.
Create a DynamoDB table to store the form submissions.
Configure the Lambda function to store form submissions in the DynamoDB table.
[Optional, but recommended] Create a CloudFront distribution to serve your web app files, improving performance and reducing latency.
Update the DNS records for your domain to point to the CloudFront distribution.
Test your web app to make sure everything is working as expected.