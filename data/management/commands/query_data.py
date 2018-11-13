from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
import random

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
            except Exception:
                cat = Category.objects.create(name='category '+str(i))
                cat.save()

        #Create workflow 11, workflow 12 y workflow 13
        for i in xrange(11,14):
            try:
                cat = Category.objects.get(name='category 1')
                work = WorkFlow.objects.get(name='workflow ' + str(i))
            except Exception:
                cat = Category.objects.get(name='category 1')
                ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                work = WorkFlow.objects.create(name='workflow ' + str(i), client_ip=ip, json=self.getJson())
                work.category.add(cat)
                work.save()

        ##Create workflow 21, workflow 22 y workflow 23
        for i in xrange(21,24):
            try:
                cat = Category.objects.get(name='category 2')
                work = WorkFlow.objects.get(name='workflow ' + str(i))
            except Exception:
                cat = Category.objects.get(name='category 2')
                ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                work = WorkFlow.objects.create(name='workflow ' + str(i), client_ip=ip, json=self.getJson())
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
            for cat in work.category.all():
                print cat.slug
        except Exception:
            print 'workflow 1 inexistente'

        #Category of workflow with slug workflow-10
        try:
            work = WorkFlow.objects.get(slug='workflow_10')
            for cat in work.category.all():
                print cat.slug
        except Exception:
            print 'workflow_10 inexistente'

    def getJson(self):
        return """[
    {
        "object.className": "ProtImportMovies",
        "object.id": "2",
        "object.label": "import movies",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "importFrom": 0,
        "filesPath": "",
        "filesPattern": "Falcon*.mrcs",
        "copyFiles": false,
        "acquisitionWizard": null,
        "voltage": 300.0,
        "sphericalAberration": 2.0,
        "amplitudeContrast": 0.1,
        "magnification": 39548,
        "samplingRateMode": 0,
        "samplingRate": 3.54,
        "scannedPixelSize": 14.0,
        "gainFile": null
    },
    {
        "object.className": "ProtMovieAlignment",
        "object.id": "40",
        "object.label": "movie alignment",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "cleanMovieData": true,
        "alignMethod": 0,
        "alignFrame0": 0,
        "alignFrameN": 0,
        "doGPU": false,
        "GPUCore": 0,
        "winSize": 150,
        "sumFrame0": 0,
        "sumFrameN": 0,
        "cropOffsetX": 0,
        "cropOffsetY": 0,
        "cropDimX": 0,
        "cropDimY": 0,
        "binFactor": 1,
        "extraParams": "",
        "hostName": "localhost",
        "numberOfThreads": 4,
        "numberOfMpi": 1,
        "inputMovies": "2.__attribute__outputMovies"
    },
    {
        "object.className": "ProtCTFFind",
        "object.id": "82",
        "object.label": "ctffind4",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "recalculate": false,
        "sqliteFile": null,
        "ctfDownFactor": 1.0,
        "useCftfind4": true,
        "astigmatism": 100.0,
        "findPhaseShift": false,
        "lowRes": 0.05,
        "highRes": 0.35,
        "minDefocus": 0.5,
        "maxDefocus": 4.0,
        "windowSize": 256,
        "hostName": "localhost",
        "numberOfThreads": 4,
        "numberOfMpi": 1,
        "inputMicrographs": "40.__attribute__outputMicrographs"
    },
    {
        "object.className": "EmanProtBoxing",
        "object.id": "369",
        "object.label": "eman2 - boxer",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "inputMicrographs": "40.__attribute__outputMicrographs"
    },
    {
        "object.className": "ProtUserSubSet",
        "object.id": "380",
        "object.label": "3mics",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "other": null,
        "sqliteFile": "Runs/000082_ProtCTFFind/ctfs_selection.sqlite,",
        "outputClassName": "SetOfMicrographs",
        "inputObject": "82.__attribute__outputCTF"
    },
    {
        "object.className": "XmippProtParticlePicking",
        "object.id": "420",
        "object.label": "xmipp3 - manual picking",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "memory": 2.0,
        "inputMicrographs": "40.__attribute__outputMicrographs"
    },
    {
        "object.className": "XmippProtExtractParticles",
        "object.id": "449",
        "object.label": "extract 3 mics",
        "object.comment": "\\n",
        "runName": null,
        "runMode": 0,
        "micsSource": 0,
        "boxSize": 64,
        "doSort": false,
        "rejectionMethod": 0,
        "maxZscore": 3,
        "percentage": 5,
        "doRemoveDust": true,
        "thresholdDust": 3.5,
        "doInvert": true,
        "doFlip": false,
        "doNormalize": true,
        "normType": 2,
        "backRadius": -1,
        "hostName": "localhost",
        "numberOfThreads": 1,
        "numberOfMpi": 1,
        "ctfRelations": "82.__attribute__outputCTF",
        "inputCoordinates": "123.__attribute__outputCoordinates",
        "inputMicrographs": "369.outputMicrographs"
    },
    {
        "object.className": "XmippParticlePickingAutomatic",
        "object.id": "517",
        "object.label": "xmipp3 - auto-picking",
        "object.comment": "",
        "runName": null,
        "runMode": 0,
        "micsToPick": 0,
        "memory": 2.0,
        "hostName": "localhost",
        "numberOfThreads": 1,
        "numberOfMpi": 1,
        "xmippParticlePicking": "420"
    }
]"""
