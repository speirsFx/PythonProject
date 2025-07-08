import streamlit as st
import groq
import requests
import re
import os

os.environ['USER_AGENT'] = 'myagent'
import json
from serpapi import GoogleSearch
from langchain_community.document_loaders import WebBaseLoader

# 🔑 API Keys
SERPAPI_KEY = 'df423a6cf93137168eae920eaeb696f66f7a49866d41f6ed629bdb9308585957'
GROQ_API_KEY = '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'


# ✅ Cached Groq Client
# @st.cache_resource
def get_groq_client():
    return groq.Groq(api_key=GROQ_API_KEY)


# @st.cache_resource
def get_search_client():
    return GoogleSearch


client = get_groq_client()
SearchClient = get_search_client()


# ✅ Search Function
def get_first_result_url(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 1
    }
    search = SearchClient(params)
    results = search.get_dict()
    organic = results.get('organic_results', [])
    if organic:
        return organic[0].get('link')
    return None


# ✅ Scrape Website Text
def get_page_data(url):
    loader = WebBaseLoader(url)
    page_data = loader.load().pop().page_content
    return page_data[:6000]


# ✅ Extract Tool Features with Groq
# ✅ Extract Tool Features with Groq
def extract_with_groq(tool_name, url, text):
    prompt = f"""
    Extract key details about the ETL/ELT tool "{tool_name}" from the provided text. Your response should include:
    
    1. A short paragraph (2–3 lines) describing what the tool is and what it does in simple language.
    
    2. A bulleted list of key features and highlights based on the following aspects (only include those that are available from the text):
    - Deployment Type
    - Open Source vs Commercial
    - Target Users
    - Ease of Use
    - Supported Data Connectors
    - Transformation Approach
    - Real-time vs Batch Processing Support
    - Workflow Orchestration Capabilities
    - Scalability and Performance
    - Built-in Data Quality and Validation
    - Monitoring, Logging, and Observability
    - Integration with Cloud Ecosystems
    - Pricing Model
    - Security and Compliance Features
    - Community Size and Ecosystem
    
    The 'tool' name is: **{tool_name}**  
    The official website is: **{url}**
    
    👉 Keep the response concise but informative. No preamble like “Here is the answer” and with no  bold or italic just simple text.
    
    {text}
    """
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=6000
    )
    content = completion.choices[0].message.content
    json_match = content
    return content


# ✅ Recommend Tools from Use Case

# ✅ Recommend Tools from Use Case
def recommend_tools(use_case):
    prompt = f"""
    A user has the following ETL/ELT use case:
    "{use_case}"

    Recommend the 3 most suitable ETL/ELT tools for this use case. For each tool, return:
    - "tool": The name of the tool
    - "reason": A short reason why this tool is a good fit

    Return STRICTLY VALID JSON (no preamble, no explanation) in this exact format:

    {{
      "recommendations": [
        {{
          "tool": "Tool Name",
          "reason": "Why it's a good fit"
        }},
        {{
          "tool": "Tool Name",
          "reason": "Why it's a good fit"
        }},
        {{
          "tool": "Tool Name",
          "reason": "Why it's a good fit"
        }}
      ]
    }}
    """

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    content = completion.choices[0].message.content
    return content


# ✅ Streamlit UI
st.title("🔍 ETL/ELT Tool Recommender + Comparator (Groq + SerpAPI)")

use_case = st.text_area("Describe your ETL/ELT Use Case (e.g., sync Salesforce to Snowflake in real-time)")

if st.button("Get Recommendations"):
    if not use_case.strip():
        st.warning("Please describe your use case.")
    else:
        with st.spinner("🧠 Thinking..."):
            recs = recommend_tools(use_case)
            try:
                recs_json = json.loads(recs)
                # print(recs_json)
            except json.JSONDecodeError:
                print("❌ Invalid JSON format")
            # print(recs)
            # print(recs_json['recommendations'])

        if "recommendations" in recs_json:
            st.subheader("✅ Recommended Tools")
            st.json(recs_json)

            for rec in recs_json["recommendations"]:
                tool_name = rec.get("tool")
                reason = rec.get("reason")
                st.markdown(f"### 🚀 {tool_name}\n*Reason:* {reason}")

                with st.spinner(f"🔍 Fetching {tool_name} details..."):
                    url = get_first_result_url(tool_name)
                    print(url)
                    if url:
                        try:
                            text = get_page_data(url)
                            # print(text)
                            features = extract_with_groq(tool_name, url, text)
                            print(features)
                            st.success(f"🔗 Found: {url}")
                            st.write(features)
                        except:
                            st.error(f"⚠️ Failed to extract details for {tool_name}")
        else:
            st.error("❌ No tools could be recommended.")