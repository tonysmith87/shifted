from django.shortcuts import render_to_response, redirect
from contact.models import *
from django.template import RequestContext

from contact.views import login_required
from django.http import HttpResponse
import json
import datetime

from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q


# login view
def login(request):
    error = 'none'

    if 'username' in request.POST:

        # get username and password from request.
        username = request.POST['username']
        password = request.POST['password']

        # get a user from database based on username and password
        user = Person.objects.filter(user_name=username, password=password)

        # check whether the user is in database or not
        if len(user) < 1:
            error = 'block'
        else:
            request.session['user'] = {
                "id": user[0].id,
                "username": user[0].user_name,
                "role": user[0].role
            }

            user[0].last_login = datetime.datetime.now().strftime('%Y-%m-%d')
            user[0].save()
            if user[0].role == 1:
                return redirect("/admin/client-management")
            elif user[0].role == 2:
                return redirect("/admin/meal-view")
            else:
                return redirect("/admin/login/")

    return render_to_response('app_admin/login.html', locals(), context_instance=RequestContext(request))


# logout view
#   initialize session variable
def logout(request):
    request.session['user'] = None
    return redirect("/admin/login")


@login_required(role="admin")
def client_management(request):
    user = request.session['user']

    if request.POST:
        c_type = request.POST['type']
        rate = request.POST['rate']

        if c_type != "-1":
            person = Person.objects.filter(pk=int(c_type), role=2)[0]
        else:
            person = Person()
            person.register_date = datetime.datetime.now().strftime('%Y-%m-%d')

        person.first_name = request.POST['first_name']
        person.email = request.POST['email']
        person.password = request.POST['password']
        person.user_name = request.POST['user_name']
        person.role = 2
        person.save()

        person = Person.objects.filter(user_name=request.POST['user_name'], password=request.POST['password'])[0]

        if c_type != "-1":
            client = Client.objects.filter(person_id=person.id)[0]
        else:
            client = Client()
            client.person_id = person.id

        client.rate = rate
        client.save()

    return render_to_response('app_admin/clientManagement.html', locals(), context_instance=RequestContext(request))


@login_required(role="admin")
def client_list(request):
    role = int(request.GET['role'])
    user = request.session['user']

    clients = Person.objects.filter(role=role)

    rates = dict()
    client_name = dict()
    for client in clients:
        if role == 2:
            rate = Client.objects.filter(person_id=client.id)[0].rate
        else:
            rate = Staff.objects.filter(person_id=client.id)[0].rate
            name = Staff.objects.filter(person_id=client.id)[0].client.person.user_name
            client_name[client] = name

        rates[client] = rate

    if role == 2:
        url = 'app_admin/clientList.html'
    elif role == 3:
        url = 'app_admin/staffList.html'

    return render_to_response(url, locals(), context_instance=RequestContext(request))


@csrf_exempt
@login_required(role="admin")
def delete_client(request):
    user = request.session['user']
    role = 2
    # delete a client
    if request.POST:
        role = int(request.POST['role'])
        email = request.POST['email']
        person = Person.objects.filter(email=email, role=role)
        if role == 2:
            Client.objects.filter(person_id=person[0].id).delete()
        else:
            Staff.objects.filter(person_id=person[0].id).delete()

        person.delete()

    clients = Person.objects.filter(role=role)

    rates = dict()
    client_name = dict()
    for client in clients:
        if role == 2:
            rate = Client.objects.filter(person_id=client.id)[0].rate
        else:
            rate = Staff.objects.filter(person_id=client.id)[0].rate
            name = Staff.objects.filter(person_id=client.id)[0].client.person.user_name
            client_name[client] = name

        rates[client] = rate

    return render_to_response('app_admin/clientList.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
@login_required(role="admin")
def check_client(request):
    type = request.GET['type']
    value = request.GET['value']
    user_id = int(request.GET['user_id'])

    res = dict()

    if type == 'username':  # check only username if it's in database
        if user_id == -1:
            user = Person.objects.filter(user_name=value)
        else:
            user = Person.objects.filter(Q(user_name=value) & ~Q(pk=user_id))
    else:   # check only email if it's in database
        if user_id == -1:
            user = Person.objects.filter(email=value)
        else:
            user = Person.objects.filter(Q(email=value) & ~Q(pk=user_id))

    if len(user) > 0:   # if there is a person who has the username and the password in database
        res['existed'] = True
    else:               # otherwise
        res['existed'] = False

    return HttpResponse(json.dumps(res))


@login_required(role="admin")
def get_client(request):
    role = int(request.GET['role'])
    email = request.GET['email']

    rate = 0
    person = Person.objects.filter(email=email, role=role)[0]
    if role == 2:
        rate = Client.objects.filter(person_id=person.pk)[0].rate
    else:
        rate = Staff.objects.filter(person_id=person.pk)[0].rate

    res = {
        'id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
        'password': person.password,
        'user_name': person.user_name,
        'rate': rate,
    }

    return HttpResponse(json.dumps(res))


@login_required(role="admin")
def staff_management(request):
    user = request.session['user']

    if request.POST:
        c_type = request.POST['type']
        rate = request.POST['rate']

        if c_type != "-1":
            person = Person.objects.filter(pk=int(c_type), role=3)[0]
        else:
            person = Person()
            person.register_date = datetime.datetime.now().strftime('%Y-%m-%d')

        person.first_name = request.POST['first_name']
        person.last_name = request.POST['last_name']
        person.email = request.POST['email']
        person.password = request.POST['password']
        person.user_name = request.POST['user_name']
        person.role = 3
        person.save()

        person = Person.objects.filter(user_name=request.POST['user_name'], password=request.POST['password'])[0]

        if c_type != "-1":
            staff = Staff.objects.filter(person_id=person.id)[0]
        else:
            staff = Staff()
            staff.person_id = person.id

        staff.client_id = (request.POST['client'])
        staff.rate = rate
        staff.save()

    clients = Client.objects.all()

    return render_to_response('app_admin/staffManagement.html', locals(), context_instance=RequestContext(request))


@login_required(role="admin")
def meal_management(request):
    user = request.session['user']

    if request.POST:
        type = int(request.POST['type'])

        # create new meal
        if type == -1:
            meal = Meal()
        else:
            meal = Meal.objects.filter(pk=type)[0]

        meal.name = request.POST['name']
        meal.description = request.POST['description']
        meal.score = 0
        meal.date = request.POST['date']
        meal.price = request.POST['price']
        meal.location = request.POST['location']
        meal.client_id = int(request.POST['client'])

        meal.save()

        # create roster
        staffs = Staff.objects.filter()

        absent_staff = Staff.objects.filter(client_id=int(request.POST['client']))
        staff_ids = [staff.id for staff in absent_staff]

        # create new meal
        if type == -1:
            rosters = Staff.objects.filter(~Q(id__in=staff_ids))

            meal = Meal.objects.filter(name=request.POST['name'], date=request.POST['date'], location=request.POST['location'])[0]
            Roster.objects.filter(meal_id=meal.id).delete()
            for roster in rosters:
                tp_roster = Roster()
                tp_roster.meal_id = meal.id
                tp_roster.staff_id = roster.id
                tp_roster.save()

    clients = Client.objects.all()

    return render_to_response('app_admin/mealManagement.html', locals(), context_instance=RequestContext(request))


@login_required(role="admin")
def meal_list(request):

    user = request.session['user']

    meals = Meal.objects.all()

    return render_to_response("app_admin/mealList.html", locals(), context_instance=RequestContext(request))


@login_required(role="admin")
def get_meal(request):
    id = request.GET['id']

    meal = Meal.objects.filter(pk=id)[0]

    res = {
        'id': meal.id,
        'name': meal.name,
        'description': meal.description,
        'location': meal.location,
        'score': meal.score,
        'price': meal.price,
        'date': meal.date,
        'client_id': meal.client_id
    }

    return HttpResponse(json.dumps(res))

@csrf_exempt
@login_required(role="admin")
def delete_meal(request):
    user = request.session['user']

    # delete a client
    if request.POST:
        id = request.POST['id']

        Roster.objects.filter(meal_id=id).delete()
        Meal.objects.filter(pk=id).delete()

    meals = Meal.objects.all()

    return render_to_response('app_admin/mealList.html', locals(), context_instance=RequestContext(request))

@login_required(role="client")
def roster_management(request):

    user = request.session['user']

    meal_id = int(request.GET['meal_id'])

    return render_to_response('app_admin/rosterManagement.html', locals(), context_instance=RequestContext(request))


@login_required(role="client")
def roster_list(request):
    meal_id = int(request.GET['meal_id'])

    meal = Meal.objects.filter(pk=meal_id)
    rosters = Roster.objects.filter(meal_id=meal_id)

    return render_to_response('app_admin/rosterList.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
@login_required(role="client")
def delete_roster(request):
    id = int(request.POST['id'])
    meal_id = int(request.POST['meal_id'])

    Roster.objects.filter(pk=id).delete()

    meal = Meal.objects.filter(pk=meal_id)
    rosters = Roster.objects.filter(meal_id=meal_id)

    return render_to_response('app_admin/rosterList.html', locals(), context_instance=RequestContext(request))


@login_required(role="client")
def meal_view(request):
    user = request.session['user']

    meals = Meal.objects.filter(client_id=user['id'])

    return render_to_response("app_admin/client/mealManagement.html", locals(), context_instance=RequestContext(request))


@login_required(role="client")
def send_comment(request):
    meal_id = request.GET['meal_id']
    comment = request.GET['comment']

    meal = Meal.objects.filter(pk=meal_id)[0]
    meal.meal_comment = comment
    meal.save()

    return render_to_response("app_admin/client/mealManagement.html", locals(), context_instance=RequestContext(request))


@login_required(role="client")
def client_profile(request):
    user = request.session['user']

    client = Client.objects.filter(person_id=user['id'])[0]

    return render_to_response("app_admin/client/profile.html", locals(), context_instance=RequestContext(request))


@login_required(role="client")
def staff_list(request):
    user = request.session['user']

    clients = Staff.objects.filter(client=user['id'])

    return render_to_response("app_admin/client/staffList.html", locals(), context_instance=RequestContext(request))


def register_staff(request):
    clients = Client.objects.all()

    return render_to_response("app_admin/client/registerStaff.html", locals(), context_instance=RequestContext(request))