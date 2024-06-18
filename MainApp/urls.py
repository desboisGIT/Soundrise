from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = [
    path('loginAndRegister/', views.loginAndRegister, name='loginAndRegister'),
    path('login_succes/', views.login_succes, name='login_succes'),
    path('explore/', views.explore, name='explore'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('settings/<str:page>/', views.setting, name='setting_view'),
    path('settings/', views.setting, {'page': 'default'}, name='setting'),
    path('profile/<str:user_name>/',views.profile,name='profile'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)