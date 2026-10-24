from django.http import JsonResponse

def saludo(request):
    data = {
        "status": "success",
        "mensaje": "¡Hola, Adrian!"
    }
    return JsonResponse(data)