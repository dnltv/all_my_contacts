from django.views import generic
from django.shortcuts import render
from .models import DopeUser

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

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри (переменная контекста)
    return render(
        request,
        'index.html',
        context={'num_dope_user': num_dope_user,
                 'num_visible_dope_user': num_visible_dope_user,
                 'num_visits': num_visits,
                 }
    )


class DopeUsersListView(generic.ListView):
    """Generic class-based view for a list of users w/ visible accounts."""
    model = DopeUser
    context_object_name = 'users_list'
    template_name = 'contacts/users_list.html'
    paginate = 10
    paginate_by = 10


class DopeUserDetailView(generic.DetailView):
    model = DopeUser
    context_object_name = 'user'
    paginate = 10





