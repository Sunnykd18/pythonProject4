from learning.views import home_view, registration_view
from django.urls import path

urlpatterns = [
    path('', home_view, name="home"),
    path('register/', registration_view, name="register")

]
