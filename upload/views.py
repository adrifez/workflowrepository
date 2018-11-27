# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from data.models import Category, WorkFlow

# Create your views here.
def add_workflow(request):
    form = WorkFlowForm()
    if request.method == 'POST':
        form = WorkFlowForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #Esto va a fallar
            return render(request, 'upload/index.html')

        else:
            print (form.errors)
    #Como es un GET, tenemos que coger todas las categorias de la base de datos
    cats = list(Category.objects.all())
    return render(request, 'upload/add_workflow', cats=cats)
