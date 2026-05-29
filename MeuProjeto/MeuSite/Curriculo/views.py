from django.shortcuts import render

def Curriculo1 (request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'Curriculo/index.html')

def Curriculo2 (request):

    return render(request, 'Curriculo/spiff.html')