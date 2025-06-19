from app import create_app

app = create_app()  # calling a factory function to create the Flask app


def main():
    print("Hello from flaskhello!")


if __name__ == "__main__":
    app.run(debug=True)
