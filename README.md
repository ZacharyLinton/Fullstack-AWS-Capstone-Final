# Fullstack AWS Capstone Final Project

This project is a web application that allows users to sign up with their name, address, email, and phone number.

## Prerequisites

Before getting started, you'll need to have the following:

- An AWS account
- Basic knowledge of HTML
- Basic knowledge of AWS services such as S3, Lambda, API Gateway, and CloudFront

## Getting Started

To set up this web application, follow these steps:

1. Clone this repository to your local machine.
2. Set up an S3 bucket to host your HTML file.
3. Create a Lambda function that will handle the form submission and store the data in a DynamoDB table.
4. Create an API Gateway REST API to trigger the Lambda function.
5. Set up a CloudFront distribution to serve your S3 bucket.
6. Update the `index.html` file with your API endpoint URL.
7. Upload the updated `index.html` file to your S3 bucket.
8. Test your web application by opening the CloudFront URL.

## Built With

- HTML
- AWS S3
- AWS Lambda
- AWS API Gateway
- AWS DynamoDB
- AWS CloudFront

## Author

- Zachary W. Linton

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
