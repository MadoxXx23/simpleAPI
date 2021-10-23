from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

tutorials = [
    {
        'title' : 'Video #1',
        'description' : 'GET, POST routes'
    },
    {
        'title': 'Video #2',
        'description': 'PUT, DELETE routes'
    }
]



@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)


@app.route('/tutorials', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


if __name__== '__main__':
    app.run()