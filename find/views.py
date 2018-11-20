# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import json

from data.models import Category, WorkFlow

from find.forms import SearchForm

# Create your views here.

def workflow_list(request, category_slug=None):
    # YOUR CODE GOES HERE
    category = None
    categories = None
    workflows = None
    found = True
    error = ''
    form = SearchForm()

    if category_slug == None:
        try:
            workflows = WorkFlow.objects.all()
        except Exception:
            found = False
            error += 'No existen workflows en la base de datos. '

    else:
        try:
            category = Category.objects.get(slug=category_slug)
        except Exception:
            found = False
            error += 'Busqueda de categoria con slug ' + category_slug + ' fallida. '
        else:
            try:
                workflows = WorkFlow.objects.filter(category=category)
            except Exception:
                found = False
                error += 'Busqueda de los workflows con categoria con slug ' + category_slug + ' fallida. '

    try:
        categories = Category.objects.all()
    except Exception:
        found = False
        error += 'No existen categorias en la base de datos. '

    _dict = {'category': category,  # category associated to category_slug
        'categories': categories,   # list with all categories
                                    # usefull to repaint the category
                                    # menu
        'workflows': workflows,     # all workflows associated to category
                                    # category_slug
        'result': found,            # False if no workflow satisfices the query
        'error': error,             # message to display if results == False
        'form': form
    }

    return render(request, 'find/list.html', _dict)

def workflow_detail(request, id, slug):
    #Your code goes here
    result = True
    workflow = None
    error = ''
    cats = []
    form = SearchForm()

    try:
        workflow = WorkFlow.objects.get(slug=slug)
        for cat in workflow.category.all():
            cats.append(cat)
    except Exception:
            result = False
            error += 'No existe ese workflow en la base de datos. '

    #query that returns the workflow with id=id
    _dict = {}
    _dict['result'] = result        # False if no workflow satisfices the query
    _dict['workflow'] = workflow    # workflow with id = id
    _dict['error'] = error          # message to display if results == False
    _dict['categories'] = cats
    _dict['form'] = form

    return render(request, 'find/detail.html', _dict)

def workflow_search(request):
    #Your code goes here
    result = True
    workflow = None
    error = ''
    cats = []
    form = SearchForm()

    if request.method == 'POST':

        try:
            form = SearchForm(request.POST)
            f = str(form)
            print f
            start = f.find('name="key" value="') + 18
            end = f.find('"', start)
            key = f[start:end]
            workflow = WorkFlow.objects.get(name=key)
            for cat in workflow.category.all():
                cats.append(cat)
        except Exception:
                result = False
                error += 'No existe ese workflow en la base de datos. '

    else:
        result = False
        error += 'Se necesita metodo POST. '

    _dict = {}
    _dict['result'] = result      # False if no workflow satisfices the query
    _dict['workflow'] = workflow  # workflow with name = name
    _dict['error'] = error        # message to display if results == False
    _dict['categories'] = cats
    _dict['form'] = form

    return render(request, 'find/detail.html', _dict)


# Download worflow
def workflow_download(request , id , slug , count = True ):
    error = ''
    worlflow = None
    # Buscamos en la base de datos el workflow correspondiente
    try:
        workflow = WorkFlow.objects.get(slug=slug)
        print workflow

    except Exception:
            count = False
            error += 'No existe ese workflow en la base de datos.'

    if count == True:
        workflow.downloads = workflow.downloads + 1
        workflow.save()

        response = HttpResponse(workflow.json, content_type=" application / octet−stream")
        fileName = "WorkFlow_"+ str(workflow.id)
        response['Content-Disposition'] = 'inline; filename=%s' %fileName
        return response

#TODO:Devolver algo con sentido
    return error
