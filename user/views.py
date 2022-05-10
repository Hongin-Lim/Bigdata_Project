# from django.contrib import auth
# from django.contrib.auth import login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
#
#
# # Create your views here.
# def signup(request):
#     global now_user
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                                             username=request.POST['username'],
#                                             password=request.POST['password1'],
#                                             email=str(now_user),
#                                             first_name=request.POST['first_name'],)
#             auth.login(request, user)
#             return redirect('/user/login')
#         return render(request, 'user/signup.html')
#     return render(request, 'user/signup.html', {'now_user' : now_user})
#
# def userlogin(request):
#     if request.method == "GET":
#         loginForm = AuthenticationForm()
#         return render(request, 'user/login.html', {'loginForm': loginForm})
#     elif request.method == "POST":
#         loginForm = AuthenticationForm(request, request.POST)
#         if loginForm.is_valid():
#             login(request, loginForm.get_user())
#             return render(request, 'main_post/main_post.html')
#         else:
#             return redirect('/user/login')
#
# def userlogout(request):
#     logout(request)
#     return redirect('/user/login')