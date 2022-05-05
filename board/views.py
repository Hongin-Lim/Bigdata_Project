from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from board.forms import BoardForm


def home(request):
    return render(request, 'home/base.html')

def home2(request):
    return render(request, 'home/mainpage.html')

def notice(request):
    return render(request, 'notice/notice.html')

def register(request):
    if request.method == 'GET':
        boardForm = BoardForm()
        return render(request, 'notice/register.html', {'boardForm':boardForm})
    elif request.method == 'POST':
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.save()
            return redirect('/register')