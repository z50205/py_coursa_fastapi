import pytest
from fastapi.testclient import TestClient
from app import app  # 替換成你的 FastAPI 實例
from model import User,Course  # 替換為你 User 類別的位置

client = TestClient(app)

def test_create_user_success(monkeypatch):
    # 模擬 User.query_users_by_name 回傳 None（代表帳號未存在）
    monkeypatch.setattr(User, "query_users_by_name", lambda username: None)
    
    # 模擬 User.create_users 成功執行
    monkeypatch.setattr(User, "create_users", lambda u, p, n, e, i: None)

    response = client.post("/api/users", data={
        "username": "newuser",
        "password": "secret",
        "name": "New User",
        "email": "newuser@example.com",
        "is_instructor": "false"
    })

    assert response.status_code == 201
    assert response.json() == {"status": "ok", "detail": "create user success."}

def test_create_user_duplicate(monkeypatch):
    # 模擬 query_users_by_name 回傳使用者（代表已存在）
    monkeypatch.setattr(User, "query_users_by_name", lambda username: {"username": "newuser"})

    response = client.post("/api/users", data={
        "username": "newuser",
        "password": "secret",
        "name": "New User",
        "email": "newuser@example.com",
        "is_instructor": "false"
    })

    assert response.status_code == 409
    assert response.json() == {"status": "fail", "detail": "duplicate user name."}

def test_delete_course_success(monkeypatch):
    # 模擬 Course.delete_courses 不報錯
    monkeypatch.setattr(Course, "delete_courses", lambda cid: None)

    response = client.delete("/api/courses/123")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "detail": "delete course success."}