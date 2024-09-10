dimension = input('''enter hieght,length,thickness, zip1, zip2 of your package:
                 ''').split(',')

height = dimension[0]
length = dimension[1]
thickness = dimension[2]
zip1 = dimension[3]
zip2 = dimension[4]

def get_size(height, length, thickness):
    height = float(height)
    length = float(length)
    thickness = float(thickness)
    if length >



#zip code code
zone_zip1 = 0
zone_zip2 = 0

def get_zip(zipcode, zone_zip):
    zipcode = int(zipcode)
    print(zipcode)
    if zipcode < 6999 and zipcode > 1:
        zone_zip = 1
    elif zipcode <19999 and zipcode > 7000:
        zone_zip = 2
    elif zipcode <35999 and zipcode > 20000:
        zone_zip = 3
    elif zipcode <62999 and zipcode > 36000:
        zone_zip = 4
    elif zipcode <84999 and zipcode > 63000:
        zone_zip = 5
    elif zipcode <99999 and zipcode > 85000:
        zone_zip = 6
    else:
        print("not a zipcode")
    
get_zip(zip1, zone_zip1)
get_zip(zip2, zone_zip2)
zone_hops = (abs(zone_zip1-zone_zip2))
print(zone_hops)
