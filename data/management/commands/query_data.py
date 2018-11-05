from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
import random
import from populate import Command

django.setup()

from data.models import Category, WorkFlow


# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts queries de workFlow database.' \
           'Execute it with the command line python manage.py query_data'

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):

        #Create category 1 y category 2 if dont exist
        for i in xrange(1, 3):
            try:
                cat = Category.objects.get(name='category '+str(i))
            except ObjectDoesNotExist:
                cat = Category.objects.create(name='category '+str#Category of workflow with slug workflow-1
        try:
            work = WorkFlow.objects.get(slug='workflow-1')
            cat = work.category
            print cat.slug
        except ObjectDoesNotExist:
            print 'workflow workflow 1 inexistnte'(i))
                cat.save()

        #Create workflow 11, workflow 12 y workflow 13
        for i in xrange(11,14):
            try:
                cat = Category.objects.get(name='category 1')
                work = WorkFlow.objects.get(name='workflow ' + str(i), category=cat)
            except ObjectDoesNotExist:
                cat = Category.objects.get(name='category 1')
                work = WorkFlow.objects.get(name='workflow ' + str(i), json=Command.getJson())
                work.category.add(cat)
                work.save()

        ##Create workflow 21, workflow 22 y workflow 23
        for i in xrange(21,24):
            try:
                cat = Category.objects.get(name='category 2')
                work = WorkFlow.objects.get(name='workflow ' + str(i), category=cat)
            except ObjectDoesNotExist:
                cat = Category.objects.get(name='category 2')
                work = WorkFlow.objects.get(name='workflow ' + str(i))
                work.category.add(cat)
                work.save()

        #List of workflows associated with category 1
        cat1 = Category.objects.get(name='category 1')
        list = WorkFlow.objects.filter(category=cat1)
        for item in list:
            print item

        #Category of workflow with slug workflow-1
        try:
            work = WorkFlow.objects.get(slug='workflow-1')
            cat = work.category
            print cat.slug
        except ObjectDoesNotExist:
            print 'workflow workflow 1 inexistnte'

        #Category of workflow with slug workflow-10
        try:
            work = WorkFlow.objects.get(slug='workflow_10')
            cat = work.category
            print cat.slug
        except ObjectDoesNotExist:
            print 'workflow workflow_10 inexistnte'
