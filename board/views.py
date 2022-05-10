from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

# Create your views here.
from django.views.generic import CreateView

from board.forms import BoardForm
from board.models import Board


def home(request):
    return render(request, 'home/base.html')

def home2(request):
    return render(request, 'costomer_service/notice.html')



def register(request):
    if request.method == 'GET':
        boardForm = BoardForm()
        return render(request, 'costomer_service/register.html', {'boardForm':boardForm})
    elif request.method == 'POST':
        boardForm = BoardForm(request.POST)
        if boardForm.is_valid():
            board = boardForm.save(commit=False)
            board.save()
            print('잘됌')
        if not boardForm.is_valid():
            print('안됌')
    return redirect('/costomer_service')


def notice(request):
    posts = Board.objects.all().order_by('-id')
    return render(request, 'costomer_service/costomer_service.html',
                      {'posts': posts})

def read(request, bid):
    post = Board.objects.all( Q(id=bid) )
    return render(request, 'costomer_service/costomer_service.html',
                  {'post': post})


def board_list(request):
    boards= Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {"boards":boards})


from django.shortcuts import render
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def q_index(request):
    # 질문목록출력
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'costomer_service/notice.html', context)

def detail(request, question_id):
    # 질문내용출력
    question = Question.objects.get(id=question_id)
    context = {'question' : question}
    return render(request, 'costomer_service/question_detail.html', context)

# @login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # answer.author = request.user  # 추가한 속성 author 적용
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('board:detail', question_id=question.id), answer.id))
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'cosmomer_service/question_detail.html', context)

def question_create(request):
    #질문등록
    if request.method == 'POST':
        form =QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date =timezone.now()
            question.save()
            return redirect('board:q_index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'costomer_service/question_form.html', context)

