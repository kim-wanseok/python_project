from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer

# Create your views here.

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    answer_list = Answer.objects.all()
    context = {'question_list': question_list, 'answer_list': answer_list}
    return render(request, 'pybo/question_list.html', context)
    # return HttpResponse('안녕하세요 학습 동아리 게시판 입니다.')