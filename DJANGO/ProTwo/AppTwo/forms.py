from django.forms import ModelForm
from AppTwo.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
