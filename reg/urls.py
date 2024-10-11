from django.urls import path, include
from . import views

urlpatterns = [
    path('', view=views.loginUser),

    path('signup/', view=views.registerUser, name='signup'),
    path('login/', view = views.loginUser, name='login'),

    path('loginS/', view=views.loginSuccess),
    path('loginF/', view=views.loginFailed),

    path('signupS/', view=views.signupSuccess),
    path('signupF/', view=views.signupFailed),
    
]
