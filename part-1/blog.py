from flask import (Blueprint, current_app, flash, g, redirect, render_template,
                   request, url_for)
from werkzeug.exceptions import abort

from .db import get_db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    current_app.logger.debug("Handling request to / route.")
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("USE flask_blog")
    query = ("SELECT id, title, content, created_at, author_id, user_username"
        " FROM posts p JOIN tbl_user u ON p.author_id = u.user_id"
        " ORDER BY created_at DESC")
    cursor.execute(
        query
    )
    return render_template("index.html", posts=cursor.fetchall())


def get_post(id, check_author=True):
    """Get a post and its author by id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    query = ("SELECT id, title, content, created_at, author_id, user_username"
            " FROM posts p JOIN tbl_user u ON p.author_id = u.user_id"
            " WHERE p.id = %s")
    cursor = get_db().cursor(dictionary=True)
    cursor.execute(query, (id,))
    post = cursor.fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post

