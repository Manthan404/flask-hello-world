from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/process_parameters', methods=['POST'])
def process_parameters():
    data = request.get_json()  # Get JSON data from the request

    # Extract the "arguments" parameter from the input JSON
    arguments_str = data["choices"][0]["message"]["function_call"]["arguments"]
    
    # Unescape the JSON string
    unescaped_arguments = json.loads(arguments_str.encode('utf-8').decode('unicode_escape'))
    
    return jsonify(unescaped_arguments)

if __name__ == '__main__':
    app.run(debug=True)
