import agentflow as af

async def handle(context):
    longitude = context["longtitude"]
    latitude  = context["latitude"]

    return await af.request('https://api.open-meteo.com/v1/forecast',
        params = { 'longitude': longitude, 'latitude': latitude,
            'current_weather': True })
