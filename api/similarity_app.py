from flask import Flask, request
from flask_restful import Resource, Api
import json
from similarity import text_metrics
from utils import text_utils


app = Flask(__name__)
api = Api(app)


'''
Call endpoint /getTextSimilarityScore
Input - pageId that uniquely identifies an Image
Output - The Image file in Response
'''


class TextSimilarityScoreApp(Resource):
    def get(self):
        json_payload = json.loads(request.data)

        # Get the 2 input texts
        text1 = json_payload['text1']
        text2 = json_payload['text2']
        metric = json_payload['metric']
        feat_eng_options = json_payload['text_eng_options']

        # options = docs_json['options']

        # Text engineering
        # 1. Convert all characters in the text to lower case if "IgnoreCase" option is present
        # 2. Expand apostrophe contractions
        # 3. Remove punctuation (extract only words using regular expression - managed in text_utils)
        # 4. Convert text into vectors

        if "IgnoreCase" in feat_eng_options:
            text1 = text1.lower()
            text2 = text2.lower()

        if "FilterStopWords" in feat_eng_options:
            text1 = text_utils.stopwords_cleaner(text1)
            text2 = text_utils.stopwords_cleaner(text2)

        vector1 = text_utils.text_to_vector(text_utils.apostrophe_cleaner(text1))
        vector2 = text_utils.text_to_vector(text_utils.apostrophe_cleaner(text2))

        similarity_score = 0.0

        # Determine Similarity score using the given metric
        if metric == "cosine":
            similarity_score = text_metrics.cosine_similarity(vector1, vector2)
        elif metric == "jaccard":
            similarity_score = text_metrics.jaccard_similarity(vector1, vector2)

        response_json = {}
        response_json['metric']  = metric
        response_json['distance_score'] = similarity_score



        # return "Similarity score using {} metric: {}".format(metric, similarity_score)
        return response_json


# Mapping between endpoints and functions
api.add_resource(TextSimilarityScoreApp, '/getTextSimilarityScore')


@app.errorhandler(404)
def not_found(e):
    return '', 404
