from django.urls import path
from Blog import views
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login,name='login'),
    path('posts/', views.posts,name='posts'),
    path('post/', views.post,name='post'),
    path('add_education/', views.add_education,name='add-education'),
    path('add_experience/', views.add_experience,name='add-experience'),
    path('create-profile/', views.create_profile,name='create-profile'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('profiles/', views.profiles,name='profiles'),
    path('profile/', views.profile,name='profile'),
    path('register/', views.register,name='register'),
]