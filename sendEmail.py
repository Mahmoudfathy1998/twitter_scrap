import boto3

def send_plain_email(recipient , body):
    ses_client = boto3.client("ses", region_name="us-east-1")
    CHARSET = "UTF-8"

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                recipient,
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": "User tweeted a new tweet! \n"+body,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "New Tweet!",
            },
        },
        Source="mafathyaly@gmail.com",
    )