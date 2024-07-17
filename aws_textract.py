import textractcaller as tc
import trp.trp2 as t2
import boto3

def recognize_passport(filename):
    textract = boto3.client('textract', region_name="us-east-1")
    q1 = tc.Query(text="What is Passport No?", alias="passport_no", pages=["1"])
    q2 = tc.Query(text="What is Surname", alias="surname", pages=["1"])
    q3 = tc.Query(text="What is Given_name", alias="given_name", pages=["1"])
    q4 = tc.Query(text="What is Date of birth", alias="date_of_birth", pages=["1"])
    q5 = tc.Query(text="What is Date of issue", alias="date_of_issue", pages=["1"])
    q6 = tc.Query(text="What is Date of expiry", alias="date_of_expiry", pages=["1"])
    adapter1 = tc.Adapter(adapter_id="f63bc34524f2", version="3", pages=["1"])
    textract_json = tc.call_textract(
        input_document="image.jpeg",
        queries_config=tc.QueriesConfig(queries=[q1, q2, q3, q4, q5, q6]),
        adapters_config=tc.AdaptersConfig(adapters=[adapter1]),
        features=[tc.Textract_Features.QUERIES],
        boto3_textract_client=textract)
    t_doc: t2.TDocument = t2.TDocumentSchema().load(textract_json)  # type: ignore
    for page in t_doc.pages:
        query_answers = t_doc.get_query_answers(page=page)
        for x in query_answers:
            print(f"{x[1]},{x[2]}")
    return query_answers

if __name__ == '__main__':
    recognize_passport('image.jpeg')