from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

contacts_urls = [
    path('',
         include('contacts.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token),
] + contacts_urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('contacts/', ContactApiView.as_view()),
# ]
