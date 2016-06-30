# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.template import Context, Template
from django.template.loader import get_template

def hello(request):
  today = datetime.datetime.today().strftime('%d, %b %Y')
  return render_to_response('hello.html',{ 'teraz': today})

def hello2(request):
    t = get_template('hello.html')
    today = datetime.datetime.now()
    c = Context({'teraz': today})

    html = t.render(c)
    return HttpResponse(html)





#  t = loader.get_template('hello.html')
#  html = t.render(Context({ 'teraz' : today }))
#  return HttpResponse(html)
  #t = '<html><body>Witaj!'
  #t += 'Dziś mamy {{ teraz }} '
  #t +=' </body></html>'
  #szablon = Template(t)
  #html = szablon.render(Context({ 'teraz': today}))
  #return HttpResponse(html)
