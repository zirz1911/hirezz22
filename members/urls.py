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

    path('addPost', views.addPost, name='addPost'),
    path('<myUser>/updatePost', views.updatePost, name='updatePost'),
    path('<myUser>/deletePost', views.deletePost, name='deletePost'),
    path('postPage', views.postPage, name='postPage'),
    path('search_post', views.search_post, name='search_post'),
    path('<myUser>/selectPost', views.selectPost, name='selectPost'),
    path('userProfileShow', views.userProfileShow, name='userProfileShow'),

    path('freelanceProfileShow', views.freelanceProfileShow, name='freelanceProfileShow'),
    path('myPost', views.myPost, name='myPost'),
    path('addFreelancer', views.addFreelancer, name='addFreelancer'),
    path('<myUser>/selectFreelancer', views.selectFreelancer, name='selectFreelancer'),
    path('<myUser>/updateFreelancer', views.updateFreelancer, name='FreelancerUpdate'),
    path('<myUser>/deleteFreelancerProfile', views.deleteFreelancerProfile, name='deleteFreelancerProfile'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)