from django.shortcuts import render, redirect
from .hashing import Hashing


def index(request):
    if request.method == 'POST' and len(request.POST['link']) > 0:
        return render_result_page(request)
    else:
        return render(request, 'main_page/index.html')


def render_result_page(request):
    return render(request, 'result_page/index.html',
                  {'shortened_link': get_result_link(request)})


def get_result_link(request) -> str:
    return request.get_host() + Hashing.process_url(request.POST['link'])


def redirect_to_original(request, shortened_url):
    shortened_url = '/' + shortened_url
    if Hashing.is_this_a_new_url(shortened_url, hashed=True):
        return error_404_view(request)
    else:
        return redirect(Hashing.get_original_url(shortened_url))


def error_404_view(request, *args):
    return render(request, 'error_404/index.html')
