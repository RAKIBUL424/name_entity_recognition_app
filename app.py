from flask import Flask, render_template, request
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route("/entity", methods=["GET", "POST"])
def entity():
    if request.method == "POST":
        file = request.files.get('file')
        
        if file:
            # Debugging: Print file info
            print(f"File received: {file.filename}")
            
            # Read the file's content
            redable_file = file.read().decode('utf-8', errors='ignore')
            
            # Process the text with spaCy
            docs = nlp(redable_file)
            html = displacy.render(docs, style='ent', jupyter=False)
            
            # Render the results in the template
            return render_template("index.html", html=html, text=redable_file)

    # If GET request, render the form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
