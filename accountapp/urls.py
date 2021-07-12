from django.urls import path

from accountapp.views import hello, AccountCreateView

app_name='accountapp'


urlpatterns = [
    path('hello/',hello, name = 'hello'),

    path('Create/', AccountCreateView.as_view(), name = 'Create')
]

