''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5050.
'''
from flask import Flask, render_template, request 
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask('Sentiment Analyzer')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label == None:
        return 'Invalid input'
    else:
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)



@app.route("/")
def render_index_page():
      ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
      return render_template('index.html')

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5050)
