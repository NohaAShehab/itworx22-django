

from django.urls import path
from accounts.views import SignUpView
urlpatterns = [
    path("signup/itworx",SignUpView.as_view(), name='accounts.signup' )
]
