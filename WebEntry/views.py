from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json

@api_view(["GET"])
def imageprocessfun(data):
    try:
        received_json_data = json.loads(data.body)
        # print(str(received_json_data))
        source_type_val = received_json_data['source_type']
        waste_type_val = received_json_data['waste_type']
        loc_type_val = received_json_data['loc_type']
        img_raw_val = received_json_data['img_raw']
        img_processed_val = received_json_data['img_processed']
        time_date_val = received_json_data['time_date']
        waste_char_val = received_json_data['waste_char']
        waste_shape_val = received_json_data['waste_shape']
        waste_status_val = received_json_data['waste_status']
        waste_prod_name_val = received_json_data['waste_prod_name']
        waste_prod_address_val = received_json_data['waste_prod_address']
        other_val = received_json_data['other']
        latitude_val = received_json_data['latitude']
        longitude_val = received_json_data['longitude']
        country_val = received_json_data['country']
        state_val = received_json_data['state']
        district_val = received_json_data['district']
        region_val = received_json_data['region']
        city_val = received_json_data['city']
        street_val = received_json_data['street']
        pincode_val = received_json_data['pincode']

        print(str(source_type_val))
        print(str(waste_type_val))
        print(str(loc_type_val))
        print(str(img_raw_val))
        print(str(img_processed_val))
        print(str(time_date_val))
        print(str(waste_char_val))
        print(str(waste_shape_val))
        print(str(waste_status_val))
        print(str(waste_prod_name_val))
        print(str(waste_prod_address_val))
        print(str(other_val))
        print(str(latitude_val))
        print(str(longitude_val))
        print(str(country_val))
        print(str(state_val))
        print(str(district_val))
        print(str(region_val))
        print(str(city_val))
        print(str(street_val))
        print(str(pincode_val))
        return JsonResponse("done", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

