import os

import barcode
from barcode.writer import ImageWriter
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from uploadfilses.settings import BASE_DIR


# Create your views here.

def upload(r):
    # ean = barcode.get_barcode_class('code128')
    ean = barcode.get(name="code128",code='1234ABC',writer=ImageWriter())
    # code = ean('1234', writer=ImageWriter())
    # ean.save(os.path.join(BASE_DIR, 'templates/docx/generateddrs/barcode/1234'))
    models.Model(name='1234',files=ean.save(os.path.join(BASE_DIR,"files/1234ABC"))).save()
    return HttpResponse("Hi")