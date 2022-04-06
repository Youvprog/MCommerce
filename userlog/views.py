from django.shortcuts import redirect, render
from .forms import AllFieldsUserCreate, UserCustomer
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.


def UserRegister(request):
    if request.method == 'POST':
        userform = AllFieldsUserCreate(request.POST)
        customerform = UserCustomer(request.POST)
        if userform.is_valid() and customerform.is_valid():
            user = userform.save()
            customer = customerform.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login')
    else:
        userform = AllFieldsUserCreate()
        customerform = UserCustomer()
        return render(request, 'userlog/register_user.html', {
            "form1": userform,
            "form2": customerform
        })


class CustomerLogin(LoginView):
    template_name = "userlog/login_user.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('index')

def index(request):
    return render(request,'userlog/index.html')