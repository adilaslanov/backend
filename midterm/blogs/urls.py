from django.urls import path
from . import views


urlpatterns = [
    path('blogs/', views.blogs_handler),
    path('blogs/<int:pk>', views.blog_handler),
]

