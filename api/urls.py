from django.conf.urls import url
from api.resources.reviews import ReviewList, ReviewDetail

urlpatterns = [
    url(r'^reviews', ReviewList.as_view(), name='list'),
    url(r'^review/(?P<review_id>[0-9]+)$', ReviewDetail.as_view(), name='detail'),
]