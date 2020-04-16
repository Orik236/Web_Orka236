from django.contrib import admin
from django.urls import path, include
from api import views, views_generic

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('api/companies/', views_generic.CompanyListAPIView.as_view()),
    path('api/companies/<int:pk>', views_generic.CompanyDetailAPIView.as_view()),
    path('api/companies/<int:id>/vacancies/', views.company_vacancies),
    path('api/vacancies/', views_generic.VacancyListAPIView.as_view()),
    path('api/vacancies/<int:pk>', views_generic.VacancyDetailAPIView.as_view()),
    path('api/vacancies/top_ten/', views.top_ten_vacancy)
]
