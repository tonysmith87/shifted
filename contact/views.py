from django.shortcuts import redirect

from functools import wraps


# Login Required decorator
def login_required(role):
    def login_decorator(function):
        @wraps(function)
        def wrapped_function(request):

            authentication = {"admin": 1, "client": 2, "staff": 3}
            # if a user is not authorized, redirect to login page
            if 'user' not in request.session or request.session['user'] is None:
                return redirect("/admin/login/")
            # otherwise, go on the request
            else:
                # if the user doesn't have enough permission.
                if request.session['user']['role'] > authentication[role]:
                    request.session['user'] = None
                    return redirect("/admin/login/")

            return function(request)

        return wrapped_function

    return login_decorator
