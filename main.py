from .app.webhook import app

if __name__ == "__main__":
    app.run(debud=True, port=5000)
