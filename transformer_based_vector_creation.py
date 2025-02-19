# -*- coding: utf-8 -*-
"""Transformer based Vector creation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZhD1YnQPYVplMMyi7PzqsGgcHdRrr2M9
"""

from huggingface_hub import notebook_login

notebook_login()

import pandas as pd
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
!pip install huggingface_hub


def vectorize_df(df, file_path):
    # Define the models to use as a dictionary
    models = {
        "paraphrase-multilingual-MiniLM-L12-v2": "paraphrase-multilingual-MiniLM-L12-v2",
        "All-MiniLM-L12-v2" : "All-MiniLM-L12-v2",
        "bert-base-uncased" : "bert-base-uncased",
        "roberta-large-nli-stsb-mean-tokens" : "roberta-large-nli-stsb-mean-tokens"
    }

    # Enable the progress bar for pandas
    tqdm.pandas()

    # Function to encode text using a specific model
    def encode_text(text, model):
        embeddings = model.encode(text)
        return embeddings.tolist()

    # Process each model
    for model_name, model_path in models.items():
        print(f"Processing with {model_name}...")
        # Load the model
        model = SentenceTransformer(model_path)
        # Create vector column for this model
        column_name = f'Vector {model_name}'
        df[column_name] = df['chat_gpt_explanation'].progress_apply(lambda x: encode_text(x, model))

        # Save the updated DataFrame back to Excel
        df.to_excel(file_path, index=False)
    return df

# File path
file_path = 'updated_1867_Hebrew_Proverbs with Vectors.xlsx'

try:
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Vectorize using all models
    df = vectorize_df(df, file_path)


    print(f"Successfully added vector columns to {file_path}")

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except KeyError as e:
    print(f"Error: Column '{e}' not found in the Excel file. Please ensure the column name is correct")