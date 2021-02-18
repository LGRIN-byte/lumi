from django.shortcuts import render


def first(request):
    return render(request, 'Web/first.html', {})

def main(request):
    return render(request, 'Web/main.html', {})
