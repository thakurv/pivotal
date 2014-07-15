from django.http import HttpResponse
from fizzbuzz.fizzbuzz import *

def index_view(request):
		return HttpResponse(FizzBuzz().numb())
