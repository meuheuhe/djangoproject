from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
# from .opencv_mix import opencv_mix

# Create your views here.


def opencvweb(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    
            imageURL1 = settings.MEDIA_URL + form.instance.document.name
            imageURL2 = settings.MEDIA_URL + form.instance.document1.name            
            # opencv_mix(settings.MEDIA_ROOT_URL + imageURL1, settings.MEDIA_ROOT_URL + imageURL2)
    
            return render(request, 'opencvweb.html', {'form':form, 'post':post})
    else:
        form = ImageUploadForm()
    return render(request, 'opencvweb.html',{'form':form})