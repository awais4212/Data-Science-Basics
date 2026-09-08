from flask import Flask,jsonify, request

app=Flask(__name__)

items = [
    {'id':1, 'task':'Item 1', 'description': 'This is Item 1'},
    {'id':2, 'task':'Item 2', 'description': 'This is Item 2'}
]

@app.route('/')
def home():
    return "This is a TODO List"
    

@app.route('/items', methods=['GET'])
def getItems():
    return jsonify(items)

@app.route('/items/<int:itemID>', methods=['GET'])
def getItem(itemID):
    item =  next((item for item in items if item[id]==itemID),None)
    if item is None:
        return jsonify({"error":'Item is not present in the TODO List'})
    return jsonify(item)


@app.route('/items',methods=['POST'])
def createList():
    if not request.json or not "task" in request.json:
        return jsonify({"error":'Item is not present in the TODO List'}),400
    newItem = {
        'id': items[-1]['id']+1 if items else 1,
        'task': request.json['task'],
        'description': request.json['description']
    }
    items.append(newItem)
    return jsonify(newItem),201

@app.route('/items/<int:itemID>', methods=['PUT'])
def updateItem(itemID):
    item = next((item for item in items if item['id']==itemID),None)
    
    if item is None:
        return jsonify({"error":'Item is not present in the TODO List'}), 400
    
    item ['task'] = request.json.get('task',item['task'])
    item['description']=request.json('description',item['description'])
    return jsonify(item)
    
@app.route('/items/<int:itemID>', methods=['DELETE'])
def delete(itemID):
    global items
    items = [item for item in items if item['id'] != itemID]
    return jsonify({'result': "Item is Deleted Succesfullly"})

if __name__=='__main__':
    with app.test_client() as client:
        response = client.post('/items', json={
            'task': 'Buy groceries',
            'description': 'Milk, eggs, bread'
        })
        print(response.status_code)
        print(response.json)
    app.run(debug=True)
    