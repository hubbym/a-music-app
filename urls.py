from django.urls import path
 
from django.contrib.auth import views as auth_views 

from . import views 

app_name = 'music'

urlpatterns = [
    path('',views.home , name = 'home'),
    path('register/' , views.register , name= 'register'),
    path('login/' , views.loginPage , name = 'login'),
    path('logout/' , views.logoutUser , name = 'logout'),
  
    path("password-reset", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

  
    path('addAlbum/' , views.addAlbum , name= 'addAlbum'),
    path('updateAlbum/<str:album_id>/' , views.updateAlbum , name= 'updateAlbum'),
    path('<str:album_id>/' , views.detail , name= 'detail'),
    path('deleteAlbum/<str:album_id>/' , views.deleteAlbum , name= 'deleteAlbum'),

    path('<str:album_id>/favorite' , views.favorite , name= 'favorite'),
     
    ]