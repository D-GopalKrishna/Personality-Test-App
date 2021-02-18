from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers
from .viewsets import QuestionViewset, UserDataViewset, userSelectionViewset


app_name = 'Test'

router = routers.DefaultRouter()
router.register(r'question', QuestionViewset)
# router.register(r'userchoice', UserChoiceViewset)
router.register(r'userdata', UserDataViewset)
# router.register(r'userdatadetail/<uuid:url_key>', UserDataDetailViewset)

router.register(r'userselection', userSelectionViewset)


urlpatterns = [
    # path('', views.HomeView.as_view(), name="index"),
    # path('<uuid:pk>/test/', views.TestView.as_view(), name="test"),
    # path('<uuid:pk>/results/', views.ResultView.as_view(), name="result"),


    # path('', views.HomeView, name="index"),
    # path('test-all/<str:url_key>/', views.TestView1, name="test1"),
    # path('test-one/<str:url_key>/', views.TestView2, name="test2"),
    # path('result/<uuid:url_key>/', views.ResultView, name="result"),

    # api
    path('personality_api/', include(router.urls)),
]