from django.shortcuts import render
from .zipcodetrigger import ZipCodeTrigger
# from .postcode import ShoppingParams

def shopping_type(postcode):
    pass


def home(request):
    different_city = False
    different_city_message = None
    invalid_postcode = False
    valid_postcode = False
    context = {}
    if request.POST:
        postcode = request.POST.get("postcode")
        find_coordinates = ZipCodeTrigger()
        origin_coordinates = find_coordinates.post_code_coordinates(postcode)
        coordinates_check = isinstance(origin_coordinates, dict)
        if origin_coordinates == 999:
            invalid_postcode = True
        elif not coordinates_check and origin_coordinates != 999:
            different_city = True
            different_city_message = origin_coordinates
        else:
            valid_postcode = True


        context = {
            "invalid_postcode": invalid_postcode,
            "different_city": different_city,
            "different_city_message": different_city_message,
            "valid_postcode": valid_postcode,
            "post_code": postcode
        }

    return render(request, "home.html", context)
