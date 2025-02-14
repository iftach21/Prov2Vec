# Prov2Vec
Our code used for our paper on Prov2Vec under NLP class.

To view our paper, you're welcome to read the following file: `Converting_Hebrew_Proverbs_and_Idioms_from_Hebrew_to_English.pdf` in this repo.

## Abstract
Understanding the semantic relationships be-
tween proverbs across and within languages
provides insights into cultural and linguistic
connections. This paper introduces a novel ap-
proach, Prov2Vec, where we generate vector
embeddings for proverbs using GPT-4 Mini
explanations combined with few Token embed-
dings models. These embeddings are evalu-
ated for semantic similarity using cosine sim-
ilarity. Our work builds upon previous ef-
forts in Hebrew-English translation of idioms
but shifts focus to embedding-based analysis
of proverbs, uncovering deeper connections
within and across languages. The dataset com-
prises 5000 English proverbs, 1800 Hebrew
proverbs, and 100 proverbs in Chinese, Ara-
bic, and French. We highlight the methodology,
showcase examples, and discuss the implica-
tions of our findings in computational linguis-
tics and cultural studies.

## Data set
Our dataset is available in this link:


[Dataset](https://drive.google.com/file/d/15vfFSbOqoiwMO8YeYtY5Fa0oSxNY5i88/view?usp=sharing)

It consist of English, Arabic, Chinese, French and Hebrew proverbs that we collected.
in total:
1. 1867 in Hebrew
2. 4437 in English
3. 127 in Chinese
4. 100 in French
5. 100 in Arabic.


## Code
![dataset_processing_method](https://github.com/user-attachments/assets/6a102c5f-e80c-4e60-b127-bc36acafdd01)


Our code split into our method pipeline:

1. We first processed the data - creating the explenation by using API call to chatGPT 4o mini using this file `sentence_explanations_chatgpt.ipynb`.
2. Then we took those explenation from step 1, and encoded it to vectors using couple of embeding models using this file `transformer_based_vector_creation.py`.
3. Finaly, We used the embeding and did research and clustering done here `analysis_and_clustering.ipynb` and used it to extract the results.
