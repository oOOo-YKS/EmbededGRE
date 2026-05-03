# 🔴 EmbeddedGRE: AI-Powered Semantic Vocabulary Clustering

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oOOo-YKS/EmbededGRE/blob/main/notebooks/main.ipynb)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**EmbeddedGRE** is a Machine Learning pipeline that modernizes GRE vocabulary studying. Instead of relying on traditional, alphabetical A-Z lists, this project uses advanced Sentence Transformers to group 3,000 GRE words into mathematical, meaning-based clusters.

![EmbeddedGRE Semantic Map](image/README/1777846868453.png)
*A 2D UMAP projection of the 3,000-word GRE vocabulary space. Each color represents a distinct semantic function.*

---

## 💡 The Problem with Traditional Lists
Traditional GRE study guides group words like *abase* and *abash* together simply because they start with the letter "A". This ignores how the human brain actually learns language: through contextual and functional relationships.

## 🛠️ The AI Solution: "The Blindfold Technique"
To achieve pure semantic clustering, this project utilizes **BAAI/bge-large-en-v1.5**, a state-of-the-art embedding model. 

By "blindfolding" the AI to the spelling of the word and only feeding it the English definition, we eliminate prefix bias. The AI reads the *meaning* and maps the words into a high-dimensional vector space.

### Technology Stack
* **Embeddings:** `SentenceTransformers` (BGE-Large)
* **Dimensionality Reduction:** `UMAP` (to compress the 384-dimensional space)
* **Clustering:** `HDBSCAN` (to automatically discover the natural number of semantic categories)

---

## 📂 Project Structure

```text
EmbeddedGRE/
├── data/
│   ├── L-GRE-再要你命3000.csv       # Raw, original A-Z vocabulary list
│   └── Final_EmbeddedGRE_List.csv   # Processed list, sorted by AI clusters
├── notebooks/
│   └── EmbeddedGRE_Main.ipynb       # The complete Data Science pipeline
└── README.md