# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from data.models import Category, WorkFlow

from upload.forms import WorkFlowForm

from find.forms import SearchForm

# Create your views here.
def add_workflow(request):

    result = True
    workflow = None
    error = ''
    cats = []
    formSearch = SearchForm()

    if request.method == 'POST':
        form = WorkFlowForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                #Guardamos el workflow (falta categoria y json)
                workflow = form.save(commit=True)
                
                #Guardamos la categoria
                nameCat = form.cleaned_data['category'][0]
                cat = Category.objects.get(name=nameCat)
                workflow.category.add(cat)

                #Guardamos el json
                workflowFile = form.cleaned_data['json']
                file_data = workflowFile.read().decode('utf-8')
                form.instance.json = file_data
                workflow.json = file_data

                #Guardamos el workflow
                workflow.save()

            except Exception:
                result = False
                error += 'Workflow  with this name alredy exists'

            if result == True:
                for cat in workflow.category.all():
                    cats.append(cat)
            else:
                cats = list(Category.objects.all())        

            #Formamos el diccionario
            _dict = {}
            _dict['result'] = result        # False if no workflow satisfices the query
            _dict['workflow'] = workflow    # workflow with id = id
            _dict['error'] = error         # message to display if results == False
            _dict['categories'] = cats

    
            if result == False:
                return render(request, 'upload/add_workflow.html', _dict)

            _dict['form'] = formSearch
            _dict['msg'] = 'Workflow %s successfully uploaded' %(workflow.name)

            return render(request, 'find/detail.html', _dict)

        else:
            print (form.errors)

    #Como es un GET, tenemos que coger todas las categorias de la base de datos
    context_dict = {}
    context_dict['categories'] = list(Category.objects.all())
    return render(request, 'upload/add_workflow.html', context_dict)

