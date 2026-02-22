import os
import gradio as gr
from google import genai
import requests
from bs4 import BeautifulSoup

# 1. This is API Key
API_KEY = os.environ.get("GEMINI_API_KEY")

# --- THE WEB SCRAPER FUNCTION ---
def extract_text_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paragraphs = soup.find_all('p')
        article_text = " ".join([p.get_text() for p in paragraphs])
        return article_text
    except Exception as e:
        return f"ERROR: {e}"

# --- THE MASTER AI FUNCTION ---
def pure_ai_factchecker(article_url, article_text):
    final_text = ""
    
    if article_url.strip():  
        scraped_text = extract_text_from_url(article_url.strip())
        if "ERROR:" in scraped_text or len(scraped_text) < 50:
            return "⚠️ Could not extract text from this link. The website might be blocking bots. Please try pasting the text manually in the box below."
        final_text = scraped_text
    elif article_text.strip():  
        final_text = article_text
    else:
        return "⚠️ Please provide either a valid link OR paste the article text!"

    client = genai.Client(api_key=API_KEY)
    
    prompt = f"""
    You are an expert fact-checker for students. Analyze the following news article.
    
    Format your response exactly like this:
    VERDICT: [Write either "🚨 SUSPICIOUS / MANIPULATIVE" or "✅ RELIABLE / FACTUAL"]
    SUMMARY: [Write a 2-sentence summary of the claims]
    REASONING: [Bullet point 3 reasons why you reached this verdict, focusing on tone, sources, or logic]
    
    ARTICLE TEXT TO ANALYZE:
    {final_text}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error: Could not connect to Google. Check your API key! (Details: {e})"

# --- THE USER INTERFACE ---
interface = gr.Interface(
    fn=pure_ai_factchecker,
    inputs=[
        gr.Textbox(lines=1, placeholder="🔗 Option 1: Paste a News URL here...", label="News Link"),
        gr.Textbox(lines=6, placeholder="📝 Option 2: OR Paste the article text here...", label="News Text")
    ],
    outputs=gr.Textbox(label="AI Fact-Check Report", lines=10),
    title="🛡️ VeriStudent - Smart News Analyzer",
    description="Paste a news link **OR** the article text below. Our bot will extract the facts and give you a valid news.",
    theme="soft" 
)

# Launch it! 
interface.launch()
