from django.shortcuts import render
from datetime import datetime, timedelta
import csv
import pandas as pd


def index(request):
    time_now = datetime.now().strftime('%d %H:%M')
    return render(request, "calculator/input.html", {'date_now': time_now})


def count_calories(request):
    sport = int(request.POST['activity'])
    str_time = request.POST['time']
    activity_from = request.POST['tnow']
    str_weight = request.POST['weight']
    data = pd.read_csv('sport.csv')
    action = data['name'][sport]
    if str_time.isdigit()>0 and str_weight.isdigit()>0:
        weight_data = float(data['weight'][sport])
        time_data = float(data['time'][sport])
        activity_to = datetime.strptime(activity_from, '%d %H:%M') + timedelta(minutes=int(str_time))
        activity_to = datetime.strftime(activity_to, '%d %H:%M')
        time = int(str_time)
        weight = int(str_weight)
        res = round((time*time_data) * (weight*weight_data))
        row = [action, activity_from, activity_to, res]
        with open('exercise_history.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)
        return render(request, "calculator/result.html", {
            "result": res, 
            "activity": action, 
            "activity_from": activity_from, 
            "activity_to": activity_to
            })
    else:
        res = "Only digits are allowed"
        return render(request, "calculator/result.html", {"result": res})


def history(request):
    df = pd.read_csv('exercise_history.csv')
    df_time_from = df['time_from']
    df_exercise = df['exercise']
    df_calories = df['calories']
    df_time_to = df['time_to']
    return render(request, "calculator/history.html", {
        'exercises': df_exercise,
        'time_from_values': df_time_from, 
        'time_to_values': df_time_to, 
        'calories': df_calories
        })


