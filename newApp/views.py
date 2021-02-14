from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "home.html"


# User 생성
class UserCreateView(CreateView):
    template_name = "registration/resgister.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("resgister_done")


class UserCreateDoneTV(TemplateView):
    template_name = "registration/resgister_done.html"
