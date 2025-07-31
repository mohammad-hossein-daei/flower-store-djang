from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="شماره تلفن شما باید در این قالب باشد.'+989876543211'"
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    address = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    
    def __str__(self):
        return f'Profile {self.user.username}'
    