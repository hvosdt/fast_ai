import boto3

if __name__ == "__main__":
    #textract = TextractWrapper(boto3.client("textract"), boto3.resource("s3"), sqs_resource='sqs')
    #response = textract.analyze_file(['FORMS'], "passport.jpeg")
    client = boto3.client('textract')
    with open('image.jpeg', 'rb') as file:
        document = file.read()
            
    response = client.analyze_document(
        Document={
            'Bytes': document,                
        },
        FeatureTypes=[
            'TABLES',
        ],            
        AdaptersConfig={
            'Adapters': [
                {
                    'AdapterId': 'f63bc34524f2',                    
                    'Version': 'Ver. 3'
                },
            ]
        }
    )
    print(response)