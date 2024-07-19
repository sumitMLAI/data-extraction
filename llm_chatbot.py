import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from retrieve_text import image2text

# Load environment variables from .env
load_dotenv()

# Initialize the ChatGoogleGenerativeAI instance
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=150,
    timeout=None,
    max_retries=2,
)

def llm_chatbot(query,image_path):
    try:
        # Get the API key from environment variables
        google_api_key = os.getenv("GOOGLE_API_KEY")

        if google_api_key:
            os.environ["GOOGLE_API_KEY"] = google_api_key
        else:
            raise ValueError("Google API Key not found in environment variables.")

        # Retrieve context data using retrieve_data function
        context = image2text(image_path)

        # Define the messages to invoke the AI
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant invoice data extraction use only context: {context} only that generates responses in json based on user queries.",
            },
            {
                "role": "human",
                "content": f"user_query: {query} , context: {context}",
            },
        ]

        # Invoke the AI and get the response
        response = llm.invoke(messages)

        # Extract response content
        ai_msg = response.content.strip()  # Get the generated text

        # Extract usage metadata if needed
        # usage_metadata = response.usage_metadata

        return ai_msg

    except Exception as e:
        return f"Error: {e}"

# query="i want all field in json format from my image of invoice data"
# image_path='invoice.png'
# text=llm_chatbot(query,image_path)
# print(text)

