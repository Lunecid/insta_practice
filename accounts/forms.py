from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class CustomUserCreationform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','profile_image', )
                                                                
                            
class CustomAuthenticationForm(AuthenticationForm):
    pass