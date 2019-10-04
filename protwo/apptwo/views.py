from django.shortcuts import render
from django.http import HttpResponse
#from apptwo.models import User
from apptwo.forms import MyForm

def index(request):
	return render(request,'apptwo/index.html')
def help(request):
	return render(request,'apptwo/help.html')

def user(request):
	# users_list=User.objects.order_by('Fname')
	# name_dict={'users':users_list}
	# return render(request,'apptwo/users.html',context=name_dict)
	form = MyForm()
	if request.method == "POST":
		form = MyForm(request.POST)
		if form.is_valid:
			form.save(commit=True)
			return index(request)
	return render(request,'apptwo/users.html',{'form':form})
# Create your views here.
