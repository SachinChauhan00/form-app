from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('Edit-Student/',views.edit_student,name="edit"),
]
