# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from api.utils import helpers
from api.exceptions.http import BadGateway
from api.models.reviews import Review
from api.serializers.reviews import ReviewSerializer, ReviewSerializerUpdate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ReviewList(APIView):
    """
    List all reviews, or create a new snippet.
    """

    permission_classes = (IsAuthenticated,)

    def get(self, format=None):
        """Retrieves all reviews by the current authenticated user"""

        review = helpers.get_reviews(self.request.user)
        serializer = ReviewSerializer(review, many=True)

        return Response(serializer.data)

    def post(self, format=None):
        """Creates a new reviews for the current authenticated user"""

        serializer_validation = ReviewSerializerUpdate(data=self.request.data)

        if serializer_validation.is_valid():
            data = self._get_read_only_data()
            data.update(serializer_validation.data)
            new_review = Review(**data).save()

            return Response(new_review, status=status.HTTP_201_CREATED)

        return Response(serializer_validation.errors, status=status.HTTP_400_BAD_REQUEST)

    def _get_ip_address(self):
        """Gets user remote address
        Raises BadGateway exception in case the web server is not forwarding
        the address header
        """
        addr = self.request.META.get('REMOTE_ADDR')

        if addr is not None:
            return addr

        raise BadGateway()

    def _get_read_only_data(self):
        return {'ip_address': self._get_ip_address(),
         'user': helpers.get_user(self.request.user)}


class ReviewDetail(APIView):
    """Review detail API
    Get/Update/Delete a given review entity by its id
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, review_id):
        """Get the review entity by user and review id"""

        user = helpers.get_user(request.user)
        review = helpers.get_review(review_id, user)
        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def put(self, request, review_id):
        """Update the review entity by user and review id"""

        user = helpers.get_user(request.user)
        review = helpers.get_review(review_id, user)
        serializer = ReviewSerializerUpdate(review, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        """Delete a given review entity by user and review id"""

        user = helpers.get_user(request.user)
        review = helpers.get_review(review_id, user)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
