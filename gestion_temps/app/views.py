from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'acceuil.html',{})
def about(request):
    return render(request, 'a_propos.html',{})
def videos(request):
    return render(request, 'videos.html', {})
def connexion(request):
    logout(request)
    return redirect('login_in')
def index(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repeat_password = request.POST.get('repassword', None)
        
        try:
            validate_email(email)
        except:
            error = True
            message = "Entrer un email valide svp"

        if error == False:
            if password == repeat_password:
                error = True
                message = "Les deux mots de passe ne correspondent pas! "
        
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Cet utilisateur {name} ou le mail {email} existe déjà! "
        
        if error == False:
            user = User(
                username= name,
                email= email,
            )
            user.save()
            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('login')


            #print("=="*5, "NEW POST: ",name,email,password,repeat_password,  "=="*5)


        

    context = {
            'error': error,
            'message': message
        }
    return render(request, 'index.html', context)

@login_required(login_url='login_in')
def table(request):
    return render(request, 'tables_l1.html', {})

def login_in(request):

    if request.method == 'POST':
        email = request.POST.get('email',None)
        password = request.POST.get('password', None)
        
        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('table')
            else:
                print("Mots de passe incorrecte")
        else:
            print("L'utilisateur n'existe pas")

        print("=="*5, "NEW POST: ",email,password,  "=="*5)
    return render(request, 'login.html', {})
def update(request):
    return render(request, 'update_password.html', {})
def forgot(request):
    return render(request, 'forgot_password_copy.html', {})
def admin(request):
    return render(request, 'admin.html', {})

