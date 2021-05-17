from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiview(APIView):
    #Apiviews de prueba

    def get(self,request, format=None):
        #retornar caracteristicas del apiviews

        an_apiview = [
            'usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los URLs',

        ]

        return Response({'massage': "Hello World", 'an_apiview': "an_apiview"})
