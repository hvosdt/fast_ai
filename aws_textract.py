import boto3
from textractcaller.t_call import call_textract, Textract_Features, Query, QueriesConfig, Adapter, AdaptersConfig

if __name__ == "__main__":
    #textract = TextractWrapper(boto3.client("textract"), boto3.resource("s3"), sqs_resource='sqs')
    #response = textract.analyze_file(['FORMS'], "passport.jpeg")
    client = boto3.client('textract')
    with open('image.jpeg', 'rb') as file:
        document = file.read()
    # Create AdaptersConfig
    adapter1 = Adapter(adapter_id="111111111", version=1, pages=[])
    adapters_config = AdaptersConfig(adapters=[adapter1])

    # Call AnalyzeDocument API with custom adapter
    response = call_textract(
        features=[Textract_Features.QUERIES],
        queries_config=QueriesConfig(adapters_config=adapters_config),
        document_location={
                'Bytes': document,                        
            }
        )        
    print(response)