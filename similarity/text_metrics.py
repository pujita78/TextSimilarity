import math


# Cosine Similarity metric - Measure of similarity between two non-zero vectors
# Derived by using Euclidean dot formula
# https://en.wikipedia.org/wiki/Cosine_similarity
def cosine_similarity(vector1, vector2):
    intersection = set(vector1.keys()) & set(vector2.keys())
    numerator = sum([vector1[x] * vector2[x] for x in intersection])

    sum1 = sum([vector1[x] ** 2 for x in vector1.keys()])
    sum2 = sum([vector2[x] ** 2 for x in vector2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if denominator:
        return float(numerator) / denominator
    else:
        return 0.0


def jaccard_similarity(vector1, vector2):
    # Numerator
    intersection_cardinality = len(set(vector1.keys()) & set(vector2.keys()))

    # Denominator
    union_cardinality = len(set(vector1.keys()) | set(vector2.keys()))

    if union_cardinality:
        return intersection_cardinality / float(union_cardinality)
    else:
        return 0.0
