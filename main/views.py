from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home: Trainbooking',
        'head': 'Train booking - HOME',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the'
                   ' industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                   'and scrambled it to make a type specimen book.',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About: Trainbooking',
        'head': 'Train booking - ABOUT',
        'content': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the'
                   ' industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type '
                   'and scrambled it to make a type specimen book.',
    }

    return render(request, 'main/about.html', context)