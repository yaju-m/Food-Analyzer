from google.cloud import language

def parse(text_content):

    client = language.Client()

    document = client.document_from_text(text_content)

    annotations = document.annotate_text()
    entities = document.analyze_entities()

    entities = list(entities)

    food = (max(entities, key = lambda x: x.salience)).name

    nouns = []
    amount = None

    for token in annotations.tokens:
        if token.part_of_speech == "NOUN":
            nouns.append(token.text_content)
        if token.part_of_speech == "NUM":
            amount = token.text_content

    for string in food.split(" "):
        if string in nouns:
            nouns.pop(nouns.index(string))

    return (amount, nouns, food)
