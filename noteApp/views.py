from django.contrib import auth
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .forms import *
from django.http import HttpResponseRedirect

class NoteView(View):
    def get(self, request):
        form = NoteForm()
        font=Font.objects.all()
        cat=Category.objects.all()
        note=Note.objects.all()
        obj={'form': form,'font':font,'category':cat,'note_list':note}
        return render(request, 'main.html', obj)
    def post(self,request):
        form=NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note=form.save(commit=False)
            note.owner=auth.get_user(request)
            note.font_id=int(request.POST.get('select_font'))
            note.category_id=int(request.POST.get('select_cat'))
            note.colorText=request.POST.get('select_colorText')
            note.colorArea=request.POST.get('select_colorArea')
            note.save()
        return HttpResponseRedirect('/')



