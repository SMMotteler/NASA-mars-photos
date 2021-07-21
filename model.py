import requests

def getImageUrlFrom(query):
    my_nasa_api_response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera="+(query)+"&api_key=DEMO_KEY").json()
    my_nasa_image_url = my_nasa_api_response["photos"][0]["img_src"]
    return my_nasa_image_url
