from django.http import JsonResponse


def error_404_view(request, exception):
    return JsonResponse({'status_code': 404,
                         'Error': 'The requested url is not found'
                         }, status=404)


def error_500_view(request):
    return JsonResponse({'status_code': 500,
                         'Error': 'something went wrong, Please try later'
                         }, status=500)
