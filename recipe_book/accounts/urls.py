from django.urls import path

from . import views

urlpatterns = [
    # path("login/", views)
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
