from django.contrib.auth.views import LoginView
from django.urls import path

from accountapp.views import hello, AccountCreateView, AccountDetailView, AccountUpdateView

app_name='accountapp'


urlpatterns = [
    path('hello/', hello, name = 'hello'),

    path('login/', LoginView.as_view(template_name = 'accountapp/login.html')
         , name='login'),
    path('logout/', LoginView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail'),

    path('update/<int:pk>',AccountUpdateView.as_view(),name='update'),
]

