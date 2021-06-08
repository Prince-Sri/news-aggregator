from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    
    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=dee86c8f95284260a8dbb95a390c72aa")
    
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api':api})