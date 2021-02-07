from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HomeView.as_view(), name="index"),
    # path('<uuid:pk>/test/', views.TestView.as_view(), name="test"),
    # path('<uuid:pk>/results/', views.ResultView.as_view(), name="result"),

    path('', views.HomeView, name="index"),
    path('<uuid:pk>/test/', views.TestView, name="test"),
    path('<uuid:pk>/results/', views.ResultView, name="result"),
]