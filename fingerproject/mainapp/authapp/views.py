from django.shortcuts import render
from django.http import JsonResponse
from webauthn import generate_registration_options, verify_registration_response
from os import urandom

''' For complete registration, we need to register 3 things with the server:
    1: The relying party (our app) 2. The user 3. The authenticator'''

def generate_registration_options_view(request):
    # Generate registration options using simple Options from https://github.com/duo-labs/py_webauthn/blob/master/examples/registration.py
    simple_registration_options = generate_registration_options(

''' First we have to register our app with the server by assigning two things:
    1. An rp_id, for the server to be able to identify the relying party - our app 
    2. and human-identifyable rp_name for our app '''
    
    rp_id="verbose-funicular-q557xv7wxp734j9p-8000.app.github.dev",
    rp_name="Finger Auth App",

''' Next, we generate a random user_id so the server can identify the user,
    and the username is the human-readable version of this user id
    a 16 bytes random ID, it's like a server-readable username '''

    user_id = urandom(16)
    user_id = user_id
    user_name = request.user.username,
    user_display_name = request.user.get_full_name(),

''' Lastly, we also have to register the authenticator with the server
    Authenticor's attestation process:
    This is how you make sure your authenticator is still legit and hasn't been tampered with
    It has to return a cryptograpic attestation object to the server, as proof of integrity '''
    
''' This is the server asking for the full attestation object by using the DIRECT conveyance method
    Here we set the criteria an authenticator must meet for it to be selected
    It must be a cross-platform(web/roaming) authenticator, as opposed to a platform(in-built)
    the authenticator is also REQUIRED to support resident keys
    Resident keys are a pair of public and private keys that get generated afte successful registration.
    The private resident key is stored on the authenticator,
    acting like a voucher so that the user doesn't always have to reenter their full details from scratch
    While the public resident key is stored on the server '''

    attestation=AttestationConveyancePreference.DIRECT,
    authenticator_selection=AuthenticatorSelectionCriteria(
    authenticator_attachment=AuthenticatorAttachment.CROSS_PLATFORM,
    resident_key=ResidentKeyRequirement.REQUIRED,
    ),

''' We can generate a 16-byte random number for the server to verify the response
    We can also exclude any credentials that have already been registered with the server.
    The server also has to specify the algorithms it supports for the public key '''

    challenge = os.urandom(16),
    exclude_credentials=[
        PublicKeyCredentialDescriptor(id=base64.b64decode(credential.credential_id)),
    ],
    supported_pub_key_algs=[COSEAlgorithmIdentifier.ECDSA_SHA_512],
    timeout=12000,
)

    print(options_to_json(complex_registration_options))

def verify_registration_response_view(request):
    # Registration Response Verification
registration_verification = verify_registration_response(
    # Demonstrating the ability to handle a plain dict version of the WebAuthn response
    credential={
        "id": "ZoIKP1JQvKdrYj1bTUPJ2eTUsbLeFkv-X5xJQNr4k6s",
        "rawId": "ZoIKP1JQvKdrYj1bTUPJ2eTUsbLeFkv-X5xJQNr4k6s",
        "response": {
            "attestationObject": "o2NmbXRkbm9uZWdhdHRTdG10oGhhdXRoRGF0YVkBZ0mWDeWIDoxodDQXD2R2YFuP5K65ooYyx5lc87qDHZdjRQAAAAAAAAAAAAAAAAAAAAAAAAAAACBmggo_UlC8p2tiPVtNQ8nZ5NSxst4WS_5fnElA2viTq6QBAwM5AQAgWQEA31dtHqc70D_h7XHQ6V_nBs3Tscu91kBL7FOw56_VFiaKYRH6Z4KLr4J0S12hFJ_3fBxpKfxyMfK66ZMeAVbOl_wemY4S5Xs4yHSWy21Xm_dgWhLJjZ9R1tjfV49kDPHB_ssdvP7wo3_NmoUPYMgK-edgZ_ehttp_I6hUUCnVaTvn_m76b2j9yEPReSwl-wlGsabYG6INUhTuhSOqG-UpVVQdNJVV7GmIPHCA2cQpJBDZBohT4MBGme_feUgm4sgqVCWzKk6CzIKIz5AIVnspLbu05SulAVnSTB3NxTwCLNJR_9v9oSkvphiNbmQBVQH1tV_psyi9HM1Jtj9VJVKMeyFDAQAB",
            "clientDataJSON": "eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRlIiwiY2hhbGxlbmdlIjoiQ2VUV29nbWcwY2NodWlZdUZydjhEWFhkTVpTSVFSVlpKT2dhX3hheVZWRWNCajBDdzN5NzN5aEQ0RmtHU2UtUnJQNmhQSkpBSW0zTFZpZW40aFhFTGciLCJvcmlnaW4iOiJodHRwOi8vbG9jYWxob3N0OjUwMDAiLCJjcm9zc09yaWdpbiI6ZmFsc2V9",
            "transports": ["internal"],
        },
        "type": "public-key",
        "clientExtensionResults": {},
        "authenticatorAttachment": "platform",
    },
    expected_challenge=base64url_to_bytes(
        "CeTWogmg0cchuiYuFrv8DXXdMZSIQRVZJOga_xayVVEcBj0Cw3y73yhD4FkGSe-RrP6hPJJAIm3LVien4hXELg"
    ),
    expected_origin="http://localhost:5000",
    expected_rp_id="localhost",
    require_user_verification=True,
)

print("\n[Registration Verification - None]")
print(registration_verification)
assert registration_verification.credential_id == base64url_to_bytes(
    "ZoIKP1JQvKdrYj1bTUPJ2eTUsbLeFkv-X5xJQNr4k6s"
)

