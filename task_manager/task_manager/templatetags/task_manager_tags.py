from django import template

register = template.Library()


@register.inclusion_tag('task_manager/navbar.html')
def task_manager_navbar(is_authenticated=False):
    tabs_ = [{
        'url': '/users/',
        'title': 'Users',
        'position': 'left'
    }]

    if is_authenticated:
        tabs_.append({
            'url': '/logout/',
            'title': 'Logout',
            'position': 'right'
        })
    else:
        tabs_.append({
            'url': '/login/',
            'title': 'Log in',
            'position': 'right'
        })
        tabs_.append({
            'url': '/users/create/',
            'title': 'Register',
            'position': 'right'
        })

    return {'tabs': tabs_}
