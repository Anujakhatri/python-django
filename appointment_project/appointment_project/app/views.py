from django.shortcuts import render, redirect

# Create your views here.
from .db import create_table, create_appointment, read_appointments, update_appointment, delete_appointment

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
        # syntax = request.POST.get(key, default_value)
        name = request.POST.get("name", "").strip()
        contact = request.POST.get("contact", "").strip()
        gender = request.POST.get("gender", "Female")
        date = request.POST.get("date", "")
        time = request.POST.get("time", "")
        reason = request.POST.get("reason", "").strip()

        if name and contact and date and time:
            try:
                create_appointment(name, contact, gender, date, time, reason)
                return redirect("list_appointments")
            except Exception as e:
                error= f"Error creating appointment: {str(e)}"
                return render(request, "list_appointments")
        else:
            error = "Please fill in all required fields"
            return render(request, "list.html", {"error": error})

    return render(request, "list.html")

def list_appointments(request):
    try:
        appointments = read_appointments()
    except Exception as e:
        appointments = []
        error = f"Error loading appointments: {str(e)}"
        return render(request, "success.html", {"error": error, "appointments": []})
    return render(request, "success.html", {"appointments": appointments})

def update(request, id):
    create_table()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        contact = request.POST.get("contact", "").strip()
        gender = request.POST.get("gender", "Female")
        date = request.POST.get("date", "")
        time = request.POST.get("time", "")
        reason = request.POST.get("reason", "").strip()

        if name and contact and date and time:
            try:
                update_appointment(id, name, contact, gender, date, time, reason)
                return redirect("list_appointments")
            except Exception as e:
                error = f"Error updating appointment: {str(e)}"
                return render(request, "edit.html", {"error": error, "id": id})
        else:
            error = "Please fill in all required fields"
            return render(request, "edit.html", {"error": error, "id": id})
    return render(request, "edit.html", {"id": id})
def delete(request, id):
    try:
        delete_appointment(id)
    except Exception as e:
        print(f"Error deleting appointment: {str(e)}")
    return redirect("list_appointments")