from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from models import Wyklad
from models import Student
from models import Wykladowca

def search_form(request):
  return render_to_response('zapisy/search_form.html')

def search_student(request):
    return render_to_response('zapisy/search_student.html')

def search(request):
  if 'query' in request.GET and request.GET['query']:
    query = request.GET['query']
    wyklady = Wyklad.objects.filter(nazwa__icontains=query)
    return render_to_response('zapisy/search_results.html',
      {'wyklady': wyklady, 'query': query})
  else:
    return render_to_response('search_form.html', {'error': True})

def search_student_result(request):
    if 'imie' in request.GET and 'nazwisko' in request.GET:
        imie_1 = request.GET['imie']
        nazwisko_1 = request.GET['nazwisko']
        studenci = Student.objects.filter(imie=imie_1, nazwisko=nazwisko_1)
        return render_to_response('zapisy/search_results_student.html',{'studenci':studenci})
    elif 'show' in request.GET:
        studenci = Student.objects.all()
        return render_to_response('zapisy/search_results_student.html',{'studenci':studenci})
    else:
        return render_to_response('zapisy/search_student.html', {'error':True})

def search_teacher(request):
    return render_to_response('zapisy/search_teacher.html')

def search_teacher_result(request):
    if 'imie' in request.GET and 'nazwisko' in request.GET:
        imie_1 = request.GET['imie']
        nazwisko_1 = request.GET['nazwisko']
        teachers = Wykladowca.objects.filter(imie=imie_1, nazwisko=nazwisko_1)
        return render_to_response('zapisy/search_teacher_result.html', {'teachers':teachers})
    
    elif 'query' in request.GET:
        teachers = Wykladowca.objects.all()
        return render_to_response('zapisy/search_teacher_result.html', {'teachers':teachers})
    else:
        return render_to_response('zapisy/search_teacher_result.html', {'error':True})

def search_subjects(request):
    return render_to_response('zapisy/search_subjects.html')

def search_subjects_result(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if query == 'all':
            subjects = Wyklad.objects.all()
            return render_to_response('zapisy/search_subjects_result.html', {'subjects':subjects})
        else:
            subjects = Wyklad.objects.filter(nazwa=query)
            return render_to_response('zapisy/search_subjects_result.html', {'subjects':subjects})
    else:
        return render_to_response('zapisy/search_teacher_result.html', {'error':True})

from forms import ContactForm
from django.core.mail import send_mail
def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      send_mail(cd['subject'], cd['message'], cd['email'], ['noreply@example.com'])
      return HttpResponseRedirect('zapisy/thanks/')
  else:
    form = ContactForm()
  return render(request, 'zapisy/contact_form.html', {'form': form})

#from forms import ContactFormStudent
def zapisz(request):
    subjects = Wyklad.objects.all()
    return render(request, 'zapisy/zapisz.html', {'subjects':subjects})

def zapisz_result(request):
    if request.method == 'POST':
        imie1 = request.POST.get("imie")
        nazwisko1 = request.POST.get("nazwisko")
        przedmiot = request.POST.get("przedmiot")
        if imie1 == '' or nazwisko1 == '':
            subjects = Wyklad.objects.all()
            return render(request, 'zapisy/zapisz.html', {'subjects':subjects, 'error':True})
        try:
            student_1 = Student.objects.get(imie=imie1, nazwisko=nazwisko1)
            text = '%s %s zostal znaleziony w bazie. ' % (student_1.imie, student_1.nazwisko)
        except:
            student_1 = Student(imie=imie1, nazwisko=nazwisko1)
            student_1.save()
            text = '%s %s nie zostal znaleziony. Dodano studenta do bazy. ' % (student_1.imie, student_1.nazwisko)
        przedmiot_1 = Wyklad.objects.get(nazwa=przedmiot)
        try:
            student_2 = przedmiot_1.studenci.get(imie=imie1, nazwisko=nazwisko1)
            print 'student ', student_2.imie, ' jest juz zapisany na ', przedmiot_1.nazwa
            return render_to_response('zapisy/zapisz.html', {'odpowiedz':True, 'odpowiedz2':text+'Student jest juz zapisany za zajecia'})
        except:
            przedmiot_1.studenci.add(student_1)
            return render_to_response('zapisy/zapisz.html', {'odpowiedz':True, 'odpowiedz2':text+'Student zostal zapisany na zajecia'})
    else:
        return render_to_response('zapisy/zapisz.html', {'error':True})