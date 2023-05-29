import pytest
from flask import g, session, url_parse
from .db import get_db
from .auth import login, login_required


def test_index(client, auth):
    # test that index page requires authentication
    response = client.get("/")
    assert b"Log In" in response.data

    # test that posts show up on index page
    auth.login()
    response = client.get("/")
    assert b"Test Title" in response.data
    assert b"Test Content" in response.data
    assert b"Test User" in response.data


def test_create(client, auth):
    # test that create page requires authentication
    response = client.get("/create")
    assert url_parse(response.headers["Location"]).path == "/auth/login"

    # test creating a post
    auth.login()
    response = client.post("/create", data={"title": "created", "content": ""})
    assert url_parse(response.headers["Location"]).path == "/blog/create"

    response = client.post(
        "/create", data={"title": "created", "content": "test content"}
    )
    assert url_parse(response.headers["Location"]).path == "/blog/index"
    with client:
        response = client.get("/")
        assert b"created" in response.data


def test_update(client, auth):
    # test that update page requires authentication
    response = client.get("/3/update")
    assert response.headers["Location"] == "http://localhost:5000/auth/login"

    # test that non-authors cannot update a post
    auth.login()
    response = client.get("/2/update")
    assert b"Test Title" in response.data
    assert b"Test Content" in response.data
    assert b"Test User" not in response.data

    # test that authors can update a post
    response = client.post("/3/update", data={"title": "updated", "content": ""})
    assert response.headers["Location"] == "http://localhost:5000/blog/1/update"

    response = client.post(
        "/3/update", data={"title": "updated", "content": "test content"}
    )
    assert response.headers["Location"] == "http://localhost:5000/blog/index"
    with client:
        response = client.get("/")
        assert b"updated" in response.data


def test_delete(client, auth):
    # test that delete route requires authentication
    response = client.post("/3/delete")
    assert response.headers["Location"] == "http://localhost:5000/auth/login"

    # test that non-authors cannot delete a post
    auth.login()
    response = client.post("/2/delete")
    assert response.status_code == 403

    # test that authors can delete a post
    response = client.post("/3/delete")
    assert response.headers["Location"] == "http://localhost:5000/blog/index"
    with client:
        response = client.get("/")
        assert b"Test Title" not in response.data
        assert b"Test Content" not in response.data


@pytest.mark.parametrize(
    ("path", "status_code"),
    (
        ("/", 200),
        ("/create", 200),
        ("/3/update", 200),
        ("/3/delete", 302),
    ),
)
@login_required
def test_login_required(client, path, status_code):
    response = client.post(path)
    assert response.headers["Location"] == "http://localhost:5000/auth/login"

    response = client.get(path)
    assert response.status_code == status_code