import pytest
from django import urls
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import Client

# @pytest.mark.django_db
# def test_my_user():
#     me = User.objects.get(username="admin")
#     assert me.is_superuser


# def test_my_user():
# assert 1 == 0


@pytest.mark.django_db
def test_my_user():
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    # me = User.objects.get(username="admin")
    # assert me.is_superuser


# @pytest.mark.django_db
# @pytest.fixture
# def client():
#     return Client()


@pytest.mark.parametrize("param", ["about", "contact", "log"])
def test_hello_world(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200
