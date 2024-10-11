from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', view=views.viewDashboard),
    path('newpost/', view=views.createPost)
]