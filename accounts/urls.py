from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change-pass/', change_pass_view, name='change-pass'),
    path('reset/', reset_pass, name='reset'),
    path('reset2/', reset_pass2, name='reset2'),
    path('profile/update/', profile_update_view, name='profile-update'),

]