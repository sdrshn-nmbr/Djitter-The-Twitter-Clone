from django.forms import ModelForm
from .models import Room
from  django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants'] # exclude host and participants from form
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']