from app import create_app

app = create_app()


def main():
    print("Hello from flaskhello!")


if __name__ == "__main__":
    app.run(debug=True)
