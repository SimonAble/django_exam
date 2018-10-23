from django.shortcuts import render, HttpResponse, redirect

from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

#<<--------------INDEX HTML-------------->>
def index(request):
    print("\n<<-----------------INDEX HTML----------------->>\n")

    return render(request, 'mainApp/index.html')


#<<--------------NEW USER POST-------------->>
def new_user(request):
    print("\n<<-----------------NEW USER POST----------------->>\n")
    print(request.POST)

    #VALIDATIONS----------------->>
    errors = User.objects.registration_validator(request.POST)


    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        print(errors)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        #Create password hash
        hash_brown = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        
        #Create the user
        user = User.objects.create(name = request.POST['name'], username = request.POST['username'],password = hash_brown)

        #store user info in session
        request.session['id'] = user.id
        request.session['username']=user.username
        request.session['name']=user.name

        return redirect('/user_dash')


#<<-------------LOGIN POST-------------->>
def login(request):
    print("\n<<-----------------LOGIN POST----------------->>\n")
    print("LOGIN REQUEST EXECUTED")
    print(request.POST)

    #VALIDATIONS----------------->>
    errors = User.objects.login_validator(request.POST)
    print(errors)

    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        print(errors)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        user = User.objects.get(username=request.POST['username'])

        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("password match")
            request.session['id'] = user.id
            request.session['username']=user.username
            request.session['name']=user.name
            return redirect('/user_dash')
        else:
            print("failed password")
            messages.error(request, "Wrong password")

            return redirect('/')

#<<--------------USER LOGOUT-------------->>
def logout(request):
    print("\n<<-----------------LOGING OUT USER----------------->>\n")
    request.session.clear()
    return redirect('/')


#<<--------------USER DASH HTML-------------->>
def user_dash(request):
    print("\n<<-----------------DISPLAYING USER DASH----------------->>\n")

    if not request.session:
        return redirect('/')

    else:
        all_items = Item.objects.all()

        my_items = Item.objects.filter(added_by_id=request.session['id'])

        user_favorite = Favorite.objects.filter(user_id=request.session['id'])

        for i in user_favorite:
            all_items=all_items.exclude(id=i.item_id)
        
        all_items=all_items.exclude(added_by_id=request.session['id'])

        context = {
            "my_items":my_items,
            "all_items":all_items,
            "user_favorite" : user_favorite
        }

        return render(request, 'mainApp/user_dash.html',context)


#<<--------------ADD ITEM HTML-------------->>
def add_item(request):
    print("\n<<-----------------ADD ITEM----------------->>\n")
    return render(request, "mainApp/add_item.html")


#<<-------------ADD ITEM POST REDIRECT------------->>
def create_item(request):
    print("\n<<-----------------ADD ITEM POST----------------->>\n")
    print("PRINTING ADD ITEM POST: ", request.POST)

    #VALIDATIONS----------------->>
    errors = Item.objects.item_validator(request.POST)
    print(errors)

    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        print(errors)
        # redirect the user back to the form to fix the errors
        return redirect('/add_item')
    else:
        Item.objects.create(name=request.POST['name'],description=request.POST['desc'],added_by_id=request.session['id'])

        return redirect('/user_dash')

#<<-------------REMOVE ITEM------------->>
def remove_item(request, item_id):

    if Item.objects.filter(id=item_id):
        Item.objects.get(id=item_id).delete()

    if Favorite.objects.filter(item_id=item_id):
        Favorite.objects.get(item_id=item_id).delete()

    return redirect('/user_dash')

#<<-------------FAVORITE ITEM------------->>
def join_item(request, item_id):
    Favorite.objects.create(item_id=item_id,user_id=request.session['id'])
    print(item_id)
    return redirect('/user_dash')

def unjoin_item(request, item_id):
    if Favorite.objects.filter(item_id=item_id):
        Favorite.objects.filter(item_id=item_id).delete()
    return redirect( "/user_dash")

#<<-------------SHOW ITEM------------->>
def show(request, item_id):
    this_item = Item.objects.get(id=item_id)
    item_favs = Favorite.objects.filter(item_id = item_id)

    item_favs = item_favs.exclude(user_id = request.session['id'])

    
    context = {
        "this_item":this_item,
        "item_favs":item_favs
    }

    return render(request, 'mainApp/show.html',context)