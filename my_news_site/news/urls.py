from django.urls import path

from . import views

urlpatterns = [
    path('', views.last_news, name='home'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('all_news/', views.index, name='all_news'),
    path('news/<int:new_id>/', views.view_news, name='view_new'),
    path('news/add_new/', views.add_news, name='add_news'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

