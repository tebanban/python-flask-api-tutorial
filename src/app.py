from flask import Flask, jsonify, request
app = Flask(__name__)
import json
decoded_object = json.loads(original_string)

todos=[
      {"label": "My first task", "done": False},
      {"label": "My second task", "done": False}
      ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
 

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
