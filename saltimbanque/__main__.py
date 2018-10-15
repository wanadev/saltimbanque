import os

from .app import app


PORT = int(os.environ["PORT"]) if "PORT" in os.environ else 5000


def main():
    app.run(port=PORT)


if __name__ == "__main__":
    main()
