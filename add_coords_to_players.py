import csv

# Create mapping, country name to (latitude, longitude)
country_coords = {}
with open("country-coord.csv", mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        country = row["Country"].strip()
        lat = row["Latitude (average)"].strip()
        lng = row["Longitude (average)"].strip()
        country_coords[country.lower()] = (lat, lng)

# Process nodes, create a new version with the coords
with open("nodes_gephi.csv", mode='r', encoding='utf-8-sig') as file_in, open("nodes_gephi_with_coords.csv", mode='w', newline='', encoding='utf-8') as file_out:
    reader = csv.DictReader(file_in)
    # Add new fields for the output
    fieldnames = reader.fieldnames + ["lat", "lng"]
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        location = row["location"].strip()
        coord = country_coords.get(location.lower())

        if (coord):
            row["lat"], row["lng"] = coord
        else:
            row["lat"], row["lng"] = "", ""
        writer.writerow(row)

print("Done adding, outputted to the target file")