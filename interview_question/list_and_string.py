""" Reviers string"""

name = "sohel"
print(name[::-1])

name = "sohel shital pujari"
names = name.split(" ")
nm =([i[::-1] for i in names][::-1])

namedsdd = nm[0]+" "+nm[1]+" "+nm[2]
print(namedsdd)
