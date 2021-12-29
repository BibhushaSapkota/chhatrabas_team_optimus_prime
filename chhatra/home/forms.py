from django import forms


from django.contrib.auth import get_user_model

from django.db.models import fields


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm



#User = get_user_model()



# class UserResgistrationForm(forms.ModelForm):

#     confirm_password = forms.CharField(max_length=255,required=True)

#     class Meta:

#         model = User

#         fields = ["hostel_name","location","email","contact_num","password","confirm_password"]

# classSignupForm(UserCreationForm):

#     classMeta:

#         model=User

#         fields= ('hostel_name','location','email','phone_number','password','confirm_password')
