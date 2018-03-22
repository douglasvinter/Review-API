from django.http import Http404
from api.models.reviews import Review
from django.contrib.auth.models import User


def get_reviews(user):
    """Helper method to return a list of reviews by user"""
    try:
        user = get_user(user)
        return Review.objects.filter(user=user)
    except Review.DoesNotExist:
        raise Http404


def get_review(review_id, user):
    """Helper method to return a review entity by its id"""
    try:
        return Review.objects.get(id=review_id, user=user)
    except Review.DoesNotExist:
        raise Http404


def get_user(user_name):
    """Helper method to get authenticated user name"""
    try:
        return User.objects.get(username=user_name)
    except User.DoesNotExist:
        raise Http404