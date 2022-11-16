from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    print(request)
    print(request)
    return render(request, 'excelapp/index.html')
