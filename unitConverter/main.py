coversion = {"cm": 1, "in": 2.54, "mi": 160934, "km": 100000, "kg": 1, "lb": 0.453592}

while(True):
  startUnit = input("select the input unit for conversion: ").lower()
  
  if(startUnit == "in" or startUnit == "mi" or startUnit == "cm" or startUnit == "km"):
    while(True):
      endUnit = input("select the output unit for conversion: ").lower()
      if((endUnit == "in" or endUnit == "cm" or endUnit == "km" or endUnit == "mi") and endUnit != startUnit):
        break
      print("please enter a valid output unit from this list ('cm', 'in', 'km', 'mi')")
    break
  elif(startUnit == "kg" or startUnit == "lb"):
    if(startUnit == "kg"):
      endUnit = "lb"
    else:
      endUnit = "kg"
    break
  print("please enter a vaild input from this list ('cm', 'in', 'mi', 'km', 'kg', 'lb')")
print("converting from", startUnit, "to", endUnit)
while True:
  try:
    input = float(input("please enter a value to convert: "))
    break
  except:
    print("please input a valid number")

print((input * coversion[startUnit]) / coversion[endUnit], endUnit)
