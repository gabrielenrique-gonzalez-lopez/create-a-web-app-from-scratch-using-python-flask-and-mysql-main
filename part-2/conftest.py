import pytest
from flask import g, session
from .db import get_db
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SECRET_KEY": "testing"})

    # Create a test user
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        # Set up test data
        test_user = {
            "name": "Test User",
            "username": "testuser",
            "password": "testpassword",
        }

        # Hash password and insert test user into the database
        test_user["password"] = generate_password_hash(test_user["password"])
        cursor.execute(
            "INSERT INTO tbl_user (user_name, user_username, user_password) "
            "VALUES (%(name)s, %(username)s, %(password)s)",
            test_user,
        )
        db.commit()

    yield app

    # Clean up test data
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM tbl_user WHERE user_username = 'testuser'")
        db.commit()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth(client):
    # Log in as the test user
    with client.session_transaction() as session:
        session["user_id"] = 3  # Assumes test user has ID of 8

    yield client


@pytest.fixture
def logged_out_client(client):
    # Log out by clearing the session
    with client.session_transaction() as session:
        session.clear()

    yield client
