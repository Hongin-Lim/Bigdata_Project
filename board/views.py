from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from board.forms import BoardForm
from board.models import Board


def home(request):
    return render(request, 'home/base.html')

def home2(request):
    return render(request, 'home/mainpage.html')



def register(request):
    if request.method == 'GET':
        boardForm = BoardForm()
        return render(request, 'notice/register.html', {'boardForm':boardForm})
    elif request.method == 'POST':
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.save()
            print('잘됌')
        if not boardForm.is_valid():
            print('안됌')
    return redirect('/notice')


def notice(request):
    posts = Board.objects.all().order_by('-id')
    return render(request, 'notice/notice.html',
                      {'posts': posts})

def read(request, bid):
    post = Board.objects.get( Q(id=bid) )
    return render(request, 'notice/notice.html',
                  {'post': post})


def board_list(request):
    boards= Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {"boards":boards})