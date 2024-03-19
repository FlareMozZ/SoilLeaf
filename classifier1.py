from taipy.gui import Gui, notify
from httpx import Client

def latitude(place):
    with Client() as client:
        response = client.get(
            url="https://api-test.openepi.io/geocoding/",
            params={"q": place},
        )

        data = response.json()

        # prints the coordinates of the first result
        return data["features"][0]["geometry"]["coordinates"][1]
    
def longitude(place):
    with Client() as client:
        response = client.get(
            url="https://api-test.openepi.io/geocoding/",
            params={"q": place},
        )

        data = response.json()

        # prints the coordinates of the first result
        return data["features"][0]["geometry"]["coordinates"][0]

def country(place):
    with Client() as client:
        response = client.get(
            url="https://api-test.openepi.io/geocoding/",
            params={"q": place},
        )

        data = response.json()

        # prints the coordinates of the first result
        return data["features"][0]["properties"]["country"]




text = ""
lat = ""
long = ""
cntry = ""

# Definition of the page
page = """
# Geocoding Service

Place name: <|{text}|>

<|{text}|input|>

<|Get Coordinates|button|on_action=on_button_action|> <br/>
Latitude is: <|{lat}|> <br/>
Longitude is: <|{long}|> <br/>
country: <|{cntry}|> <br/>

"""

def on_button_action(state):
        state.lat = latitude(state.text)
        state.long = longitude(state.text)
        state.cntry = country(state.text)
        notify(state, 'info', f'The text is: {state.text}')
        notify(state, 'info', f'The text is: {state.cntry}')
        notify(state, 'info', f'The text is: {state.lat}')
        notify(state, 'info', f'The text is: {state.long}')
        state.text = ""

app = Gui(page=page)

if __name__ == "__main__":
    app.run(use_reloader=True)