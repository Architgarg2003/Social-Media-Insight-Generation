# import json
# import requests
# import streamlit as st
# from streamlit_chat import message as st_message
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Constants for LangFlow API
# BASE_API_URL = "https://api.langflow.astra.datastax.com"
# LANGFLOW_ID = "08ba690e-8c9f-4f82-a03a-2e91bc9d6f0f"
# FLOW_ID = "ae5a24cf-7841-4c48-be60-367d3c2a404c"
# APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
# ENDPOINT = "insight"


# # Function to call LangFlow API
# def run_flow(message: str) -> dict:
#     api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
#     payload = {
#         "input_value": message,
#         "output_type": "chat",
#         "input_type": "chat",
#     }
#     headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
#     response = requests.post(api_url, json=payload, headers=headers)
#     response.raise_for_status()  # Raise HTTPError for bad responses
#     return response.json()


# # Main function
# def main():
#     st.set_page_config(
#         page_title="Social Media Performance Analysis",
#         page_icon="📊",
#         layout="centered",
#         initial_sidebar_state="expanded",
#     )

#     # Header section
#     st.markdown(
#         """
#         <style>
#         .title-style {
#             text-align: center;
#             font-size: 36px;
#             font-weight: bold;
#             color: #4CAF50;
#             margin-bottom: 20px;
#         }
#         .subtitle-style {
#             text-align: center;
#             font-size: 18px;
#             color: #6c757d;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
#     st.markdown('<div class="title-style">📊 Social Media Performance Analysis</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subtitle-style">Get insights into your social media strategies!</div>', unsafe_allow_html=True)

#     # Initialize session state for chat history
#     if "messages" not in st.session_state:
#         st.session_state["messages"] = []

#     # Input section
#     st.markdown("---")
#     st.markdown("### 💬 Enter a post type to get insights:")
#     message = st.text_area("", placeholder="Post type (e.g. reels, carousel, static images)...", height=100)

#     # Button to send the query
#     if st.button("🔍 Get Insights"):
#         if not message.strip():
#             st.error("🚫 Please enter a message.")
#         else:
#             try:
#                 with st.spinner("⏳ Running analysis..."):
#                     # Call the LangFlow API
#                     response = run_flow(message)
#                     response_text = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get("results", {}).get("message", {}).get("text", "No insights available.")

#                 # Add new message to the chat history
#                 st.session_state["messages"].insert(0, {"user": message, "bot": response_text})

#             except Exception as e:
#                 st.error(f"⚠ An error occurred: {str(e)}")

#     # Display chat messages, latest at the top
#     st.markdown("---")
#     for i, msg in enumerate(st.session_state["messages"]):
#         st_message(msg["user"], is_user=True, key=f"user_{i}")
#         st_message(msg["bot"], is_user=False, key=f"bot_{i}")

#     # Footer section
#     st.markdown("---")
#     st.markdown(
#         """
#         <div style="text-align: center; font-size: 14px; color: #6c757d;">
#         Made by Team Matrix
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# if __name__ == "__main__":
#     main()



# import json
# import requests
# import streamlit as st
# from streamlit_chat import message as st_message
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Constants for LangFlow API
# BASE_API_URL = "https://api.langflow.astra.datastax.com"
# LANGFLOW_ID = "08ba690e-8c9f-4f82-a03a-2e91bc9d6f0f"
# FLOW_ID = "ae5a24cf-7841-4c48-be60-367d3c2a404c"
# APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
# ENDPOINT = "insight"

# def run_flow(message: str) -> dict:
#     api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
#     payload = {
#         "input_value": message,
#         "output_type": "chat",
#         "input_type": "chat",
#     }
#     headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
#     response = requests.post(api_url, json=payload, headers=headers)
#     response.raise_for_status()
#     return response.json()

# def main():
#     # Page configuration
#     st.set_page_config(
#         page_title="Social Media Analyzer",
#         page_icon="📱",
#         layout="wide",
#         initial_sidebar_state="collapsed",
#     )

#     # Custom CSS
#     st.markdown("""
#         <style>
#         /* Main container styling */
#         .main {
#             padding: 2rem;
#         }
        
#         /* Header styling */
#         .title-style {
#             text-align: center;
#             font-size: 2.5rem;
#             font-weight: bold;
#             background: linear-gradient(45deg, #4CAF50, #2196F3);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             margin-bottom: 1rem;
#         }
        
#         .subtitle-style {
#             text-align: center;
#             font-size: 1.2rem;
#             color: #6c757d;
#             margin-bottom: 2rem;
#         }
        
#         /* Chat container styling */
#         .chat-container {
#             background-color: #f8f9fa;
#             border-radius: 10px;
#             padding: 1rem;
#             margin: 1rem 0;
#             max-height: 500px;
#             overflow-y: auto;
#         }
        
#         /* Message styling */
#         .stTextInput>div>div>textarea {
#             border-radius: 20px;
#         }
        
#         .stButton>button {
#             border-radius: 20px;
#             width: 100%;
#             background-color: #4CAF50;
#             color: white;
#         }
        
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 8px;
#         }
        
#         ::-webkit-scrollbar-track {
#             background: #f1f1f1;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb {
#             background: #888;
#             border-radius: 10px;
#         }
        
#         ::-webkit-scrollbar-thumb:hover {
#             background: #555;
#         }
        
#         /* Footer styling */
#         .footer {
#             text-align: center;
#             padding: 1rem;
#             color: #6c757d;
#             position: fixed;
#             bottom: 0;
#             width: 100%;
#             background-color: white;
#         }
        
#         /* Loading animation */
#         .loading {
#             display: inline-block;
#             width: 20px;
#             height: 20px;
#             border: 3px solid rgba(0,0,0,.3);
#             border-radius: 50%;
#             border-top-color: #4CAF50;
#             animation: spin 1s ease-in-out infinite;
#         }
        
#         @keyframes spin {
#             to { transform: rotate(360deg); }
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     # Header
#     st.markdown('<div class="title-style">Social Media Performance Analyzer</div>', unsafe_allow_html=True)
#     st.markdown('<div class="subtitle-style">Unlock powerful insights for your social media strategy</div>', unsafe_allow_html=True)

#     # Create two columns for layout
#     col1, col2 = st.columns([2, 1])

#     with col1:
#         # Chat container
#         st.markdown("### 💬 Chat History")
#         chat_container = st.container()
        
#         # Initialize session state
#         if "messages" not in st.session_state:
#             st.session_state["messages"] = []

#         # Display chat messages in scrollable container
#         with chat_container:
#             st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#             for i, msg in enumerate(reversed(st.session_state["messages"])):
#                 st_message(msg["user"], is_user=True, key=f"user_{i}")
#                 st_message(msg["bot"], is_user=False, key=f"bot_{i}")
#             st.markdown('</div>', unsafe_allow_html=True)

#     with col2:
#         # Input section
#         st.markdown("### 📝 New Analysis")
#         message = st.text_area(
#             "",
#             placeholder="Describe your post type (e.g., reels, carousel, static images)...",
#             height=100,
#             key="input"
#         )

#         # Analysis button
#         if st.button("🔍 Analyze", key="analyze"):
#             if not message.strip():
#                 st.error("⚠️ Please enter a message first.")
#             else:
#                 try:
#                     with st.spinner("🔄 Analyzing your request..."):
#                         response = run_flow(message)
#                         response_text = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get("results", {}).get("message", {}).get("text", "No insights available.")
#                         st.session_state["messages"].append({"user": message, "bot": response_text})
#                         st.rerun()  # Updated from experimental_rerun()
#                 except Exception as e:
#                     st.error(f"❌ Error: {str(e)}")

#         # Tips section
#         with st.expander("💡 Tips for better analysis"):
#             st.markdown("""
#                 - Be specific about the post type
#                 - Include relevant metrics if available
#                 - Mention your target audience
#                 - Specify your goals
#             """)

#     # Footer
#     st.markdown(
#         """
#         <div class="footer">
#             Made with ❤️ by Team Matrix | v2.0
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()


import json
import requests
import streamlit as st
from streamlit_chat import message as st_message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants for LangFlow API
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "08ba690e-8c9f-4f82-a03a-2e91bc9d6f0f"
FLOW_ID = "ae5a24cf-7841-4c48-be60-367d3c2a404c"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "insight"

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    # Page configuration
    st.set_page_config(
        page_title="Social Media Analyzer",
        page_icon="📱",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Custom CSS with updated footer styling
    st.markdown("""
        <style>
        /* Main container styling */
        .main {
            padding: 2rem;
            margin-bottom: 60px; /* Add space for footer */
        }
        
        /* Header styling */
        .title-style {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(45deg, #4CAF50, #2196F3);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        .subtitle-style {
            text-align: center;
            font-size: 1.2rem;
            color: #6c757d;
            margin-bottom: 2rem;
        }
        
        /* Chat container styling */
        .chat-container {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            max-height: 500px;
            overflow-y: auto;
            border: 1px solid #2f363d;
        }
        
        /* Message styling */
        .stTextInput>div>div>textarea {
            border-radius: 20px;
        }
        
        .stButton>button {
            border-radius: 20px;
            width: 100%;
            background-color: #4CAF50;
            color: white;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #1b1f23;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #2f363d;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #444d56;
        }
        
        /* Footer styling */
        .footer-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: linear-gradient(to right, #1a1a1a, #2d2d2d);
            padding: 1rem;
            z-index: 1000;
            border-top: 1px solid #383838;
        }
        
        .footer-content {
            display: flex;
            justify-content: center;
            align-items: center;
            color: #a0a0a0;
            font-size: 0.9rem;
            gap: 0.5rem;
        }
        
        .footer-heart {
            color: #ff4b4b;
            animation: pulse 1.5s infinite;
        }
        
        .footer-version {
            background-color: #383838;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            margin-left: 8px;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        /* Loading animation */
        .loading {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid rgba(0,0,0,.3);
            border-radius: 50%;
            border-top-color: #4CAF50;
            animation: spin 1s ease-in-out infinite;
        }
        
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        
        /* Dark theme elements */
        .stExpander {
            border: 1px solid #2f363d;
            border-radius: 8px;
            background-color: #1b1f23;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<div class="title-style">Social Media Performance Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-style">Unlock powerful insights for your social media strategy</div>', unsafe_allow_html=True)

    # Create two columns for layout
    col1, col2 = st.columns([2, 1])

    with col1:
        # Chat container
        st.markdown("### 💬 Chat History")
        chat_container = st.container()
        
        # Initialize session state
        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        # Display chat messages in scrollable container
        with chat_container:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            for i, msg in enumerate(reversed(st.session_state["messages"])):
                st_message(msg["user"], is_user=True, key=f"user_{i}")
                st_message(msg["bot"], is_user=False, key=f"bot_{i}")
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Input section
        st.markdown("### 📝 New Analysis")
        message = st.text_area(
            "",
            placeholder="Describe your post type (e.g., reels, carousel, static images)...",
            height=100,
            key="input"
        )

        # Analysis button
        if st.button("🔍 Analyze", key="analyze"):
            if not message.strip():
                st.error("⚠️ Please enter a message first.")
            else:
                try:
                    with st.spinner("🔄 Analyzing your request..."):
                        response = run_flow(message)
                        response_text = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get("results", {}).get("message", {}).get("text", "No insights available.")
                        st.session_state["messages"].append({"user": message, "bot": response_text})
                        st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

        # Tips section
        with st.expander("💡 Tips for better analysis"):
            st.markdown("""
                - Be specific about the post type
                - Include relevant metrics if available
                - Mention your target audience
                - Specify your goals
            """)

    # Updated footer with modern dark theme
    st.markdown(
        """
        <div class="footer-container">
            <div class="footer-content">
                Made with <span class="footer-heart">❤️</span> by Team Matrix
                <span class="footer-version">v2.1</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()