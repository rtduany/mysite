from django.shortcuts import get_object_or_404, redirect, render

from .models import Bookmark
# Create your views here.


def bookmark_list(request):
	bookmarks = Bookmark.public.all()
	context = {'bookmarks': bookmarks}
	return render(request, 'marcador/bookmark_list.html', context)
