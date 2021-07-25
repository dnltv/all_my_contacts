from django.views import generic
from django.shortcuts import render
from .models import DopeUser, SocialMedia, Messengers


# Create your views here.
def index(request):
    """
    View Function for Home (Main) page.
    """
    # Сколько пользователей зарегистрировано в dope на данный момент
    num_dope_user = DopeUser.objects.all().count()
    # Сколько видимых профилей
    num_visible_dope_user = DopeUser.objects.filter(status__exact='v').count()
    # Сколько раз поделились контактами
    # num_share

    # Отрисовка HTML-шаблона index.html с данными внутри (переменная контекста)
    return render(
        request,
        'index.html',
        context={'num_dope_user': num_dope_user,
                 'num_visible_dope_user': num_visible_dope_user,
                 }
    )


class DopeUsersListView(generic.ListView):
    """Generic class-based view for a list of users w/ visible accounts."""
    model = DopeUser
    context_object_name = 'users_list'
    template_name = 'contacts/users_list.html'
    paginate = 10


class DopeUserDetailView(generic.DetailView):
    model = DopeUser
    context_object_name = 'user'
    paginate = 10





