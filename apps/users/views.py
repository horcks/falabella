from django.shortcuts import render
from django.views.generic import ListView
from apps.users.models import *
from apps.users.forms import *
from apps.users.resources import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.
class Extended_UserListView(ListView):
    model = Extended_User
    template_name = 'users/index.html'
    paginate_by = 20

def registration(request,code=None):
    request.session.flush()
    context = {
        'formExtendUser' : ExtendUserForm(),
        'formUser' : UserForm(),
    }
    if request.method=='POST':  
        updated_request = request.POST.copy()
        new_email=request.POST['email'].lower()
        updated_request.update({'email': new_email, 'username': new_email })
        # formAfiliate = AfiliateForm(updated_request)
        formExtendUser = ExtendUserForm(updated_request)
        formUser = UserForm(updated_request)
        if formExtendUser.is_valid() and formUser.is_valid() :
            user = formUser.save(commit=False)
            user.set_password(formUser.data['new_password'])
            user.save()
            exted = formExtendUser.save(commit=False)
            exted.user_id=user.id
            exted.save()
            usuario = authenticate(username=new_email, password=formUser.data['new_password'])
            if usuario is not None:
                login(request, usuario)
                return redirect('users:index')
            else :
                return redirect('login')
        else :
            context['formUser'] = formUser
            context['formExtendUser'] = formExtendUser

    return render (request,"users/registration.html",context)


def downloadUsers(request):
    dataset = UserExportResource().export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Usuarios.xls"'
    return response