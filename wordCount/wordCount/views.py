from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def countPage(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()

    wordCount = len(wordList)
    wordCountDictionary = {}

    for word in wordList:
        if word in wordCountDictionary:
            wordCountDictionary[word] += 1
        else:
            wordCountDictionary[word] = 1

    sortWordCountDictionary = sorted(wordCountDictionary.items(), key=operator.itemgetter(1), reverse=False)
    return render(request, 'count.html', {'fulltext':fulltext, 'sortedWordCountDictionary': sortWordCountDictionary, 'wordCount':wordCount})

def aboutPage(request):
    return render(request, 'about.html')