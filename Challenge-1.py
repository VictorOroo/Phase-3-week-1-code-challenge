#Defined a function that will convert time in 12 hour system to 24
def convert_12hr_to_24hr(time12):
#This will check if the time ends with AM and if the first two digits are 12
    if time12[-2:] == "AM" and time12[:2] == "12":
        return "00" + time12[2:-2] # this will replace 12 with 00 for midnight

#this will check if the time ends with "AM"
    elif time12[-2:] == "AM":
        return time12[:-2] # removes "AM"

#this checks if the time ends with "PM" and if the two digits are 12
    elif time12[-2:] == "PM" and time12[:2] == "12":
        return time12[:-2] #it will keep the same hours for noon
    
    else:
        hours = str(int(time12[:2]) +12)# adds 12 hrs to the given hours
        if hours == "24":
            hours = "00" #resets to 00 for midnight

        return hours + time12[2:5] # this will combine the new hours with the existing minutes and seconds
    
print(convert_12hr_to_24hr("08:30:00"))