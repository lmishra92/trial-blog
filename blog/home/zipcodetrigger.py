import requests
import googlemaps

class ZipCodeTrigger(object):
    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.api_key = 'AIzaSyDqtlsHxt_jm32r-4GPRc3WqiolXG6o0jo'
        self.client = googlemaps.Client(self.api_key)

        self.path = None
        self.city = None
        self.street = None
        self.coordinates = None
        self.google_response = None

    def get_params(self, postcode):
        params = {'key': self.api_key, 'address': postcode}
        return params

    def get_exact_coordinates(self, address):
        params = self.get_params(address)
        self.google_response = requests.get(self.url, params=params, verify=True)
        return self.google_response.json()["results"]

    def postcode_validity_check(self, postcode):
        sanity_list = {"number": False, "letters": False, "digits": False}
        if len(postcode) == 6:
            sanity_list["digits"] = True
        if postcode[0:3].isnumeric():
            sanity_list["number"] = True
        if not postcode[-2:].isnumeric():
            sanity_list["letters"] = True
        if all(value == True for value in sanity_list.values()):
            return True
        else:
            return False

    def get_google_info(self, postcode):
        params = self.get_params(postcode)
        self.google_response = requests.get(self.url, params=params, verify = True)
        return self.google_response

    def get_city(self, postcode):
        postcode = ''.join(postcode.split())
        sanity_check = self.postcode_validity_check(postcode)
        if sanity_check:
            google_info = self.get_google_info(postcode)
            if self.google_response.status_code == 200:
                try:
                    for info in self.google_response.json()["results"][0]["address_components"]:
                        if 'locality' in info["types"]:
                            self.city = info["long_name"]
                            return self.city
                except Exception as e:
                    print(e)
                    return 999
            elif self.google_response.status_code in (400, 401, 403, 415, 429):
                return "Our Zip Code tracker is under maintenance. Sorry for the inconveneience"
        else:
            return 999

    def post_code_coordinates(self, postcode):
        postcode = ''.join(postcode.split())
        sanity_check = self.postcode_validity_check(postcode)
        if sanity_check:
            city = self.get_city(postcode)
            if city == 'Rotterdam':
                google_info = self.get_google_info(postcode)
                if google_info.status_code == 200:
                    self.coordinates = google_info.json()["results"][0]["geometry"]["location"]
                    return self.coordinates
                elif google_info.status_code in (400, 401, 403, 415, 429):
                    return "Our Zip Code tracker is under maintenance. Sorry for the inconveneience"
            else:
                return city
        else:
            return 999

    def distance_matrix(self,origin, destination):
        return self.client.distance_matrix(origin,destination)["rows"][0]["elements"][0]["distance"]