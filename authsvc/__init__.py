from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from .models import authenticate
from pyramid.security import Allow, Everyone


class RootFactory(object):
    __acl__ = [ 
                (Allow, Everyone, 'everybody')
            ]
    def __init__(self, request):
        pass


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret2', callback=authenticate, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings, root_factory=RootFactory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('test', '/test')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('user', '/user')

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.scan()
    return config.make_wsgi_app()
