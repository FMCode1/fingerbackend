from django.db import models
from django.contrib.auth.models import User

class WebAuthnRegForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='webauthn_credentials')
    credential_id = models.CharField(max_length=200, unique=True)
    public_key = models.TextField()
    sign_count = models.IntegerField(default=0)
    rp_id = models.CharField(max_length=253)  # Relying Party ID
    # You can also store other information as needed, such as the attestation format or AAGUID
    # These fields are optional and depend on your specific requirements
    attestation_format = models.CharField(max_length=50, blank=True, null=True)
    aaguid = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s credential {self.credential_id}"