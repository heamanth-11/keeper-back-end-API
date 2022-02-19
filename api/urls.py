from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('api/',views.getApi, name='api'),
path('addnote',views.addNote, name='addNote'),
path('deletenote',views.deleteNote, name='deleteNote'),
path('updatenote',views.updateNote, name='updateNote')
]
