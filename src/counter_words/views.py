from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def counter(request):
    return render(request, 'counter.html')

def output_counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'output_counter.html', {'amount': amount_of_words})