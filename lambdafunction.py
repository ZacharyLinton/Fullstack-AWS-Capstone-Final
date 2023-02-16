import json
import boto3

def lambda_handler(event, context):
    # Get the data from the form
    name = event.get('name')
    address = event.get('address')
    email = event.get('email')
    phone = event.get('phone')

    # Store the data in a DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('signup')
    table.put_item(
        Item={
            'Name': name,
            'Address': address,
            'Email': email,
            'Phone': phone
        }
    )

    # Return a success response
    response = {
        'statusCode': 200,
        'body': json.dumps('Sign up successful!')
    }
    return response
