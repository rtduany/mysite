from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookmarkForm
from .models import Bookmark
# Create your views here.


def bookmark_list(request):
	bookmarks = Bookmark.public.all()
	context = {'bookmarks': bookmarks}
	return render(request, 'marcador/bookmark_list.html', context)

def bookmark_user(request, username):
	user = get_object_or_404(User, username=username)
	if request.user == user:
		bookmarks = user.bookmarks.all()
	else:
		bookmarks = Bookmark.public.filter(owner__username=username)
		context = {'bookmarks': bookmarks, 'owner': user}
	return render(request, 'marcador/bookmark_user.html', context)


@login_required
def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(data=request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.owner = request.user
            bookmark.save()
            form.save_m2m()
            return redirect('marcador_bookmark_user',
                username=request.user.username)
    else:
        form = BookmarkForm()
    context = {'form': form, 'create': True}
    return render(request, 'marcador/form.html', context)
