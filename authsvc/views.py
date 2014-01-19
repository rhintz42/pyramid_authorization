from pyramid.view import view_config

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )


@view_config(route_name='home', renderer='json')
def my_view(request):
    return  {
                'status': 0,
                'data': {'content': 'Cool Man Luke'}
            }

@view_config(route_name='test', renderer='json')
def this_is_a_test(request):
    return  {
                'status': 0,
                'data': {'content': 'Test Route'}
            }

@view_config(route_name='login', renderer='json')
def login(request):
    login = 'rhintz42'
    password = 'CoolManLuke'
    headers = remember(request, login)
    from pyramid.httpexceptions import HTTPFound
    from pyramid.url import route_url
    return HTTPFound(location=route_url('user', request), headers=headers)
    #import pdb;pdb.set_trace()
    #return  {
    #            'status': 0,
    #            'data': {'content': 'You are Now Logged In'}
    #        }

@view_config(route_name='logout', renderer='json')
def logout(request):
    headers = forget(request)
    a = authenticated_userid(request)
    import pdb;pdb.set_trace()
    
    return  {
                'status': 0,
                'data': {'content': 'You are Now Logged Out'}
            }

@view_config(route_name='user', renderer='json')
def user(request):
    a = authenticated_userid(request)
    import pdb;pdb.set_trace()
    return  {
                'status': 0,
                'data': {'content': 'This User is Signed In: '}
            }
