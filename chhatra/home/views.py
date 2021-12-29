from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls.conf import include
#from home.forms import UserResgistrationForm
#from .forms import SignupForm
# Create your views here.
# User = get_user_model()
# def register(request):

#     if request.method == 'POST':

#         form= SignupForm(request.POST)

#         if form.is_valid():

#             user= form.save()

#             Profile.objects.create(user=user,hostelname=user.hostel_name,location=user.location,email=user.email, phonenumber=user.phone_number,password=user.password)

#             messages.add_message(request, messages.SUCCESS, "User has been created successfully!")

#             return redirect('/Login1')

#         else:

#             messages.add_message(request, messages.ERROR, "Failed to create an account, Check carefully and Try Again!")

#             return render(request, 'home/registrationhostel.html', {'form': form})



#     form= SignupForm

#     context= {

#         'form': form

#         }
#     return render(request, 'home/registrationhostel.html', context)

def index(request):
    return render(request, 'index.html')

def registration1(request):
    return render(request,'registration1.html')

def registration(request):
    return render( request, 'registrationhostel.html')
    # print("error here")
    # form = UserResgistrationForm()

    # if request.method =='POST':

    #     form = UserResgistrationForm(request.POST)

    #     if form.is_valid():

    #         print("done")

    #         hostel_name = form.cleaned_data.get('hostel_name')

    #         location = form.cleaned_data.get('location')

    #         email = form.cleaned_data.get('email')

    #         contact_num = form.cleaned_data.get('contact_num')

    #         password = form.cleaned_data.get('password')

    #         user = User.objects.create_user(username='username',

    #                              hostel_name=hostel_name,

    #                              location=location,

    #                              email=email,

    #                              contact_num=contact_num,

    #                              password=password)
    #         messages.success(request,f'Hi {hostel_name},your account was created succesfully ')
    #         user.save()

    # context = {
    #     "form": form

    # }


#    if request.method=="POST":
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             Hostelname=form.cleaned_data.get('Hostel name')
#             email=form.cleaned_data.get('email')
#             messages.success(request,f'Hi {Hostelname},your account was created succesfully ')
#             return redirect ('Login1.html')

def login(request):
    return render(request,'Login1.html')
