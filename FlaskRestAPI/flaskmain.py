from flask import Flask, jsonify, request
import uuid
app = Flask(__name__)

users = [
    {'id': str(uuid.uuid4()), 'name': 'Manolo', 'surname': 'Sánchez', 'picture': 'https://1.bp.blogspot.com/-6oaF4wbcuVk/X6j9XadyVPI/AAAAAAAAPTU/hyvqPCV1Jns3uS_88GKD6JmeGA2jaIJzQCLcBGAsYHQ/w320-h213/neol%25C3%25ADtico%2Btecnolog%25C3%25ADa.png', 'email': 'manolito@gmail.com', 'phone': '633459937', 'address': 'calle blank'},
    {'id': str(uuid.uuid4()), 'name': 'Aurelio', 'surname': 'Martinez', 'picture': 'https://blogger.googleusercontent.com/img/a/AVvXsEiwDlw51c_aPKKFWL-k23lkzeizX2c0z59PChE4nR9RGdIz0Kjbfhq2XfgLCVc1lXLdiNOJ-rAwDoz4fhv8jKKat6dg-rSm8zMk9ednDVS2-3l4KsISzWxWjw2kOfMINzJwAsR2qF6PCWOihwE-GacE6RfcLLIS74wnjaW8VZ7uxYTGPQ5NL2WmMp_l', 'email': 'aurelio34534@hotmail.com', 'phone': '664564567', 'address': 'calle guadalupe 10'},
    {'id': str(uuid.uuid4()), 'name': 'Matilde', 'surname': 'Rodríguez', 'picture': 'https://blogger.googleusercontent.com/img/a/AVvXsEgZ-DXOcZucVBJL2LrXpyUqGfCdW2jlZAl-Z3uJ518zIc0O7aIcklNKfUcyvmIFycUjhSQ6yJhfl3h1YourFQuhLqYLyZYDJcgOYdvhbhcbpxk5CkJaRKrr2xTeLlxzL4ruq1ZgGq5lepuNCxod98uclWsTKItZqal0iSakZyQPibDoquT4rblvynrO=s16000', 'email': 'fireyrdr@gmail.com', 'phone': '676545645', 'address': 'calle asturias 23'},
    {'id': str(uuid.uuid4()), 'name': 'Josefina', 'surname': 'Gómez', 'picture': 'https://1.bp.blogspot.com/-6vYbikCV6ZQ/YF5z-Zm2qWI/AAAAAAAATlE/TTWNPQxG1nEUo2D2LqxurZ_YzbE6LPFHACLcBGAsYHQ/s600/75.png', 'email': 'hol342@mail.com', 'phone': '656756453', 'address': 'calle de la esperanza 56'}
]

@app.route('/users', methods=['GET'])
def getUsers():
    return jsonify({'users': users})

@app.route('/users/<string:user_id>',  methods=['GET'])
def getUser(user_id):
    usersFound = [user for user in users if user['id'] == user_id]
    if (len(usersFound) > 0):
        return jsonify({'user': usersFound[0]})
    return jsonify({'mensaje': 'usuario no encontrado'})

@app.route('/users', methods=['POST'])
def adduser():
    new_user = {
        'id': str(uuid.uuid4()),
        'name': request.json['name'],
        'surname': request.json['surname'],
        'picture': request.json['picture'],
        'email': request.json['email'],
        'phone': request.json['phone'],
        'address': request.json['address'],
    }
    users.append(new_user)
    return jsonify({'users': users})

@app.route('/users/<string:user_id>', methods=['PUT'])
def edituser(user_id):
    usersFound = [user for user in users if user['id'] == user_id]
    if (len(usersFound) > 0):
        usersFound[0]['name'] = request.json['name']
        usersFound[0]['surname'] = request.json['surname']
        usersFound[0]['picture'] = request.json['picture']
        usersFound[0]['email'] = request.json['email']
        usersFound[0]['phone'] = request.json['phone']
        usersFound[0]['address'] = request.json['address']
        return jsonify({
            'mensaje': 'usuario actualizado',
            'user': usersFound[0]
        })
    return jsonify({'mensaje': 'usuario no encontrado'})

@app.route('/users/<string:user_id>', methods=['DELETE'])
def deleteuser(user_id):
    usersFound = [user for user in users if user['id'] == user_id]
    if len(usersFound) > 0:
        users.remove(usersFound[0])
        return jsonify({
            'mensaje': 'usuario eliminado',
            'users': users
        })

if __name__ == '__main__':
    app.run(debug=True, port=6668)