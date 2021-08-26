from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article



class AccountCreateView(CreateView): # view를 만듬
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('accountapp:hello') class와 함수와 불러오는데 차이가 있어서 lazy 사용,클래스에서 주로 사용
    template_name = 'accountapp/create.html' #회원가입페이지 연결방법

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})


class AccountDetailView(DetailView, MultipleObjectMixin):
   model = User
   context_object_name = 'target_user'
   template_name = 'accountapp/detail.html'

   paginate_by = 20

   def get_context_data(self, **kwargs):
       article_list = Article.objects.filter(writer=self.object)
       return super().get_context_data(object_list=article_list,
                                       **kwargs)


has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    # success_url = reverse_lazy('accountapp:detail')
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'



