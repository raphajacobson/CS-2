import time

def validate_input(length, height, thickness, zip_start, zip_end):
    while True:
        data = input("what are the specs of your package?:")
        data_list = data.split(",")
        length = float(data_list[0])
        height = float(data_list[1])
        thickness = float(data_list[2])
        zip_start = int(data_list[3])
        zip_end = int(data_list[4])
        
        if length + height + height + thickness + thickness > 130: 
            print("Package is unmailable because it is too large")
        elif length < 3.5 or height < 3.5 or thickness < .007:
            print("Package is unmailable because it is too small")
        elif zip_start < 1 or zip_start > 99999:
            print ("Your starting zip code was invalid") 
        elif zip_end < 1 or zip_end > 99999:
            print("Your end zip code is invalid")
        else:
            print("We will calculate the price of your package")
            time.sleep(2)
            break

def determine_class(length, height, thickness):

    if length >= 3.5 and length <= 4.25 and height >= 3.5 and height <= 6 and thickness >= .007 and thickness <= .016:
        package_class = "regular post card"
    elif length > 4.25 and length < 6 and height > 6 and height < 11.5 and thickness >= .007 and thickness <= .015:
        package_class = "large post card"
    elif length >= 3.5 and length <= 6.125 and height >= 5 and height <= 11.5 and thickness > .016 and thickness < .25:
        package_class = "envelope"
    elif length > 6.125 and length < 24 and height >= 11 and height <= 18 and thickness >= .25 and thickness <= .5:
        package_class = "large envelope"
    elif length > 24 and height > 18 and thickness > .5 and length + height + height + thickness + thickness <= 84:
        package_class = "package"
    elif length + height + height + thickness + thickness > 84 and length + height + height + thickness + thickness <= 130:
        package_class = "large package"
    
    return package_class

def zip_distance(zip_start, zip_end):
    
    if zip_start >= 1 and zip_start <= 6999:
        zip_start_zone = 1
    elif zip_start >= 7000 and zip_start <= 19999:
        zip_start_zone = 2
    elif zip_start >= 20000 and zip_start <= 35999:
        zip_start_zone = 3 
    elif zip_start >= 36000 and zip_start <= 62999:
        zip_start_zone = 4
    elif zip_start >= 63000 and zip_start <= 84999:
        zip_start_zone = 5
    elif zip_start >= 85000 and zip_start <= 99999:
        zip_start_zone = 6
    elif zip_end >= 1 and zip_end <= 6999:
        zip_end_zone = 1
    elif zip_end >= 7000 and zip_end <= 19999:
        zip_end_zone = 2
    elif zip_end >= 20000 and zip_end <= 35999:
        zip_end_zone = 3
    elif zip_end >= 36000 and zip_end <= 62999:
        zip_end_zone = 4
    elif zip_end >= 63000 and zip_end <= 84999:
        zip_end_zone = 5
    elif zip_end >= 85000 and zip_end <= 99999:
        zip_end_zone = 6

    zip_distance = abs(zip_start_zone - zip_end_zone)
    return zip_distance

def main():
    length, height, thickness, zip_start, zip_end = float(),float(),float(),int(),int()
    validate_input(length, height, thickness, zip_start, zip_end)
    

    
    

main()

"""
1. make sure input is valid
    - Valid length, height, width, and zip codes
2. determine classes
    -determine specifics within class (or if mailiable at all)
        - Length
        - Height
        - Width
3. Zip code distance
    - Find difference between start and end zipcode
4. Cost association
    - using the class and zip code distance
5. Define the total cost
    - class cost + distance cost = total cost
6. Main
    - input package specs
    validate input()
    print(total_cost())
"""