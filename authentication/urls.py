from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.RegisterFunc, name = "user_link" ),
    path('login/', views.LoginFunc, name = "login_link" ),
    path('profile/', views.ProfileFunc, name = "profile_link" ),
    path('addprofile/', views.AddProfileFunc, name = "Addprofile_link" ),
    path('updateprofile/', views.UpdateProfileFunc, name = "profileUpdate_link" ),
    path('update_image/', views.UpdateImageFunc, name = "update_image_link" ),
    path('logout/', views.LogoutFunc, name = "logout_link" ),
]

  