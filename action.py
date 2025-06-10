import agentflow as af

async def handle():
    longitude = af.param("longitude")
    latitude  = af.param("latitude")

    return await af.request('https://api.open-meteo.com/v1/forecast',
        params = { 'longitude': longitude, 'latitude': latitude,
            'current_weather': True })
