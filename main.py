import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    matched_countries = {}
    unmatched_countries = set()

    for code, name in plot_countries.items():
        if name in gdp_countries:
            matched_countries[code] = name
        else:
            unmatched_countries.add(code)

    return matched_countries, unmatched_countries

def build_map_dict_by_name(gdpfile, keyfield, yearfield):
    nested_dict = {}
    with open('C:\\Users\\user\\Downloads\\gdp.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                key = row[keyfield]
                nested_dict[key] = row[yearfield]
            except KeyError:
                continue

    return nested_dict

def render_world_map(gdpinfo, plot_countries, year, map_file):
    gdp_map, missing_countries, no_gdp_data = build_map_dict_by_name(gdpinfo['C:\Users\user\Downloads'], gdpinfo['country_name'], year)

    world_map = pygal.maps.world.World()
    world_map.title = f"GDP by Country for {year}"

    # Add countries with GDP data
    world_map.add('GDP', gdp_map)

    # Add missing countries
    world_map.add('Missing Data', list(missing_countries))

    # Add countries with no GDP data for the specified year
    world_map.add('No GDP Data', list(no_gdp_data))

    # Render the map to an SVG file
    world_map.render_to_file(map_file)

# Example usage
gdpinfo = {
    'gdpfile': 'gdp.csv',
    'country_name': 'Country Name',
    'separator': ',',
    'quote': '"',
    'min_year': 1960,
    'max_year': 2015,
    'footnote_indicator': 'Footnotes'
}

plot_countries = {
    'us': 'United States',
    'ca': 'Canada',
    'mx': 'Mexico',
    'gb': 'United Kingdom',
    'fr': 'France',
    # ...
}

year = '2010'
map_file = 'gdp_map.svg'

render_world_map(gdpinfo, plot_countries, year, map_file)