from app.app import flask_app, init_db

if __name__ == '__main__':
    init_db()
    flask_app.run(port=5000, host='localhost')
