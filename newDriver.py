def registerNewDriver(state, lp, fname, lname, email, number, bday):
    new_driver = str(state) + "," + str(lp) + "," + str(fname) \
        + "," + str(lname) + "," + str(email) + "," + \
        str(number) + "," + str(bday) + "\n"

    with open("driverinfo.csv", "a") as zh:
        zh.write(new_driver)
