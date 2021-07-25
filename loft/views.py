from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as admin_login
from django.contrib.auth import logout as admin_logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def loft_home(request):
	return render(request, 'loft/home.html', {'lofts': Loft.objects.all(), "comment_f": CommentForm(), "comments": Comment.objects.all()[:4]})

def comment_form(request):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(username=form.cleaned_data["username"], description=form.cleaned_data["description"])
			comment.save()
	return loft_home(request)

def quizz_form(request):
	if request.method == "POST":
		name = request.POST['name']
		age = request.POST['age']
		comments = request.POST['textarea']
		q = Quizz(username=name, age=age, comments=comments, score=0)
		q.save()
		result = 0
		framework = request.POST['framework']
		answer1 = Answer(quizz=q, question="Which framework is this website currently using?", answer=framework, correct=framework.lower()=="django")
		answer1.save()
		if answer1.correct:
			result+=5
		modalty = request.POST['modality']
		answer2 = Answer(quizz=q, question="What does the website offers?", answer=modalty, correct=modalty.lower()=="rents")
		answer2.save()
		if answer2.correct:
			result+=5
		website_name = request.POST['website_name']
		answer3 = Answer(quizz=q, question="What's the Website's name?", answer=website_name, correct=website_name.lower()=="loft")
		answer3.save()
		if answer3.correct:
			result+=5
		b_and_fa = request.POST['b_and_fa']
		answer4 = Answer(quizz=q, question="Is the website using Bootstrap and Font Awesome?", answer=b_and_fa, correct=b_and_fa.lower()=="yes")
		answer4.save()
		if answer4.correct:
			result+=5
		loft = Loft.objects.get(pk=int(request.POST['select']))
		answer5 = Answer(quizz=q, question="Choose your Favourite Apartment:", answer=loft.name, correct=True)
		answer5.save()
		cities = ""
		if "city1" in request.POST:
			cities += "Lisboa "
			result+=5
		if "city2" in request.POST:
			cities += "Porto "
			result+=5
		if "city3" in request.POST:
			cities += "Paris "
			result-=5
		if "city4" in request.POST:
			cities += "Algarve "
			result+=5
		answer6 = Answer(quizz=q, question="Choose which cities have availabe apartments?", answer=cities.strip().replace(" ", ", "), correct=True)
		answer6.save()
		q.score = result/60 * 100
		q.save()
		return render(request, 'loft/results.html', {'quizz': Quizz.objects.get(pk=q.id)})
	return loft_home(request)

def loft_page(request, loft_id):
	return render(request, 'loft/loft_page.html', {'lofts': Loft.objects.all(), 'loft': Loft.objects.get(pk=loft_id), "contact_form": ContactForm()})

def contact(request, loft_id):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = Contact(username=form.cleaned_data['username'], phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'], message=form.cleaned_data['message'], loft=Loft.objects.get(pk=loft_id))
			if "date_of_birth" in form.cleaned_data:
				contact.date_of_birth = form.cleaned_data['date_of_birth']
			contact.save()
	return render(request, 'loft/home.html', {'lofts': Loft.objects.all(), "comment_f": CommentForm(), "comments": Comment.objects.all()[:4]})

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				admin_login(request, user)
				return render(request, 'loft/profile.html',  {'lofts': Loft.objects.all(), 'contacts': Contact.objects.all()})
	return render(request, 'loft/login.html', {'lofts': Loft.objects.all(), "login_form": LoginForm(), "signup_form": SignUpForm})

def sign_up(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
			user.save()
			admin_login(request, user)
			return render(request, 'loft/profile.html',  {'lofts': Loft.objects.all(), 'contacts': Contact.objects.all()})
	return render(request, 'loft/login.html',  {'lofts': Loft.objects.all(), "login_form": LoginForm(), "signup_form": SignUpForm})

def logout(request):
	admin_logout(request)
	return render(request, 'loft/home.html', {'lofts': Loft.objects.all(), "comment_f": CommentForm(), "comments": Comment.objects.all()[:4]})

def quizz_result(request, quizz_id):
	return render(request, 'loft/results.html', {'quizz': Quizz.objects.get(pk=quizz_id)})

@login_required(login_url='./login')
def profile(request):
	return render(request, 'loft/profile.html',  {'lofts': Loft.objects.all(), 'contacts': Contact.objects.all()})

@login_required(login_url='./login')
def delete_loft(request, loft_id):
	Loft.objects.get(pk=loft_id).delete()
	return render(request, 'loft/profile.html',  {'lofts': Loft.objects.all(), 'contacts': Contact.objects.all()})

@login_required(login_url='./login')
def delete_contact(request, contact_id):
	Contact.objects.get(pk=contact_id).delete()
	return render(request, 'loft/profile.html',  {'lofts': Loft.objects.all(), 'contacts': Contact.objects.all()})