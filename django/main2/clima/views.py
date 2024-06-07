from django.shortcuts import render
import requests

def clima(request):
    if request.method == 'POST':
        ciudad = request.POST.get('ciudad')  
    else:
        ciudad = 'london'  
    api_key = 'fa6d5c6ef6d75591a0fef129b5748f7e'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    
    response = requests.get(url)
    data = response.json()
    return render(request, 'clima.html', {'data': data})