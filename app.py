from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()

tutorials = [
    {
        'id' : 1
        'title' : 'json_1',
        'description' : 'description_1'
    },
    {
        'id' : 2
        'title': 'json_2',
        'description': 'description_2'
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