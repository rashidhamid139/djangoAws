from . import views
from django.urls import path
urlpatterns =[
    # path('', views.home, name='home'),
    path('create/', views.create_session, name='createsession'),
    path('', views.access_session1, name='accesssession'),
    path('delete', views.delete_session, name='delete'),
]
