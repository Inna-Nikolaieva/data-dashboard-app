import pytest
import pytest_asyncio

from app.models import UserModel, PostModel


@pytest_asyncio.fixture
async def user(db_session):
    user = UserModel(username="test1", email="test1@test.com", password="test1pass")
    db_session.add(user)
    await db_session.commit()
    return user


@pytest_asyncio.fixture
async def post(db_session, user):
    post = PostModel(title="Test1", body="Post", user_id=user.id)
    db_session.add(post)
    await db_session.commit()
    await db_session.refresh(post)
    return post


@pytest.mark.asyncio
async def test_get_posts(client, post):
    response = await client.get("/posts/")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.asyncio
async def test_get_post(client, post):
    response = await client.get(f"/posts/{post.id}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == post.id
    assert data["title"] == "Test1"


@pytest.mark.asyncio
async def test_get_post_not_found(client):
    response = await client.get("/posts/999")

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_update_post(client, post):
    response = await client.put(f"/posts/{post.id}", json={"title": "Updated"})

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Updated"


@pytest.mark.asyncio
async def test_update_post_not_found(client):
    response = await client.put("/posts/999", json={"title": "Updated"})

    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_post(client, post):
    response = await client.delete(f"/posts/{post.id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Deleted successfully"


@pytest.mark.asyncio
async def test_delete_post_not_found(client):
    response = await client.delete("/posts/999")

    assert response.status_code == 404
