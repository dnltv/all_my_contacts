from django.views import generic
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import DopeUser, CustomUser
from .forms import CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EditDopeUserModelForm, DopeUserForm, SocialMediaForm

# Create your views here.

def index(request):
    """
    View Function for Home (Main) page.
    """
    return render(
        request,
        'index.html'
    )

#def index(request):
    #"""
    #View Function for Home (Main) page.
    #"""
    # Сколько пользователей зарегистрировано в dope на данный момент
    #num_dope_user = DopeUser.objects.all().count()
    # Сколько видимых профилей
    #num_visible_dope_user = DopeUser.objects.filter(status__exact='v').count()
    # Сколько раз поделились контактами
    # num_share

    #num_visits = request.session.get('num_visits', 0)
    #request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри (переменная контекста)
    #return render(
        #request,
        #'index.html',
        #context={'num_dope_user': num_dope_user,
                 #'num_visible_dope_user': num_visible_dope_user,
                 #'num_visits': num_visits,
                 #}
    #)


class DopeUsersListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view for a list of users w/ visible accounts.
    """
    model = DopeUser
    context_object_name = 'users_list'
    template_name = 'contacts/users_list.html'
    paginate = 10
    paginate_by = 10


class DopeUserDetailView(generic.DetailView):
    """
    Generic class-based view for all info, accounts and links of user.
    """
    model = DopeUser
    context_object_name = 'user_detail'


class UpdateDopeUserView(LoginRequiredMixin, generic.UpdateView):
    model = DopeUser
    form = EditDopeUserModelForm
    fields = ['first_name', 'last_name', 'date_of_birth', 'description', 'photo', 'status']
    context_object_name = 'user_detail'
    template_name = 'contacts/edit2.html'

    def get_object(self):
        return self.request.user.dopeuser

    #def get_absolute_url(self):
        #return reverse('edit', args=[self])


def update(request):

    if request.method == 'POST':
        dope_user_form = DopeUserForm(request.POST)
        social_media_form = SocialMediaForm(request.POST)

        if dope_user_form.is_valid() and social_media_form.is_valid():
            dope_user_form.save()
            social_media_form.save()

    else:
        dope_user_form = DopeUserDetailView
        social_media_form = SocialMediaForm

    return render(
        request,
        'contacts/edit3.html',
        context={
            'dope_user_form': dope_user_form,
            'social_media_form': social_media_form,
        }
    )


class SettingAccount(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form = CustomUserChangeForm
    fields = ['email', 'first_name']
    template_name = 'contacts/settings.html'

    def get_object(self):
        return self.request.user

    def get_absolute_url(self):
        return reverse('settings', args=[self])


# test for front from prev project
def profile(request):

    return render(
        request,
        'contacts/loginpage.html',

    )


def start(request):

    return render(
        request,
        'contacts/start.html',
    )


def log(request):

    return render(
        request,
        'contacts/log.html'
    )
