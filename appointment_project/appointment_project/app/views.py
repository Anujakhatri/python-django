from django.shortcuts import render, redirect

# Create your views here.
from .db import get_connection, create_table, create_appointment, read_appointments, update_appointment, delete_appointment

def index(request):
    create_table()
    return render(request, "list.html")

    # conn = get_connection()
    # print("test1")
    # cursor = conn.cursor()
    # print("connected")

def create(request):
    create_table()
    if request.method == "POST":
        name = request.POST["name"]
        contact = request.POST["contact"]
        gender = request.POST["gender"]
        date = request.POST["date"]
        time = request.POST["time"]
        reason = request.POST["reason"]

        create_appointment(name, contact, gender, date, time, reason)
        return redirect("list")

    return render(request, "list_appointments")

def list_appointments(request):
    appointments = read_appointments()
    return render(request, "success.html", {"appointments": appointments})

def update(request, id):
    if request.method == "POST":
        name = request.POST["name"]
        contact = request.POST["contact"]
        gender = request.POST["gender"]
        date = request.POST["date"]
        time = request.POST["time"]
        reason = request.POST["reason"]

        update_appointment(id, name, contact, gender, date, time, reason)

        return redirect("list_appointments")

def delete(request, id):
    delete_appointment(id)
    return redirect("list_appointments")