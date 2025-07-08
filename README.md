
# 🔍 ETL/ELT Tool Comparator (AI-Powered)

A simple Streamlit web app that recommends ETL/ELT tools based on a user’s specific use case and provides detailed feature comparisons by scraping official websites and using Large Language Models (LLMs) for extraction.

Built with:
- 🧠 **Groq AI (Llama3-70B)**
- 🌐 **SerpAPI (Google Search)**
- ⚙️ **LangChain Web Scraper**
- 🖥️ **Streamlit for UI**

---

## 🚀 Features

✅ Recommend the best ETL/ELT tools based on natural language use cases  
✅ Auto-search and fetch the official tool websites  
✅ Scrape key content from tool websites  
✅ Extract detailed features and comparison points using Groq AI  
✅ Display results in clean, interactive Streamlit dashboards  

---

## 🖥️ Live Demo

*Coming soon on Streamlit Community Cloud / Hugging Face Spaces*

---

## 📸 Screenshots

| Tool Recommendation | Tool Feature Extraction |
|----------------------|------------------------|
| ![Recommendation](https://via.placeholder.com/500x300?text=Recommendation+Screenshot) | ![Feature Extraction](https://via.placeholder.com/500x300?text=Feature+Extraction+Screenshot) |

---

## 🛠 Tech Stack

| Tech | Purpose |
|------|---------|
| **Python 3.10+** | Core programming language |
| **Streamlit** | Web application |
| **Groq (Llama3-70B)** | AI-based feature extraction |
| **SerpAPI** | Search engine for official links |
| **LangChain WebBaseLoader** | Web scraping |
| **BeautifulSoup (Optional)** | HTML parsing (fallback) |

---

## 📝 Installation

1. **Clone this repo**
```bash
git clone https://github.com/yourusername/etl-elt-tool-comparator.git
cd etl-elt-tool-comparator
```

2. **Create virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your API keys**  
Create a `.env` file or set them directly:
```bash
SERPAPI_KEY=your_serpapi_key
GROQ_API_KEY=your_groq_api_key
```

5. **Run the app**
```bash
streamlit run app.py
```

---

## 🔑 How It Works

1. Enter a **use case** (e.g., “Real-time streaming with open-source connectors”)
2. The app recommends **top 3 ETL/ELT tools** using Groq AI
3. Select any tool to **auto-search official website**, **scrape data**, and **extract detailed features** using AI

---

## 📦 Example Use Cases

| Use Case | Recommended Tools |
|----------|-------------------|
| Real-time data ingestion from APIs | Airbyte, Apache NiFi, Flink |
| Cloud-native ELT with Snowflake | Fivetran, Matillion, Hevo |
| Open-source ETL for small business | Singer, Meltano, Airbyte |

---

## 💡 Future Enhancements

- Add caching for faster repeated queries  
- Expand tool database with manual entries  
- Deploy live app with public link  
- Add comparison charts and scoring

---

## 🤝 Contributing

Contributions, ideas, and issues are welcome!  
Please open an issue or pull request on [GitHub](https://github.com/yourusername/etl-elt-tool-comparator).

---

## ⚠️ Disclaimer

This project uses public data and AI-generated responses for informational purposes only.  
Please verify tool suitability for production use.

---

## 📄 License

[MIT License](LICENSE)
