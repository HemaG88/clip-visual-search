# 🔍 Visual Search Engine

Search your images using natural language — no tags, no filenames, no manual organization.

🔗 **Live :** https://clip-visual-search-engine.streamlit.app/


---

## 🎬 Demo

<p align="center">
  <img src="demo.gif" alt="Visual Search Engine Demo" width="900">
</p>

---


## Features

* Search images using plain English descriptions
* Find visually similar images using image-to-image search
* Fast vector similarity search with FAISS
* CLIP-powered multimodal embeddings
* Easy-to-use Streamlit interface
* Deployed on Streamlit Community Cloud


## What It Does

Upload a collection of images and search them in two ways:

### Text Search->

Describe what you're looking for:

* "a dog on a beach"
* "red car at night"
* "Wine on a table"

The system finds the most relevant images from your collection.

###  Image Search->

Upload an image and find visually similar images from the indexed collection.

---

## Architecture

```text
Image  ──┐
          ├──▶ CLIP ──▶ Embeddings ──▶ FAISS ──▶ Ranked Results
Text   ──┘
```

CLIP converts both images and text into a shared vector space. Images and text with similar meanings are positioned close together, allowing efficient cross-modal search.

FAISS performs high-speed nearest-neighbor search to retrieve the most relevant matches.

---

## 🛠️ Tech Stack

| Technology                | Purpose                  |
| ------------------------- | ------------------------ |
| CLIP                      | Image & Text Embeddings  |
| FAISS                     | Vector Similarity Search |
| Streamlit                 | Web Interface            |
| PyTorch                   | Deep Learning Framework  |
| Python                    | Backend Logic            |
| Streamlit Community Cloud | Deployment               |

---



##  Run Locally

Clone the repository:

```bash
git clone https://github.com/HemaG88/visual-search-engine.git
cd visual-search-engine
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🌐 Live Application

Try the hosted version:

https://clip-visual-search-engine.streamlit.app/

Upload a few images, click **Add to Index**, and start searching.

Thank u hope this project helped u & worth it
