import base64

from django.http import JsonResponse
from rest_framework.views import APIView

from api.utils import CHDModelResnet
from api.utils import preparation


class TestView(APIView):

    def post(sef, request):
        img = request.data.get('image')
        base64_img_bytes = img.encode('utf-8')
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        model = preparation()
        pred = CHDModelResnet.forward(model, decoded_image_data)    
        return JsonResponse({'perd': pred})
