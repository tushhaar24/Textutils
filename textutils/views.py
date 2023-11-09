# I have created this file - T24
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   
    return render (request,'index2.html')
   
def analyze(request):
    
    djtext=request.POST.get('text','default')
    
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')
    wordscounter=request.POST.get('wordscounter','off')
    
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctutations',
                'analyzed_text':analyzed}
        djtext=analyzed
        
    
    if (fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to UpperCase',
                'analyzed_text':analyzed}
        djtext=analyzed
       
    
    if (newlineremover=='on') :
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'Removed NewLine',
                'analyzed_text':analyzed}
        djtext=analyzed
        
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remove',
                   'analyzed_text': analyzed}
        djtext=analyzed
       
    
    if (charcounter=='on'):
        analyzed=""
        char_count=len(djtext)
        analyzed += f"The character count is : {char_count} ."
        params={'purpose':'Count the Character',
                'analyzed_text':analyzed} 
        djtext=analyzed
        
    
    if (wordscounter=='on'):
        analyzed = ""
    
        words = djtext.split()
        words_count = len(words)

        analyzed = f"Total words: {words_count}"
        params = {
            'purpose': 'Count the Words',
            'analyzed_text': analyzed}
        djtext=analyzed
        
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and
        charcounter!="on" and wordscounter!="on"):
        return render(request,'error.html')
    
    return render(request, 'analyze.html', params) 

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')
