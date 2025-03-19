''' Imports library '''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    """
    Analyze the sentiment of the given text.

    Args:
        text_to_analyse (str): The text to be analyzed.

    Returns:
        str: The sentiment result (e.g., positive, negative, neutral).
    """
    # Url Api AI Watson
    url = "https://sn-watson-sentiment-bert.labs.skills." \
          "network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Request via Post to API
    response = requests.post(url, json = myobj, headers=headers, timeout=10)

    if response.status_code == 200:
        # Analizando la respuesta JSON de la API
        formatted_response = json.loads(response.text)
        # Extrayendo la etiqueta de sentimiento y la puntuación de la respuesta
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None

    # Devolviendo un diccionario que contiene los resultados del análisis de sentimientos
    return {'label': label, 'score': score}
