# -*- coding: utf-8 -*-

import pytest


auth_url = '/api/auth/sign_in'


@pytest.mark.django_db
def test_auth_success(user, client):
    data = {
        'email': user.email,
        'password': 'test',
    }
    response = client.post(auth_url, data)
    assert response.status_code == 200
    token = response.json()['data']['token']
    assert isinstance(token, str)
    assert token != ''


@pytest.mark.django_db
def test_auth_failure(user, client):
    data = {
        'email': user.email,
        'password': 'wrong_password',
    }
    response = client.post(auth_url, data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_auth_without_password(user, client):
    data = {
        'email': user.email
    }
    response = client.post(auth_url, data)
    assert response.status_code == 400