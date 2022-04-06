from unittest import result
from django.shortcuts import render

import requests


# Create your views here.

def home(request):
    return render(request,'musicsearch/home.html')


def store(request):
    r = requests.get('https://itunes.apple.com/search?term=eminem&limit=10')
    print(r)

    if(r.status_code ==200):
        
        content = r.json()

        MusicImage = content["results"][3]["artworkUrl100"]
        MusicTitle =  content["results"][3]["trackName"]
        AlbumName =  content["results"][3]["collectionName"]
        SingerName =  content["results"][3]["artistName"]

        context = {
            "songImag": MusicImage,
            "songTitle": MusicTitle,
            "albumName": AlbumName,
            "singer": SingerName
        }

    else:
        context= {}
        print("data not found")

    return render(request,'musicsearch/store.html', context)


def search(request):
     if request.method == "POST":
         searched = request.POST['query']
         searched2 = searched.replace("","+")
         if searched2:
             ApiUrl = 'https://itunes.apple.com/search?term='
             FinalApi = ApiUrl + searched2 + '&limit=10'
             response = requests.get(FinalApi)
             if (response.status_code == 200):
                  content = response.json()
                  Allresult = content["results"]
           
         else:
            searched = 'there has been an error'
            Allresult = []

     return render(request,'musicsearch/result.html', {
        "result": searched,
        "context": Allresult
    })


def cart(request):
    return render(request,'musicsearch/shop_cart.html')
