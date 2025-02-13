# Prov2Vec
Our code used for our paper on Prov2Vec under NLP class.

As part of this class we explored a new method for language translation for proverbs to other langueges, as well as inner langueges classification.

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

1. We first processed the data - creating the explenation by using API call to chatGPT 4o mini using this file `filename`.
2. Then we took those explenation from step 1, and encoded it to vectors using couple of embeding models using this file `transformer_based_vector_creation.py`.
3. Finaly, We used the embeding and did research and clustering done here `analysis_and_clustering.ipynb` and used it to extract the results.
