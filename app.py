from flask import Flask, jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1, 
        'title': u'buy vegetables',
        'description': u'tomato, onion, potato',
        'done': False
    },
    {
        'id': 2, 
        'title': u'do exercise',
        'description': u'walk, squarts',
        'done': False
    }
]

@app.route("/add-data",methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        },400)
    
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "sucess",
        "message": "task added sucessfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

if __name__ == '__main__':
    app.run(debug = True)