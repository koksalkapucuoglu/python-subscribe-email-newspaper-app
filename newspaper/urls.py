from django.urls import path

from newspaper import views

urlpatterns = [
    path('', views.EmailSubscribeView.as_view(), name='email-subscribe'),
    path('success/', views.SuccessView.as_view()),
]
