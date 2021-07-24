from django.shortcuts import render
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
		framework = request.POST['framework']
		answer1 = Answer(quizz=q, question="Which framework is this website currently using?", answer=framework, correct=framework.lower()=="django")
		answer1.save()
		modalty = request.POST['modality']
		answer2 = Answer(quizz=q, question="What does the website offers?", answer=modalty, correct=modalty.lower()=="rents")
		answer2.save()
		website_name = request.POST['website_name']
		answer3 = Answer(quizz=q, question="What's the Website's name?", answer=website_name, correct=website_name.lower()=="loft")
		answer3.save()
		b_and_fa = request.POST['b_and_fa']
		answer4 = Answer(quizz=q, question="Is the website using Bootstrap and Font Awesome?", answer=b_and_fa, correct=b_and_fa.lower()=="yes")
		answer4.save()
		loft = Loft.objects.get(pk=int(request.POST['select']))
		answer5 = Answer(quizz=q, question="Choose your Favourite Apartment:", answer=loft.name, correct=True)
		answer5.save()
		cities = ""
		if "city1" in request.POST:
			cities += "Lisboa "
		if "city2" in request.POST:
			cities += "Porto "
		if "city3" in request.POST:
			cities += "Paris "
		if "city4" in request.POST:
			cities += "Algarve "
		answer6 = Answer(quizz=q, question="Choose which cities have availabe apartments?", answer=cities.strip().replace(" ", ", "), correct=True)
		answer6.save()
	return loft_home(request)
