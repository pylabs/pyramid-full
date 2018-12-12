from pyramid.config import Configurator
from pyramid.security import unauthenticated_userid
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .security import group_finder


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    authn_policy = AuthTktAuthenticationPolicy(settings['secret_key'],
                                               timeout=86400,
                                               callback=group_finder)
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          root_factory='.resources.RootFactory',
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy)

    def get_user(request):
        return unauthenticated_userid(request)

    config.add_request_method(get_user, 'user', reify=True)

    # using jinja2 as default template engine
    config.include('pyramid_jinja2')

    # pyramid_beaker as session backend
    config.include('pyramid_beaker')

    # transaction manager settings, used by pyramid_sqlalchemy and
    # pyramid_mailer
    # config.include('pyramid_tm')

    # database settings
    # config.include('pyramid_sqlalchemy')

    # mailer settings
    # config.include('pyramid_mailer')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('login', '/login')
    # config.add_route('logout', '/logout')

    config.scan()
    return config.make_wsgi_app()
