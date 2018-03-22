from api.models.reviews import Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'rating', 'title', \
                  'summary', 'ip_address', 'submission')


class ReviewSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('rating', 'title', 'summary')
