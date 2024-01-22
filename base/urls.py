from django.urls import path
from . import views

urlpatterns = [
    # name parameter is sorta like id so we dont have to hardcode the url in files
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    path('', views.home, name='home'), 
    path('room/<str:pk>', views.room, name='room'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
    
    path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
    
    path('random_room/', views.random_room, name='random_room'),
]