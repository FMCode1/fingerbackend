from django.urls import path
from .views import *


urlpatterns = [
    path("", home),
    path("generate-registration-options/", generate_registration_options_view),
    path("verify-registration-response/", verify_registration_response_view), 
]
```