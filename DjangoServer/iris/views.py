import json

from django.http import JsonResponse
from matplotlib import pyplot as plt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from tensorboard.compat import tf

from iris.fashion_service import FashionService
from iris.iris_service import IrisService


@api_view(['GET','POST'])
@parser_classes([JSONParser])
def iris(request):
    if request.method == 'GET':
        print(f" ##### GET at Here React ID is {request.body}#####")
        return JsonResponse({
            'result': request.body})
    elif request.method == 'POST':
        user_info = request.data
        sepalLengthCm = tf.constant(float(user_info['SepalLengthCm']))
        sepalWidthCm = tf.constant(float(user_info['SepalWidthCm']))
        setalLengthCm = tf.constant(float(user_info['PetalLengthCm']))
        setalWidthCm = tf.constant(float(user_info['PetalWidthCm']))
        features = [sepalLengthCm, sepalWidthCm, setalLengthCm, setalWidthCm]
        result = IrisService().service_model(features)
        print(type(result))
        print(f'result : {result}')
        print(f'넘어온 데이터 {user_info}')
        print(f'SepalLengthCm : {sepalLengthCm}')
        print(f'SepalWidthCm : {sepalWidthCm}')
        print(f'PetalLengthCm : {setalLengthCm}')
        print(f'PetalWidthCm : {setalWidthCm}')
        if result == 0:
            result = 'setosa / 부채붓꽃'
        elif result == 1:
            result = 'versicolor / 버시칼라 '
        elif result == 2:
            result = 'virginica / 버지니카'
        return JsonResponse({'result' : result})
    else : print(';;;')



@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def fashion(request):
    if request.method == 'GET':
        print(f" ##### GET at Here React ID is {request.GET['id']}#####")
        return JsonResponse({
            'result': FashionService().service_model(int(request.GET['id']))})
    elif request.method == 'POST':
        print(" ##### POST at Here #####")
        body = request.body  # byte string of JSON data
        data = request.data
        print(f" ##### request data is {data} type {type(data)} #####")
        print(f" ##### request body is {body} type {type(body)}#####")
        data = json.loads(body)
        print(request.headers)
        print(request.content_type)
        print(f"##### React ID Is {data} ####")
        result = FashionService().service_model(int(data['Num']))
        return JsonResponse({'result': result})

    else: print(';;;;')


# @api_view(['POST'])
# def fashion(request):
#     print(" ##### POST at Here #####")
#     body = request.body # byte string of JSON data
#     data = request.data
#     print(f" ##### request data is {data} type {type(data)} #####")
#     print(f" ##### request body is {body} type {type(body)}#####")
#     data = json.loads(body)
#     print(request.headers)
#     print(request.content_type)
#     print(f"##### React ID Is {data} ####")
#     result = FashionService().service_model(int(data['Num']))
#     return JsonResponse({ 'result' : result})