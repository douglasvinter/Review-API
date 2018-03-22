# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from api.models.reviews import Review


class LoginJWTTokenTestCase(APITestCase):
    """Test case to validated JWT Token"""
    login = reverse("reviews:login")
    verify = reverse("reviews:token/verify")
    refresh = reverse("reviews:token/refresh")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_authentication_without_password(self):
        """Test login without password that should fail"""
        response = self.client.post(self.login, {"username": "snowman"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        """Test login with wrong password that should fail"""
        response = self.client.post(self.login, {"username": self.username, "password": "I_know"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_data(self):
        """Test login with valid parameters"""
        response = self.client.post(self.login, {"username": self.username, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("token" in json.loads(response.content))

    def test_jwt_token_refresh(self):
        """Test token refresh"""
        response = self.client.post(self.login, {"username": self.username, "password": self.password})
        self.assertEqual(200, response.status_code)
        response = self.client.post(self.refresh, json.loads(response.content))
        self.assertEqual(200, response.status_code)

    def test_jwt_token_verify(self):
        """Test token verify endpoint"""
        response = self.client.post(self.login, {"username": self.username, "password": self.password})
        self.assertEqual(200, response.status_code)

        response = self.client.post(self.verify, json.loads(response.content))
        self.assertEqual(200, response.status_code)


class ReviewListCreateAPITestCase(APITestCase):
    """Test case to validate reviews list API"""
    login = reverse("reviews:login")
    reviews = reverse("reviews:list")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.payload = {
                "rating": 5,
                "title": "API Unit Test review",
                "summary": "Some text that contains a Unit Test API Review"
        }
        self.api_authentication()

    def api_authentication(self):
        """Sets API token before any request"""
        response = self.client.post(self.login, {"username": self.username, "password": self.password})
        jwt = json.loads(response.content)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt.get('token'))

    def test_create_review(self):
        """Test create review API"""
        response = self.client.post(self.reviews, self.payload)
        self.assertEqual(201, response.status_code)

    def test_review_list(self):
        """Test Listing API for reviews"""
        mock = self.payload
        mock.update({'user': self.user, 'ip_address': '127.0.0.1'})
        Review.objects.create(**mock).save()
        response = self.client.get(self.reviews)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(json.loads(response.content)), Review.objects.filter(user=self.user).count())


class ReviewDetailAPITestCase(APITestCase):
    """Test case to validate reviews detail API"""
    login = reverse("reviews:login")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        payload = {
                "rating": 5,
                "title": "API Unit Test review",
                "summary": "Some text that contains a Unit Test API Review",
                'user': self.user,
                'ip_address': '127.0.0.1'
        }
        self.review = Review.objects.create(**payload)
        self.reviews = reverse("reviews:detail", kwargs={"review_id": self.review.id})
        self.api_authentication()

    def api_authentication(self):
        """Sets API token before any request"""
        response = self.client.post(self.login, {"username": self.username, "password": self.password})
        jwt = json.loads(response.content)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + jwt.get('token'))

    def test_get_review_by_id(self):
        """Test get review by review_id"""
        response = self.client.get(self.reviews)
        self.assertEqual(200, response.status_code)

    def test_review_update(self):
        """Test review update by review_id"""
        payload = {
            "rating": 4,
            "title": "API Unit Test update",
            "summary": "Some text that contains a Unit Test API Review updated",
        }

        response = self.client.put(self.reviews, payload)
        data = json.loads(response.content)

        self.assertEqual(200, response.status_code)
        self.assertEqual(data.get('rating'), payload.get('rating'))
        self.assertEqual(data.get('title'), payload.get('title'))
        self.assertEqual(data.get('summary'), payload.get('summary'))

    def test_review_delete(self):
        """Test review delete"""
        response = self.client.delete(self.reviews)
        self.assertEqual(204, response.status_code)
