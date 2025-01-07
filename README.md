# Social Media Performance Analysis Insights Tool  

This project is a no-code solution built using LangFlow, Python, and Streamlit to provide insights into social media engagement metrics. The application uses Astra DB for data storage and Groq AI for generating actionable insights.  

## About the Project  
This application was developed as a **Pre-Hackathon Assignment** by Team **TechTea**. It demonstrates the potential of combining no-code tools and APIs for solving real-world problems.  

## Features  
- **No-Code Components:** Built using LangFlow.  
- **User Interface:** Developed using Python and Streamlit for a seamless user experience.  
- **Data Storage:** Integration with Astra DB for managing engagement data.  
- **Insights Generation:** Powered by Groq AI to deliver actionable insights based on user input.  

## Application Flow  
1. **Chat Input Component:** Accepts the user’s post type input.  
2. **Prompt Component:** Prepares the query based on the input.  
3. **Astra DB Tool Component:** Fetches average engagement metrics (likes, shares, comments) for the each post type from the database.  
4. **Groq AI Agent Component:** Processes the metrics and generates actionable insights using the Groq AI API key.  
5. **Chat Output Component:** Displays the insights to the user in a conversational format.  

## Technologies Used  
- **LangFlow:** For application flow design using no-code components.  
- **Python:** For backend logic and integration.  
- **Streamlit:** For building the user interface.  
- **Astra DB:** For storing and querying engagement metrics.  
- **Groq AI API:** For generating insights.  
