# # I HAVE CREATED THIS WEBSITE!!
##CODE FOR VIDEO 6
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('''<h1>HELLO HARSHIT</H1><a href="https://www.codechef.com/LTIME91B" >django code with harshit</a>''')
# def about(request):
#     return HttpResponse('About Harshit!!')

# CODE FOR VIDEO 7
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,'index.html')
    # return HttpResponse('HOME!!!!')
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('capital','off')
    newlineremover=request.POST.get("newlineremove",'off')
    spaceremover=request.POST.get('removespace','off')
    countcharacter= request.POST.get('charcount', 'off')
    punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed=''
    if(removepunc=='on'):
        for l in djtext:
          if l not in punctuations:
            analyzed=analyzed+l
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if (fullcaps == 'on'):
        analyzed = ''
        for l in djtext:
            analyzed=analyzed+ l.upper()
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ''
        for l in djtext:
            if l != '\n' and l!='\r':
                analyzed = analyzed + l
        params = {'purpose': 'NewLine remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == 'on'):
        analyzed = ''
        for i,l in enumerate(djtext):
            if(djtext[i]==' ' and djtext[i+1]==' '):
                pass
            else:
                analyzed=analyzed+l
        params = {'purpose': 'Remove spaces', 'analyzed_text': analyzed}
        djtext = analyzed


    c=0
    if (countcharacter == 'on'):
        for l in djtext:
            if l!=" " and (l!='\n' and l!='\r'):
                c=c+1
        analyzed=djtext
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed,'charcount':c}


    if(analyzed==''):
        analyzed=djtext
        params = {'purpose': 'None', 'analyzed_text': analyzed}



    return render(request,'analyze.html',params)
def capfirst(request):
    return HttpResponse('capitalize first!!! <a href="http://127.0.0.1:8000/"><button>home</button></a>')
def newlineremove(request):
    return HttpResponse('new line remover!!! <a href="http://127.0.0.1:8000/"><button>home</button></a>')
def spaceremove(request):
    return HttpResponse('space remover!!! <a href="http://127.0.0.1:8000/"><button>home</button></a>')
def charcount(request):
    return HttpResponse('char count!!! <a href="http://127.0.0.1:8000/"><button>home</button></a>')