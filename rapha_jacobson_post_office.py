import time

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

def zip_distance(zip):

    
    if zip >= 1 and zip <= 6999:
        return 1
    elif zip >= 7000 and zip <= 19999:
        return 2
    elif zip >= 20000 and zip <= 35999:
        return 3 
    elif zip >= 36000 and zip <= 62999:
        return 4
    elif zip >= 63000 and zip <= 84999:
        return 5
    elif zip >= 85000 and zip <= 99999:
        return 6
    else:
        pass


def cost_association(package_class, zip_distance):
    cost = 0
    zip_distance
    if package_class == "regular post card":
        cost += .20
        cost += .03 * zip_distance
    elif package_class == "large post card":
        cost += .37
        cost += .03 * zip_distance
    elif package_class == "envelope":
        cost += .37
        cost += .04 * zip_distance
    elif package_class == "large envelope":
        cost += .60
        cost +=.05 * zip_distance
    elif package_class == "package":
        cost += 2.95
        cost += .25 * zip_distance
    elif package_class == "large package":
        cost += 3.95
        cost += .35 * zip_distance

    return cost

def main():

    distance = 0
    package_class = ""

    while True:
        data = input("what are the specs of your package?:")
        data_list = data.split(",")
        length = float(data_list[0])
        height = float(data_list[1])
        thickness = float(data_list[2])
        zip_start = int(data_list[3])
        zip_end = int(data_list[4])
        
        if length + height + height + thickness + thickness > 130: 
            time.sleep(2)
            print("Package is unmailable because it is too large")
        elif length < 3.5 or height < 3.5 or thickness < .007:
            time.sleep(2)
            print("Package is unmailable because it is too small")
        elif zip_start < 1 or zip_start > 99999:
            print ("Your starting zip code was invalid") 
        elif zip_end < 1 or zip_end > 99999:
            time.sleep(2)
            print("Your end zip code is invalid")
        else:
            print("We will calculate the price of your package")
            time.sleep(2)
            break 
    

    start = zip_distance(zip_start)
    end = zip_distance(zip_end)
    distance = abs(zip_distance(zip_start) - zip_distance(zip_end))
    print(type(zip_distance))
    #cost_association(package_class, zip_distance)

        

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
