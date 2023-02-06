car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
print(car.get("year"))

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
print(car.get("color"))

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car.get("model"))

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()


