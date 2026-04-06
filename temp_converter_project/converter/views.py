
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'form.html')

def convert_temp(request):

    if request.method == "POST":
        temp = float(request.POST.get("temp"))
        scale = request.POST.get("scale")

        if scale == "celsius":
            result = (temp * 9/5) + 32
            unit = "Fahrenheit"

        elif scale == "fahrenheit":
            result = (temp - 32) * 5/9
            unit = "Celsius"

        return render(request, "result.html", {
            "result": result,
            "unit": unit
        })

