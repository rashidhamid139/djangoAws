from . import views
from django.urls import path
urlpatterns =[
    path('', views.home, name='home'),
    # path('post_comment', views.post_comment, name='comment'),
]
