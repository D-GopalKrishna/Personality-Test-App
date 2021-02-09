from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HomeView.as_view(), name="index"),
    # path('<uuid:pk>/test/', views.TestView.as_view(), name="test"),
    # path('<uuid:pk>/results/', views.ResultView.as_view(), name="result"),

    path('', views.HomeView, name="index"),
    path('test/<uuid:url_key>/', views.TestView, name="test"),
    path('result/<uuid:url_key>/', views.ResultView, name="result"),

    # path('personality_api/', )

]