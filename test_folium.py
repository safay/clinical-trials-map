import folium
import json
import random
import pandas as pd

world_geo = '/Users/safay/clinical-trial-mapper-data/world-110m.json'


json_data=open(world_geo).read()
data = json.loads(json_data)
num_countries = len([country['id'] for country in data['objects']['countries']['geometries']])

nation_values = random.sample(range(1, num_countries * 2), num_countries)
nation_ids = [country['id'] for country in data['objects']['countries']['geometries']]

nation_data = pd.DataFrame({'ids':nation_ids, 'values': nation_values})


def build_test_map(filepath):
    map = folium.Map(location=[45.5236, -122.6750], zoom_start=3, tiles='Mapbox Bright')
    map.choropleth(geo_path=world_geo, data=nation_data,
                 columns=['ids', 'values'],
                 fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
                 key_on='feature.id',
                 legend_name='Unemployment Rate (%)',
                 topojson='objects.countries')
    map.save(filepath)






test_map_path = '/Users/safay/clinical-trial-mapper-data/test.html'

