from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from  .forms import RegisterUserForm


# Create your views here.

def loginPage(request):
    if request.method =='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,"wrong password or username,Try again")
            return redirect('login')
            
    context={}
    return render(request,'login_form.html')

def logout_user(request):
    logout(request)
    messages.success(request,"Your were logged out")
    return redirect('home')

# def register(request):

#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request,user)
#             messages.success(request,"regisration was succesful!")
#             return redirect('home')
#         else:
#             form=RegisterUserForm()
    
#     return render(request,'register_user.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  
        
    else:
        form = RegisterUserForm()
    return render(request, 'register_user.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')  
#         else:
#             messages.success(request,'An error occurred during registration')
        
#     else:
#         form = RegisterUserForm()
#     return render(request, 'register_user.html', {'form': form})


def home(request):
    context={}
    return render(request, 'home.html',context)

def test(request):
    return render(request, 'test.html',{})