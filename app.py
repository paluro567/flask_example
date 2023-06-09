from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello, World!'}

@app.route('/route2')
def newrt():
    return {'message': 'route 2!'}


# get information from the route entered
@app.route('/users/<username>')
def show_user(username):
    # Retrieve user information based on the username
    return f'User entered: {username}'


if __name__ == '__main__':
    app.run()
