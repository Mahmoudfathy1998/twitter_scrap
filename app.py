import boto3
from datetime import date
from datetime import datetime
import json
import scrapTwitter as twitter
import sendEmail as mail

#735256350708633600 my page
#1264208004 al ahly
def lambda_handler(event,context):
    sent = False
    user = event['user']
    tweet = twitter.scrap_twitter(user)
    tweetBody = tweet['full_text']
    TD = tweet['created_at']
    tweetdate =  datetime.strftime(datetime.strptime(TD,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')

    #create a DynamoDB client
    dynamodb = boto3.resource("dynamodb")
    table_name = "tweets"
    table = dynamodb.Table(table_name)

    response = table.get_item(Key={"user":user})
    if "Item" in response:
        saveddate = response["Item"]["createDate"]
        if tweetdate > saveddate:
            table.put_item(Item = {"user":user,"Body": tweetBody,"createDate":tweetdate})
            mail.send_plain_email("mahmed@isolvedhcm.com", tweetBody)
            sent = True
    else:
        table.put_item(Item = {"user":user,"Body": tweetBody,"createDate":tweetdate})
        mail.send_plain_email("mahmed@isolvedhcm.com", tweetBody)
        sent = True
    if sent == True:
        print("A mail with a new tweet was sent to the recipient!")
    else: print("No new tweets!")
        #AAAAAAAAA TEEEEST!
