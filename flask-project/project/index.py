from flask import Flask, jsonify, request

app = Flask(__name__)

fields = [
{
"id": "abc",
"title": "Alphabet",
"content": "A, B, C, ...",
"views": 1,
"timestamp": 1555832341
},
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)