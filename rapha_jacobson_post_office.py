'''
rapha_jacobson_post_office.py

Description: Post office program that calculates the price it will cost the user to ship any given 
package across any given zip code

Features: calculates price of package, calculates the distance a package will go

Log: 1.0

Bugs: 
'''

def determine_class(length, height, thickness):
    '''
    determines class of package                                                                  
    Args:
        length (int): length of package
        height (int): height of package
        thickness (int): thickenss of package
    Returns:
        package class in a string
    '''
    #using length, height and width to determine package types
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
    '''
    defines zones of zip codes
    Args:
        zip (string): replacement for either zip_start or zip_end (So i dont have to repeat code twice but rather just call the function with zip_start and zip_end later)
    Returns:
        the zone of a zip code the user enters
    '''
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
    '''
    assocates class of package and distance and assigns a cost
    Args:
        package_class (string) = class of package defined in determine_class function
        zip_distance (function) = function which returns the zone (in an int) of the package's zip code
    Returns:
        the zone of a zip code the user enters
    '''
    cost = 0
    zip_distance
    if package_class == "regular post card":
        cost = .20 + (.03*zip_distance)
    elif package_class == "large post card":
        cost = .37 + (.03*zip_distance)
    elif package_class == "envelope":
        cost = .37 + (.04*zip_distance)
    elif package_class == "large envelope":
        cost = .6 + (.05*zip_distance)
    elif package_class == "package":
        cost = 2.95 + (.25*zip_distance)
    elif package_class == "large package":
        cost = 3.95 + (.35*zip_distance)
    return cost

def main():

    distance = 0

    while True:
        data = input("what are the specs of your package?:")
        data_list = data.split(",")
        if len(data_list) != 5:
            print("Data must be 5 numeric values, comma separated.")
        else:
            #defining length, height, thickness, and zip start integers as the user's input and converting them to floats or integers
            length = float(data_list[0])
            height = float(data_list[1])
            thickness = float(data_list[2])
            zip_start = int(data_list[3])
            zip_end = int(data_list[4])
            
            #validating input to make sure specs are within and acceptable range to be mailiable
            if length + height + height + thickness + thickness > 130: 
                print("Package is unmailable because it is too large")
            elif length < 3.5 or height < 3.5 or thickness < .007:
                print("Package is unmailable because it is too small")
            elif zip_start < 1 or zip_start > 99999:
                print ("Pakcage is unmailable becasue the starting zip code is invalid") 
            elif zip_end < 1 or zip_end > 99999:
                print("Pakcage is unmailable becasue the end zip code is invalid")
            else:
                print("We will calculate the price of your package")
                
    
                package_type = determine_class(length, height, thickness)
                distance = abs(zip_distance(zip_start) - zip_distance(zip_end))
                

                price = cost_association(package_type, distance)
                print(f'{price:.2f}'.lstrip('0'))

        

main()
