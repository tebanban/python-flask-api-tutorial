from flask import Flask, jsonify
app = Flask(__name__)

todos=[
      {"label": "My first task", "done": False}
      
      ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return jason_text

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)