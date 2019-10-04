from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import WebPage,Topic,AccessRecord
from . import forms

def index(request):
	webpages_list=AccessRecord.objects.order_by('date')
	date_dict={'access_records':webpages_list}
	return render(request,'first_app/index.html',context=date_dict)

def form_name_view(request):
	form=forms.FormName()

	if(request.method == 'POST' ):
		form=forms.FormName(request.POST)
		if(form.is_valid()):
			print("VALIDATION SUCCESS!")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['Email'])
			print("Text: "+form.cleaned_data['text'])

	return render(request,'first_app/form_page.html',{'form':form})
# Create your views here.
def test1(request):
	return render(request,'first_app/test1.html')
def test2(request):
	return render(request,'first_app/test2.html')
