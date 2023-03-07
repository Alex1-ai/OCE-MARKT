from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('reviewForm/', views.reviewForm, name='reviewForm'),
    # path("review/", views.review, name="review")
]
