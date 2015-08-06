from django.shortcuts import render

def startpage(request):
	return render(request, "quiz/startsidaquiz.html")

def quiz(request):
    return render(request, "quiz/quiz1start.html")

def question(request): 
	return render(request, "quiz/quiz1.html")

def completed(request):
	return render(request, "quiz/quiz1resultat")


# Create your views here.
