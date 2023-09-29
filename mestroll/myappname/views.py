from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, render
from django.db import connection
from .models import Users
from .models import Classe
from .forms import ClasseForm


@csrf_exempt
@require_http_methods(["GET", "POST"])  # Allow both GET and POST requests
def test_view(request):
    if request.method == "GET":
        # Handle GET requests
        return HttpResponse("GET request received")

    if request.method == "POST":
        # Handle POST requests
        # You can access POST data from request.POST dictionary
        return HttpResponse("POST request received")

    # Handle other HTTP methods (e.g., PUT, DELETE) as needed
    return HttpResponse("Other request methods are not supported")


@csrf_exempt
@require_http_methods(["GET", "POST"])
def hello(request):
    if request.method == "GET":
        return HttpResponse("hello")


def fetch_users(request):
    # Fetch all user records from the "users" table using the custom model
    users = Users.objects.all()

    # You can serialize the data as needed
    user_data = [
        {"username": user.username, "email": user.email, "role": user.Role_name, "id": user.id} for user in users
    ]

    return JsonResponse({"users": user_data})

# @csrf_exempt
# @require_http_methods(["GET", "POST"])
def fetch_user_by_email(request):
    # Get the email parameter from the POST request
    input_email = request.POST.get("email")

    # Query the database for a user with the matching email
    user = get_object_or_404(Users, email=input_email)
    # Serialize the user data as needed
    user_data = {
        "username": user.username,
        "email": user.email,
        "role": user.Role_name,
        "id": user.id
    }

    return JsonResponse({"user": user_data})


@csrf_exempt
@require_POST
def call_insert_class1(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        classroom = request.POST.get("classroom")
        lat = float(request.POST.get("lat"))
        long = float(request.POST.get("long"))
        elevation = float(request.POST.get("elevation"))

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT sign_ins(%s, %s, %s, %s, %s)", [user_id, classroom, lat, long, elevation])
                result = cursor.fetchone()[0]

            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
@require_http_methods(["GET", "POST"])  # Allow both GET and POST requests
def call_insert_class(request):   # inserting class sign in
    # print("SELECT class_signin(%s, %s, %s, %s, %s)")
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        classroom = request.POST.get("classroom")
        lat = float(request.POST.get("lat"))
        long = float(request.POST.get("long"))
        elevation = float(request.POST.get("elevation"))

        print("SELECT class_signin(%s, %s, %s, %s, %s)" % (user_id, classroom, lat, long, elevation))

        print(f"user_id: {user_id}")
        print(f"classroom: {classroom}")
        print(f"lat: {lat}")
        print(f"long: {long}")
        print(f"elevation: {elevation}")

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT class_signin(%s, %s, %s, %s, %s)" % (user_id, classroom, lat, long, elevation))
                result = cursor.fetchone()[0]

            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=500)
    else:
        x = dict(request.GET)
        print(x)
        user_id = x.get("user_id")[0]
        classroom = x.get("classroom")[0]
        lat = x.get("lat")[0]
        long = x.get("long")[0]
        elevation = x.get("elavation")[0]

        print("SELECT class_signin(%s, %s, %s, %s, %s)" % (user_id, classroom, lat, long, elevation))

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT class_signin(%s, %s, %s, %s, %s)" % (user_id, classroom, lat, long, elevation))
                result = cursor.fetchone()[0]

            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=500)
        
    return JsonResponse({"error": "Invalid request method"}, status=405)





@csrf_exempt
@require_http_methods(["GET", "POST"])  # Allow both GET and POST requests
def call_insert_apology(request):   # inserting class sign in
    # print("SELECT class_signin(%s, %s, %s, %s, %s)")
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        reason = request.POST.get("reason")
        remark = request.POST.get("remark")
        lat = float(request.POST.get("lat"))
        long = float(request.POST.get("long"))
        elevation = float(request.POST.get("elevation"))

        print("SELECT insert_into_sickleave(%s, %s, %s, %s, %s)" % (user_id, reason, remark, lat, long, elevation))

        print(f"user_id: {user_id}")
        print(f"reason: {reason}")
        print(f"remark: {remark}")
        print(f"lat: {lat}")
        print(f"long: {long}")
        print(f"elevation: {elevation}")

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT insert_into_sickleave(%s, %s, %s, %s, %s, %s)" % (user_id, reason, remark, lat, long, elevation))
                result = cursor.fetchone()[0]

            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=500)
    else:
        x = dict(request.GET)
        print(x)
        user_id = x.get("user_id")[0]
        reason = x.get("reason")[0]
        remark = x.get("remark")[0]
        lat = x.get("lat")[0]
        long = x.get("long")[0]
        elevation = x.get("elavation")[0]

        print("SELECT class_signin(%s, %s, %s, %s, %s)" % (user_id, reason, remark, lat, long, elevation))

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT insert_into_sickleave(%s, %s, %s, %s, %s, %s)" % (user_id, reason, remark, lat, long, elevation))
                result = cursor.fetchone()[0]

            return JsonResponse({"result": result})
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=500)
        
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
@require_http_methods(["POST", "GET"])
def testd(request):
    if request.method == "GET":
        if "id" in request.GET:
            print("yo")
        else:
            print("oo")
    else:
        print(request.method, id)
        print("ITS WORKING HERE")

    return JsonResponse({"message": "working"}, status=200)
