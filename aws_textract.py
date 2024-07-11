from textract import TextractWrapper
import boto3

if __name__ == "__main__":
    textract = TextractWrapper(boto3.client("textract"), boto3.resource("s3"), sqs_resource='sqs')
    response = textract.analyze_file("passport.jpeg")
    print(response)
    