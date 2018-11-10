# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json

from data.models import Category, WorkFlow

# Create your views here.

def workflow_list(request, category_slug=None):
    # YOUR CODE GOES HERE
    category = None
    categories = None
    workflows = None
    found = True
    error = ''

    if category_slug == None:
        try:
            workflows = WorkFlow.objects.all()
        except Exception:
            found = False
            error += 'No existen workflows en la base de datos'

    else:
        try:
            category = Category.objects.get(slug=category_slug)
        except Exception:
            found = False
            error += 'Busqueda de categoria con slug ' + category_slug + ' fallida'
        else:
            try:
                workflows = WorkFlow.objects.filter(category=category)
            except Exception:
                found = False
                error += 'Busqueda de los workflows con categoria con slug ' + category_slug + ' fallida'

    try:
        categories = Category.objects.all()
    except Exception:
        found = False
        error += 'No existen categorias en la base de datos'

    _dict = {'category': category,  # category associated to category_slug
        'categories': categories,   # list with all categories
                                    # usefull to repaint the category
                                    # menu
        'workflows': workflows,     # all workflows associated to category
                                    # category_slug
        'result': found,            # False if no workflow satisfices the query
        'error': error              # message to display if results == False
    }

    return render(request, 'find/list.html', _dict)