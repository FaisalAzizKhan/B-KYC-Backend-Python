from app.Flask.FlaskInitialization import create_app  # Correct import for the app factory

app = create_app()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
