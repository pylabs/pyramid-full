from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

# database
#from pyramid_sqlalchemy import Session
#from .models import MyModel

# mailer
#from pyramid_mailer.mailer import Mailer
#from pyramid_mailer.message import Message

# auth
#@view_config(route_name='login', renderer='templates/login.jinja2')
#def login_view(request):
#    from pyramid.security import remember
#
#    if request.method == 'POST':
#        # put your auth logic here
#        username = request.POST['username']
#        password = request.POST['password']
#        if username == 'foo' and password == 'bar':
#            headers = remember(request, username)
#            return HTTPFound(location=request.route_path('home'), headers=headers)
#        else:
#            return {'error_message': 'Login failed, please check your username and password.'}
#    else:
#        return {}
#
#
#@view_config(route_name='logout')
#def logout_view(request):
#    from pyramid.security import forget
#
#    headers = forget(request)
#    return HTTPFound(location=request.route_path('home'), headers=headers)

@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {'project': '{{ cookiecutter.project_name }}'}

