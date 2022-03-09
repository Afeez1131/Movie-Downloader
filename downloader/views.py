from django.shortcuts import render
from .utils import category_movie, category_nollywood, category_series, get_videos, get_videos_genre
# Create your views here.
import re


def Home(request):

    url = request.GET.get('url','')
    print('URL ', url)
    validator = r"^https://www.thenetnaija.co/videos"
    match = re.search(validator, 'https://www.thenetnaija.co/videos')
    if match:
        print('Matched')
    else:
        print('Not the same')
    return render(request, 'home.html', {})

# download_real_link(url):




'''
https://www.thenetnaija.co/videos/nollywood/15692-two-wives-one-husband-2022
https://www.thenetnaija.co/videos/nollywood

https://www.thenetnaija.co/videos/kdrama/15745-business-proposal
https://www.thenetnaija.co/videos/kdrama

https://www.thenetnaija.co/videos/movies/15781-the-girl-on-the-mountain-2022
https://www.thenetnaija.co/videos/movies


'''