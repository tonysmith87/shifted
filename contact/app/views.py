from django.shortcuts import render_to_response, redirect
from contact.models import *
from django.template import RequestContext


# login view
def login(request):
    error = 'none'

    if 'username' in request.POST:

        # get username and password from request.
        username = request.POST['username']
        password = request.POST['password']

        # get a user from database based on username and password
        user = Person.objects.filter(username=username, password=password)

        # check whether the user is in database or not
        if len(user) < 1:
            error = 'block'
        else:
            request.session['user'] = {
                "id": user[0].id,
                "username": user[0].username,
            }

            return redirect("/manage-battle")

    return render_to_response('login.html', {'error':error}, context_instance=RequestContext(request))


# logout view
#   initialize session variable
def logout(request):
    request.session['user'] = None
    return redirect("/login")
