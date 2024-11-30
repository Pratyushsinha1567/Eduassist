'''from flask import Flask, request, jsonify, render_template
from main import main  # Import the main function from your pipeline file

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('w.html')  # Assuming you have an 'index.html' template file

# Route to handle user queries
@app.route('/ask', methods=['POST'])
def ask():
    # Get the query from the POST request (supports both form and JSON)
    query = request.form.get('query') or request.json.get('query')
    
    # Call the main pipeline function with the user query
    if query:
        answer = main(query)  # Replace 'main' with the function that processes the query
        return jsonify({'answer': answer})
    else:
        return jsonify({'error': 'No query provided'}), 400

# Main entry point for running the app
if __name__ == '__main__':
    app.run(debug=True)'''
from flask import Flask, render_template, request, jsonify
from main import main  # Import your main.py functions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('w.html')  # This renders the HTML file you provided

@app.route('/ask', methods=['POST'])
def ask():
    # Get the query from the frontend
    query = request.form.get('query')

    # Call the main function to get the answer
    answer = main(query)

    # Return the answer as JSON to the frontend
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

