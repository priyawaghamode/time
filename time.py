def timeConversion(country, t):
    dict1 = {"usa": +9.30,
             "canada": +9.30,
             "russia": +2.30,
             "japan": -3.30,
             "malysia": -2.30,
             "singapur": -2.30,
             "dubai": +1.30,
             "israel": -2.30,
             "germany": +3.30,
             "italy": +3.30,
             "england": +4.30}
    if country in dict1.keys():
        print("india:", t + dict1[country])
    else:
        print("country not present")


timeConversion("usa", 6.00)
timeConversion("japan", 6.00)

