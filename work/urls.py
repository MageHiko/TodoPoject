from django.urls import path
from work import views

urlpatterns = [
    path('works/', views.WorkView.as_view(), name = "works")
]