from json import JSONDecodeError
from django.http import JsonResponse
from .serializer.serializers import SprameterSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from .library import port2SP
from .library import port4SP
# Create your views here.


class SParameterAPIView(views.APIView):
    serializer_class = SprameterSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
    def get(self, request):
        return Response("HEllo World")
    def post(self, request):
        try:
            print(request)
            data = JSONParser().parse(request)
            serializer = SprameterSerializer(data=data)
            print(data)
            
            if serializer.is_valid(raise_exception=False):
                if(data["issingleended"]):
                    return Response(data=port2SP.calculateSparameter(data), status=status.HTTP_200_OK, content_type='application/json')
                else:
                    return Response(data=port4SP.calculateSparameter(data), status=status.HTTP_200_OK, content_type='application/json')
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except JSONDecodeError:
             return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
        except Exception:
            return JsonResponse({"result": "error","message": "Error on python server"}, status= 500)
        # except Exception:
        #     return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
