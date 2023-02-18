import boto3
import json

def lambda_handler(event, context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')

    try:
        # Get the request body from the event
        request_body = json.loads(event['body'])

        # Extract the customer information from the request body
        name = request_body['name']
        address = request_body['address']
        phone = request_body['phone']
        email = request_body['email']

        # Insert the customer information into the DynamoDB table
        table = dynamodb.Table('customers')
        table.put_item(
            Item={
                'name': name,
                'address': address,
                'phone': phone,
                'email': email
            }
        )

        # Return a success response
        response = {
            'statusCode': 200,
            'body': json.dumps('Customer information saved successfully')
        }
    except Exception as e:
        # Log the error
        print(str(e))

        # Return an error response
        response = {
            'statusCode': 500,
            'body': json.dumps('An error occurred while saving customer information')
        }

    return response
