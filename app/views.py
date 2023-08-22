import os

import barcode
from barcode.writer import ImageWriter
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from uploadfilses.settings import BASE_DIR, MEDIA_ROOT


# Create your views here.

def upload(r):
    # ean = barcode.get_barcode_class('code128')
    ean = barcode.get(name="code128",code='1234ABC',writer=ImageWriter())
    # code = ean('1234', writer=ImageWriter())
    # ean.save(os.path.join(BASE_DIR, 'templates/docx/generateddrs/barcode/1234'))
    # c = ean.save(filename="1234ABC")
    c = ean.save(os.path.join(BASE_DIR,'media/files/9951264256'))
    # models.Model(name='1234',files=c).save()
    return HttpResponse("<img src='media/files/9951264256.png'/>")