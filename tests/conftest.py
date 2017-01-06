# -*- coding: utf-8 -*-

import pytest
from kriegspiel.models import User


@pytest.fixture
def user(db):
    user = User.objects.create(
        email='test@test.com',
        username='test',
        # password hash for 'test'
        password='pbkdf2_sha256$30000$hrV5EM0C6B5O$KAfbHEJbiiuaYyZUZmWQSf3t5KA5/rg9B48cickmrxk=',
    )
    return user
