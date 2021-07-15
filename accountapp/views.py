from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.models import HelloWorld


def hello(request):
    if request.method =='POST':

        temp = request.POST.get("hello_world_input")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello'))
    # redirect to - 어디로 재연결할건지 , reverse -역추적을통해 위치를 알려줌.

    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView): # view를 만듬
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello') # class와 함수와 불러오는데 차이가 있어서 lazy 사용,클래스에서 주로 사용
    template_name = 'accountapp/create.html' #회원가입페이지 연결방법


class AccountDetailView(DetailView):
   model = User
   context_object_name = 'target_user'
   template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/update.html'


