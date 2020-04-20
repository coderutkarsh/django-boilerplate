from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from django.core import serializers
import json
#for get and post request segregatation
from django.views.generic import View
# from products.
# Create your views here.
# this is the same funcrtion as router directed controllers in our node app.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addProduct(request):
     # print(request.body)
     body_unicode = request.body.decode('utf-8')
     params = json.loads(body_unicode)
     prodObj = Product(name=params['name'], desc=params['desc'], price=params['price'])
     prodObj.save()
     return HttpResponse(prodObj)



def getProduct(request):
    # paramsTemp = request.body
    #way of getting get request parameter.
    print(request.GET)
    params = request.GET.dict()
    # print('params',params)
    #way of decoding post params
    # body_unicode = request.body.decode('utf-8')
    # params = json.loads(body_unicode)

    # # prodObj = Product.objects.get()
    # SomeModel_json = serializers.serialize("json", Product.objects.all())
    # print("SomeModel_json",SomeModel_json)
    kwargs = params

    allproducts = Product.objects.filter(**kwargs)
    qs_json = serializers.serialize('json', allproducts)
    return HttpResponse(qs_json, content_type='application/json')
    # return HttpResponse("django sucks")

def home(request):
    # Product.sampleFunc()
    prodObj = Product(name='Desktop', desc='Desktop with 2 gb ramn', price=450)
    prodObj.save()
    # Product.objects.create
    # proObj.save()
    # proObj.cre()
    # prodObj.sampleFunc()

    # /sampleFuncprint(prodObj)
    return HttpResponse('Hey there')


#
# class Product(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('This is GET request')
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse('This is POST request')



def getAllProducts(request):

    prods = Product.objects.all()

    return HttpResponse(prods)



    return HttpResponse('Sample resp')

    # HttpResponse is similar to res in node.