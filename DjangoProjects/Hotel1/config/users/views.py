from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, update_session_auth_hash



def sign_up(request):
  error = False
  if request.method=='POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('sign_in')
    error = True

  form = SignUpForm()
  return render(request, 'sign_up.html', {'form':form, 'error':error})



def sign_in(request):
  if request.method=='POST':
    form = SignInForm(data = request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('home')

  form = SignInForm()
  return render(request, 'sign_in.html', {'form':form})



def sign_out(request):
  logout(request)
  return redirect('sign_in')





def edit_profile(request):
  error = False
  form = EditProfile(request.POST, instance=request.user)
  if request.method=='POST':
    if form.is_valid():
      form.save()
      return redirect('home')
    error = True

  form = EditProfile(instance=request.user)
  return render(request, 'edit_profile.html', {'form':form, 'error':error})



def reset_password(request):
  error = False
  form = ChangePasswordForm(request.user, request.POST)
  if request.method=='POST':
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      return redirect('sign_in')
    error = True
  form = ChangePasswordForm(request.user)
  return render(request, 'reset_password.html', {'form':form, 'error':error})





