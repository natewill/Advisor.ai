from flask import Flask, request, jsonify
from llamaparse import your_function_name  # Replace with actual function from llamaparse

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_message():
    data = request.json  # Get JSON data sent from the front end
    message = data.get('message')
    
    # Call the function from llamaparse.py to process the message
    result = your_function_name(message)  # Replace with actual function

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)