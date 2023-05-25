from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    # title = 'Store - Авторизация'


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('products:products'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Store - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'
    # title = 'Store - Регистрация'


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
