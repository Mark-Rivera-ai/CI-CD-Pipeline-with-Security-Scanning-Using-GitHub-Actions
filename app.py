python

from flask import Flask, jsonfiy, request

app = Flask(_name_)

# In-memory storage for to-do items
todos = []

# Add a new to-do item
@app.route('/todo', methods=['POST'])
def add_todo():
  data = request.json
  task = data.get('task')
  if task:
    todos.append(task)
    return jsonify({'message': 'To-do item added', 'task': task}), 201
  return jsonify({'error': 'Task is required'}), 400

#Get all to-do items
@app.route('/todo', methods=['GET'])
def get_todos():
  return jsonify({'todo': todos})

if __name__=='__main__':
  app.run(debug=True)

echo "Initial commit with Flask API code"
    
