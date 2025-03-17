from flask import Flask, request, jsonify
from pyresparser import ResumeParser  # Use pyresparser instead of resume_parser
import spacy

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    file.save(file.filename)

    # Parse resume
    data = ResumeParser(file.filename).get_extracted_data()

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
