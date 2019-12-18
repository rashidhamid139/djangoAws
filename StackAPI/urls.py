from . import views
from django.urls import path
urlpatterns =[
    path('', views.home, name='home'),
    path('testcookie/', views.cookie_session, name='setcookie'),
    path('deletecookie/', views.cookie_delete, name='deletecookie'),
    path('create/', views.create_session, name='createsession'),
    path('access/', views.access_session1, name='accesssession'),
    # path('post_comment', views.post_comment, name='comment'),
]
