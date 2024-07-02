from .views import generate_registration_options_view, verify_registration_response_view

urlpatterns = [
    path("generate-registration-options/", generate_registration_options_view),
    path("verify-registration-response/", verify_registration_response_view),
]
```