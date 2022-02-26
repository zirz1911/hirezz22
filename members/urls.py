from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('workList', views.workList, name='workList'),
    path('addPost', views.addPost, name='addPost'),
    path('postPage', views.postPage, name='postPage'),
    path('<p_id>/selectPost', views.selectPost, name='selectPost'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)