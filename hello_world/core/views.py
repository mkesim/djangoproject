# core/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def calculate(request):
    result = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')
        
        if num1 and num2:
            num1 = float(num1)
            num2 = float(num2)
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Error: Division by zero'
            else:
                result = 'Invalid Operation'
        else:
            result = 'Please provide both numbers'

    return render(request, 'index.html', {'result': result})
