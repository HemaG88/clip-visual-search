import streamlit as st
import os
import shutil
from PIL import Image
from embedder import get_image_embedding, get_text_embedding
from search_engine import add_image, search, load_or_create_index

st.set_page_config(page_title="Visual Search Engine", page_icon="🔍", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
    .hero {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        padding: 2.5rem 2rem; border-radius: 16px;
        margin-bottom: 2rem; text-align: center;
    }
    .hero h1 { color: #fff; font-size: 2.4rem; font-weight: 700; margin: 0; }
    .hero p  { color: #a78bfa; font-size: 1.05rem; margin-top: 0.5rem; }
    .score-badge {
        background: #7c3aed; color: white;
        padding: 2px 10px; border-radius: 20px;
        font-size: 0.8rem; font-weight: 600;
    }
    .stButton>button { background: #7c3aed; color: white; border: none; border-radius: 8px; font-weight: 600; }
    .stButton>button:hover { background: #6d28d9; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🔍 Visual Search Engine</h1>
    <p>Search by Text · Search by Image · Powered by CLIP + FAISS</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📁 Upload Images to Index")
    uploaded_files = st.file_uploader(
        "Drop images here",
        type=["jpg", "jpeg", "png", "webp"],
        accept_multiple_files=True,
        key="indexer"
    )
    if uploaded_files:
        if st.button("➕ Add to Index"):
            progress = st.progress(0)
            for i, file in enumerate(uploaded_files):
                save_path = os.path.join("images", file.name)
                with open(save_path, "wb") as f:
                    shutil.copyfileobj(file, f)
                embedding = get_image_embedding(save_path)
                add_image(embedding, save_path)
                progress.progress((i + 1) / len(uploaded_files))
            st.success(f"✅ Added {len(uploaded_files)} image(s)!")

    index, metadata = load_or_create_index()
    st.markdown("---")
    st.metric("Images in Index", index.ntotal)

    if st.button("🗑️ Clear All"):
        if os.path.exists("index/faiss.index"):
            os.remove("index/faiss.index")
            os.remove("index/metadata.json")
        shutil.rmtree("images", ignore_errors=True)
        os.makedirs("images", exist_ok=True)
        st.rerun()

# ── Two Tabs ─────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🔤 Search by Text", "🖼️ Search by Image"])

def show_results(results):
    """Shared result display for both tabs"""
    if not results:
        st.info("No results found. Try something else!")
        return
    cols = st.columns(min(len(results), 3))
    for i, result in enumerate(results):
        with cols[i % 3]:
            img = Image.open(result["path"])
            st.image(img, use_column_width=True)
            score_pct = round(result["display_score"] * 100, 1)
            fname = os.path.basename(result["path"])
            st.markdown(
                f'<div style="text-align:center">'
                f'<span class="score-badge">Match: {score_pct}%</span><br>'
                f'<small>{fname}</small></div>',
                unsafe_allow_html=True
            )

# ── TAB 1: Text Search ───────────────────────────────────────
with tab1:
    st.markdown("### Type what you're looking for")
    query = st.text_input(
        "", placeholder="e.g. 'a dog on a beach', 'sunset over mountains'",
        label_visibility="collapsed"
    )
    top_k = st.selectbox("Number of results", [3, 5, 10], index=1, key="tk1")

    if st.button("Search 🚀", key="text_search"):
        index, _ = load_or_create_index()
        if index.ntotal == 0:
            st.warning("⚠️ Upload and index some images first!")
        elif not query:
            st.warning("Type something to search!")
        else:
            with st.spinner("Searching..."):
                query_emb = get_text_embedding(query)
                results = search(query_emb, top_k=top_k)
            st.markdown(f"#### Results for: *\"{query}\"*")
            show_results(results)

# ── TAB 2: Image-to-Image Search ────────────────────────────
with tab2:
    st.markdown("### Upload a photo — find visually similar ones")

    query_image = st.file_uploader(
        "Upload a query image",
        type=["jpg", "jpeg", "png", "webp"],
        key="query_img"
    )
    top_k2 = st.selectbox("Number of results", [3, 5, 10], index=1, key="tk2")

    if query_image:
        col_preview, col_gap = st.columns([1, 2])
        with col_preview:
            st.markdown("**Your query image:**")
            st.image(Image.open(query_image), use_column_width=True)

        if st.button("Find Similar Images 🔍", key="img_search"):
            index, _ = load_or_create_index()
            if index.ntotal == 0:
                st.warning("⚠️ Upload and index some images first!")
            else:
                temp_path = "index/query_temp.jpg"
                with open(temp_path, "wb") as f:
                    shutil.copyfileobj(query_image, f)

                with st.spinner("Finding similar images..."):
                    query_emb = get_image_embedding(temp_path)
                    results = search(query_emb, top_k=top_k2)

                os.remove(temp_path)

                st.markdown("#### Most visually similar images:")
                show_results(results)