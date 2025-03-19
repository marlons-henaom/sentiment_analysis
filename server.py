''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This function analice the sentiments
    '''
    text_to_analyze = request.args.get("textToAnalyze")

    if text_to_analyze == '':
        return "El texto no puede ser vacío"

    response = sentiment_analyzer(text_to_analyze)

    # Extraer la etiqueta y la puntuación de la respuesta
    label = response['label']
    score = response['score']

    # Verifica si el label es None, lo que indica un error o entrada no válida
    if label is None:
        return "¡Entrada no válida! Intenta de nuevo."

    # Devolver una cadena formateada con la etiqueta de sentimiento y la puntuación
    return f"El texto proporcionado ha sido identificado \
            como {label.split('_')[1]} con una puntuación de {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This funtions executes the flask app and deploys it on localhost:5000
    app.run(debug=True)
