# write a program for temperature converter

def temp_converter():
    temperature = float(input("Enter temperature in CELSIUS: "))
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}degree C is equal to {converted_temp} degree F")
    
temp_converter()