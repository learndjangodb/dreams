from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from .models import DreamReal
import datetime

# Create your views here.
def hello(request):
	today = datetime.datetime.now().date()
	daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
	return redirect("https://www.djangoproject.com")

# Sending Parameters to Views
def viewArticle(request, articleID):
	text = "Displaying the article: %s"%articleID
	# return HttpResponse(text)
	return redirect(viewArticles, year = "2045", month = "02")

def viewArticles(request, month, year):
	text = "Displaying the article: {}-{}".format(month, year)
	return HttpResponse(text)

def disdate(request):
	from datetime import date
	day = date.today()
	return render(request, "myapp/hello.html", {'today': day})

def crudops(request):
	# creating an Entry

	dreamreal = DreamReal(
		website = "www.n1tr0g3n.com", mail = "HackerOnline@net.com",
		name = "Aetos", phonenumber = "1918179940"
		)
	dreamreal.save()

	# Real all Entries
	objects = DreamReal.objects.all()
	res ='Printing all DreamReal entries in the DB : <br>'

	for elt in objects:
		res += elt.name + '<br>'

	# Read specific entry

	sorex = DreamReal.objects.get(name = 'aetos')
	res += 'Printing One entry <br>'
	res += sorex.name

	# Delete an entry
	res += '<br> Deleting an entry <br>'
	sorex.delete()

	# Update
	dreamreal = DreamReal(
				website = "www.polo.com", mail = "sorex@polo.com", 
				name = "sorex", phonenumber = "002376970"
		)
 
	dreamreal.save()
	res += 'Updating entry<br>'

	dreamreal = DreamReal.objects.get(name = 'sorex')
	dreamreal.name = 'thierry'
	dreamreal.save()

	return HttpResponse(res)


def dataManipulation(request):
	res = ''

	# Filtering data
	qs = DreamReal.objects.filter(name = 'paul')
	res += "Found : %s results<br>"%len(qs)

	# Ordering results
	qs = DreamReal.objects.order_by("name")
	for elt in qs:
		res += elt.name + '<br>'

	return HttpResponse(res)

from django.views.generic import TemplateView, ListView
class StaticView(TemplateView):
	template_name = "myapp/static.html"


class DreamRealList(ListView):
	model = DreamReal
	template_name = "myapp/dreamreal_list.html"

from .forms import LoginForm
from django.template import RequestContext

def login(request):
	username = "not loggen in"	

	if request.method == "POST":
		# Get the posted form
		MyLoginForm = LoginForm(request.POST)

		if MyLoginForm.is_valid():
			username = MyLoginForm.cleaned_data['user']
	else:
		MyLoginForm = LoginForm()
	response = render_to_response(request, 'loggedin.html', {"username" : username})
	context_instance = RequestContext(request)
	 
	response.set_cookie('last_connection', datetime.datetime.now())
	response.set_cookie('username', datetime.datetime.now())
	
	return response

	# return render(request, "myapp/loggedin.html", {"username" : username})

class UserTest(TemplateView):
	template_name = "myapp/login.html"

def formView(request):
	 if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
			username = request.COOKIES['username']
			
			last_connection = request.COOKIES['last_connection']
			last_connection_time = datetime.datetime.strptime(last_connection[:-7], 
				 "%Y-%m-%d %H:%M:%S")
			
			if (datetime.datetime.now() - last_connection_time).seconds < 10:
				 return render(request, 'myapp/loggedin.html', {"username" : username})
			else:
				 return render(request, 'myapp/login.html', {})
			
	 else:
			return render(request, 'myapp/login.html', {})