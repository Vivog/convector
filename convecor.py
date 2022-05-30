"""Convector of:
мили (1 mile = 1609 m),
ярды (1 yard = 0.9144 m),
футы (1 foot = 30.48 cm),
дюймы (1 inch = 2.54 cm),
километры (1 km = 1000 m),
метры (m),
сантиметры (1 cm = 0.01 m)
миллиметры (1 mm = 0.001 m)"""



dict_con = {
"mile": 1609,
"yard": 0.9144,
"foot": 0.3048,#cm
"inch": 0.0254,#cm
"km": 1000,
"m": 1,
"cm": 0.01,
"mm": 0.001
}

def convect(str_input):
    arr_input = str_input.split()
    value = float(arr_input[0])
    in_dimension = float(dict_con[arr_input[1]])
    out_dimension = float(dict_con[arr_input[3]])
    rez = value * (in_dimension / out_dimension)
    return print("%.2e" % rez)



"""Input is string in format:
 15.5 mile in km
 Output is string in format:
 e with 2 symbols max after point"""
str_input = input()
convect(str_input)