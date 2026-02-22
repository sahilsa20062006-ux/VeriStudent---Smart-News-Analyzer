
# 🛡️ VeriStudent - Fake News Detector

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)
![Generative AI](https://img.shields.io/badge/AI-Google%20Gemini-green.svg)
![Live App](https://img.shields.io/badge/Deployed-Hugging%20Face-yellow.svg)

**VeriStudent** is a dual-layer AI tool designed to help students and researchers verify the credibility of online news articles. It combines traditional Machine Learning for pattern recognition with LLMs for deep contextual analysis.

## 🚀 Live Demo
[👉 View the Live App on Hugging Face](https://huggingface.co/spaces/sahilsa04/VeriStudent))

## ✨ Features
* **Automatic Web Scraping:** Paste a URL, and the app extracts the article body using `BeautifulSoup4`.
* **ML Classification:** Detects clickbait and manipulative language patterns using a `PassiveAggressiveClassifier`.
* **Deep Analysis:** Uses **Google Gemini 2.5 Flash** to provide a factual summary and identify logical fallacies.
* **Secure Implementation:** API keys are managed via environment variables for maximum security.

## 🛠️ Tech Stack
* **Backend:** Python
* **ML Library:** Scikit-Learn (TF-IDF Vectorization)
* **API:** Google Generative AI (Gemini API)
* **UI:** Gradio
* **Scraping:** BeautifulSoup4 & Requests

## 🧠 Key Learnings: Solving "Data Leakage"
During development, I identified a significant "Data Leakage" issue where the model was achieving 99% accuracy by simply detecting the word "(Reuters)" in real articles. I implemented a custom preprocessing pipeline using Regular Expressions to strip these tags, forcing the model to learn actual linguistic features rather than just "cheating" on specific metadata.

## ⚙️ How to Run Locally
1. Clone the repo: `git clone https://github.com/YourUsername/VeriStudent.git`
2. Install requirements: `pip install -r requirements.txt`
3. Set your API Key: `export GEMINI_API_KEY='your_key_here'`
4. Run the app: `python veriStudent.py`
