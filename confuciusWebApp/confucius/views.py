from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'form.html')

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        return HttpResponse(search_id)
