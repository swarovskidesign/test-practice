from django.urls import path
from .views import Registration, Authbynick, Authbyacc, PersonalPage, Llogout, Setting

app_name = 'usermanage'

urlpatterns = [
    path('registration/', Registration.as_view(), name='rega'),
    path('auth0/', Authbynick.as_view(), name='authbynick'),
    path('auth1/', Authbyacc.as_view(), name='authbyaccount'),
    path('logout/', Llogout.as_view(), name='logout'),
    path('profile/<uuid:token>/', PersonalPage.as_view(), name='profile'),
    path('setting/<uuid:token>/', Setting.as_view(), name='setting'),
]