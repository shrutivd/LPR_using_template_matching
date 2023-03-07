import csv

def getDriverName(state, license_plate):
    """
    Get the driver's name associated with the
    given license plate
    """
    # organize all driver information
    driver_info = {}
    with open('driverInfo.csv', newline='') as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            driver_info[(row[0],row[1])] = [row[2], row[3], row[4], row[5]]

    name = driver_info[(state, license_plate)][0]
    email = driver_info[(state, license_plate)][1]
    number = driver_info[(state, license_plate)][2]
    bday = driver_info[(state, license_plate)][3]
    
    # return driver's information
    return name, email, number, bday
