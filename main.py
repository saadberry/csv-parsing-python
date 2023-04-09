"""program that takes a CSV, extracts the year and PPP factor, and writes to a new line"""
import csv
import json

# Opening the CSV file
with open('file.csv', encoding='utf-8-sig') as csv_file:
    # Read the CSV data
    csv_reader = csv.DictReader(csv_file)

    # Initializing an empty list to hold the data for each country
    country_data = []

    # Looping through each row in the CSV file
    for row in csv_reader:

        latest_year = None
        ppp_factor = None


        country_name = row['Country Name']

        # Looping through each year in the row
        for year in range(2021, 1960, -1):
            # Extracting the PPP factor for the year if it exists
            factor = row.get(str(year), None)

            # Store data if the PPP factor is not empty + year is the latest
            if factor and (latest_year is None or year > int(latest_year)):
                latest_year = str(year)
                ppp_factor = factor


        if latest_year and ppp_factor:
            country_data.append({
                'Country Name': country_name,
                'Latest Year': latest_year,
                'PPP factor': ppp_factor
            })
            # country_data.append("/n")

    # Writing the country data to a JSON file
    with open('country_data.json', 'w') as json_file:
        print('writing to new file')
        json.dump(country_data, json_file, indent=4, separators=(',', ': '))
        # json_file.write('\n')
