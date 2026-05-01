import pytest
import pytest_asyncio

from app.models import UserModel, PostModel, CommentModel


@pytest_asyncio.fixture
async def user(db_session):
    user = UserModel(username="test2", email="test2@test.com", password="test2pass")
    db_session.add(user)
    await db_session.commit()
    return user


@pytest_asyncio.fixture
async def post(db_session, user):
    post = PostModel(title="Test2", body="Post", user_id=user.id)
    db_session.add(post)
    await db_session.commit()
    await db_session.refresh(post)
    return post


@pytest_asyncio.fixture
async def comment(db_session, user, post):
    comment = CommentModel(body="Test comment", post_id=post.id, user_id=user.id)
    db_session.add(comment)
    await db_session.commit()
    await db_session.refresh(comment)
    return comment


@pytest.mark.asyncio
async def test_update_comment(client, comment):
    response = await client.put(
        f"/comments/{comment.id}", json={"body": "Updated comment"}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["body"] == "Updated comment"


@pytest.mark.asyncio
async def test_update_comment_not_found(client):
    response = await client.put("/comments/999", json={"body": "Updated"})

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_comment(client, comment):
    response = await client.delete(f"/comments/{comment.id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Deleted successfully"


@pytest.mark.asyncio
async def test_delete_comment_not_found(client):
    response = await client.delete("/comments/999")

    assert response.status_code == 404
