import requests
import json
from simple_chalk import chalk
from tabulate import tabulate


class country:
    def __init__(self, name):
        self.name = name
    
    # curl --location --request GET 'https://api.covid19api.com/country/south-africa/status/confirmed'
    def get_covid_details(self):
        url = 'https://api.covid19api.com/summary'
        r = requests.get(url)
        t = filter(lambda x : x['Country'].lower() == self.name.lower(), r.json()['Countries'])
        countries = list(t)
        if len(countries )==0: return []
        # This is how you delete multiple keys in an dict object.
        final = {(k,v) for k, v in countries[0].items() if k not in ['Country', 'Slug', 'Premium']}
        return final


if __name__ == "__main__":
    
    print("------------------------------------------------")
    print(chalk.red.bold("COVID SCAPE!"))
    print("------------------------------------------------")
    print("\n")
    print("Please enter the country name.")
    country_input = input()
    print(f"Finding covid details for {country_input} ...")
    print("\n")
    c = country(country_input)
    output = c.get_covid_details()
    if len(output) > 0:
        # print(output)
        # print(tuple(output))
        print(chalk.green(tabulate(output)))
    else:
        print(chalk.red.bold (f"Country {country_input} details not found."))
        