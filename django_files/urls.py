from apps.user.views import LoginCustomView
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', LoginCustomView.as_view()),
    path('users/', include('apps.user.urls')),
    path('profiles/', include('apps.custom_profile.urls'))
]
