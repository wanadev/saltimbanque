import nox


PYTHON_FILES = [
    "saltimbanque",
    "setup.py",
    "noxfile.py",
    "wsgi.py",
]

PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]


@nox.session(reuse_venv=True)
def lint(session):
    session.install("flake8", "black")
    session.run("flake8", *PYTHON_FILES)
    session.run(
        "black",
        "--check",
        "--diff",
        "--color",
        *PYTHON_FILES,
    )


@nox.session(reuse_venv=True)
def black_fix(session):
    session.install("black")
    session.run("black", *PYTHON_FILES)
