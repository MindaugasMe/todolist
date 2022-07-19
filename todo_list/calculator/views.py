from django.shortcuts import render
import csv
import pandas as pd


def index(request):
    return render(request, "calculator/input.html")


def count(request):
    sport = int(request.POST['activity'])
    data = pd.read_csv('sport.csv')
    action = data['name'][sport]
    weight_data = float(data['weight'][sport])
    time_data = float(data['time'][sport])
    str_time = request.POST['time']
    str_weight = request.POST['weight']
    if str_time.isdigit()>0 and str_weight.isdigit()>0:
        time = int(str_time)
        weight = int(str_weight)
        res = (time*time_data) * (weight*weight_data)
        return render(request, "calculator/result.html", {"result": res, "activity": action})
    else:
        res = "Only digits are allowed"
        return render(request, "calculator/result.html", {"result": res})