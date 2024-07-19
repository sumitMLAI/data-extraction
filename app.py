import logging
from flask import Flask, request, jsonify,render_template
from llm_chatbot import llm_chatbot
import json
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/data_extraction', methods=['POST'])
def chatbot_endpoint():
    if request.method == 'POST':
        try:
            # Check if the request contains form data and files
            if 'query' not in request.form or 'image' not in request.files:
                return jsonify({'error': 'Missing required fields: query or image'}), 400

            # Get query from form data
            query = request.form['query']

            # Get image file from request files
            image_file = request.files['image']

            # Save the image file locally (optional)
            image_path = 'uploaded_image.png'  # Choose your own path and filename
            image_file.save(image_path)

            # Call your LLM chatbot function here
            text= llm_chatbot(query, image_path)
            print("**************************************************",text)
            data= text.replace('```json\n', '').replace('\n```', '')
            response=json.loads(data)
            

            # Assuming your llm_chatbot function returns a response dictionary
            return jsonify({"Response": response})

        except Exception as e:
            # Log the exception
            logging.error(f"Exception occurred: {str(e)}")
            return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
