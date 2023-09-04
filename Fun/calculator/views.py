from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .src.calculator import Calculator
from .src.operations import Operator

class CalculatorView(APIView):
    
    def post(self, request):
        operator = request.data.get('operator')
        first_number = request.data.get('first_number')
        second_number = request.data.get('second_number')

        calculator = Calculator()

        try:
            op_enum = Operator(operator)
            result = calculator.execute(op_enum, first_number, second_number)
            return Response({'result': result}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
