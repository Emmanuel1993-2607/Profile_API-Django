from django.urls import path

from Profiles.Profile_api import views


urlpatterns = [
    path('Hello-view/', views.HelloApiview.as_view()),
]