from django.urls import path
from first_app.views import IndexView, UserData

urlpatterns = [
    path('', IndexView.as_view()),
    path('userdata', UserData.as_view(), name='UserData'),
]