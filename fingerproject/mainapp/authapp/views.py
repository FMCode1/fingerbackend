from django.shortcuts import render

# views.py

from django.http import JsonResponse
from webauthn import generate_registration_options, verify_registration_response

def generate_registration_options_view(request):
    """
    Generates registration options for a new authenticator.
    """
    # Your logic to retrieve user data (e.g., username) goes here
    user_id = request.user.id  # Example: Get the user ID

    # Generate registration options using simple Options from https://github.com/duo-labs/py_webauthn/blob/master/examples/registration.py
    simple_registration_options = generate_registration_options(
    # server-identifyable name for our app
    rp_id="verbose-funicular-q557xv7wxp734j9p-8000.app.github.dev",
    # human-identifyable name for our app
    rp_name="Finger Auth App",

    default_user_name="user123",
    default_user_display_name="User123",

    if user_name == "":
        user_name = default_user_name

    if user_display_name == "":
        user_display_name = default_user_display_name
)

    return JsonResponse(registration_options)

def verify_registration_response_view(request):
    """
    Verifies the registration response from the client.
    """
    # Your logic to handle the registration response goes here
    registration_response = request.POST.get("registration_response")  # Example

    # Verify the response
    try:
        verify_registration_response(registration_response)
        # Registration successful! Associate the authenticator with the user.
        return JsonResponse({"message": "Registration successful"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

