from flask import Flask, request, jsonify

app = Flask(__name__)

# This is our fake database for now (just a list)
todos = [
    {"id": 1, "task": "Buy groceries"},
    {"id": 2, "task": "Study Flask"},
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()        # get the data sent by client
    new_todo = {
        "id": len(todos) + 1,        # auto generate id
        "task": data["task"]         # get task from what client sent
    }
    todos.append(new_todo)           # save it to our fake database
    return jsonify(new_todo), 201    # return it with status 201 created

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)  # find the todo
    if todo is None:
        return jsonify({"message": "Todo not found"}), 404  # return 404 if not found
    todos.remove(todo)                                        # remove it
    return jsonify({"message": "Todo deleted"}), 200 
    
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)  # find the todo
    if todo is None:
        return jsonify({"message": "Todo not found"}), 404  # return 404 if not found
    data = request.get_json()                                # get new data from client
    todo["task"] = data["task"]                              # update the task
    return jsonify(todo), 200                                # return updated todo        # return success
if __name__ == '__main__':
    app.run(debug=True)