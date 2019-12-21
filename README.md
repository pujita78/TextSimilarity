
## <Project Name>

Given two texts, the app computes the similarity score or percentage between them.

## Setup Guide

##### Clone the repo

```bash
$ git clone <git-package-name>
$ cd DocTextSimilarity
```


##### Create the virtualenv
```bash
$ virtualenv textsimenv
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Run the app
```bash
$ python run_app.py
```

##### Running the app

Test the app in Postman using POST method with the following details:

* URL - http://localhost:7000/getTextSimilarityScore
* Method - GET
* JSON - 

{

	"text1": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.",
	"text2": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.",
	"metric": "cosine",
	"text_eng_options": ["IgnoreCase", "FilterStopWords"]
}

## API Documentation

### GET /getTextSimilarityScore

##### Body raw (application/json)

```rest
{
    "task": {
        "text.similarity.score",
        "version": "1.0"
        },
    "taskInputs": {
        "text1": <text1>
        "text2": <text2>
        "metric": <cosine/jaccard>
        "text_eng_options": ["IgnoreCase", "FilterStopWords"]
    }
}
```

##### Response:
```bash
"Similarity score using cosine metric: 0.9305779945315913"
```

## Distance Metrics

#### Cosine Similarity

Cosine Similarity metric measures the similarity between two non-zero vectors using Euclidean dot formula.

#### Jaccard Similarity

Jaccard Similarity metric measures the similarity between two non-zero vectors using the size of intersection of two sets and the size of union of two sets.
