import psutil

battery = psutil.sensors_battery()

percentage = str(battery.percent)


print("Your Battery Percentage is" + percentage + "%")

#Status- running