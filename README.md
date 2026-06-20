# 🔍 Visual Search Engine

Search your images using natural language — no tags, no filenames, no manual organization.

🔗 **Live Demo:** https://clip-visual-search-engine.streamlit.app/

---

## 🎬 Demo

<p align="center">
  <img src="demo.gif" alt="Visual Search Engine Demo" width="900">
</p>

---

## 🚀 Features

* 🔤 Search images using plain English descriptions
* 🖼️ Find visually similar images using image-to-image search
* ⚡ Fast vector similarity search with FAISS
* 🤖 CLIP-powered multimodal embeddings
* 🌐 Easy-to-use Streamlit interface
* ☁️ Deployed on Streamlit Community Cloud

---

## 📌 What It Does

Upload a collection of images and search them in two ways:

### 🔤 Text Search

Describe what you're looking for:

* "a dog on a beach"
* "red car at night"
* "mountain landscape"

The system finds the most relevant images from your collection.

### 🖼️ Image Search

Upload an image and find visually similar images from the indexed collection.

---

## 🏗️ Architecture

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

## 📂 Project Structure

```text
visual-search-engine/
│
├── app.py
├── requirements.txt
├── demo.gif
├── README.md
└── assets/
```

---

## ⚙️ Run Locally

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

---

## ⚠️ Note

The application is hosted on Streamlit Community Cloud's free tier.

Storage is not persistent across restarts, so indexed images are cleared whenever the application restarts or is redeployed.

Simply re-upload your images and click **Add to Index** again.

---

## 👩‍💻 Author

**Hemavathi G**

* GitHub: https://github.com/HemaG88

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
