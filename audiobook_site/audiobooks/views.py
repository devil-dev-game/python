from django.shortcuts import render
from .models import Audiobook

def audiobook_list(request):
    audiobooks = Audiobook.objects.all()
    return render(request, 'audiobooks/audiobook_list.html', {'audiobooks': audiobooks})
