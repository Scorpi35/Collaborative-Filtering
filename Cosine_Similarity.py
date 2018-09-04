import numpy as np

def cos_sin(a, b):
    #Taking dot product
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)


#the counts we've computed
sentence_m = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0])
sentence_h = np.array([0, 0, 1, 1, 1, 1, 0, 0, 0])
sentence_w = np.array([0, 0, 0, 1, 0, 0, 1, 1, 1])


#Expecting sentence_m and sentence_h to be more similar
print(cos_sin(sentence_m, sentence_h))
print(cos_sin(sentence_m, sentence_w))


