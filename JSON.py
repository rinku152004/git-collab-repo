# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.
# Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
import json

# some JSON:
x = '{ "name":"Rinku", "age":22, "city":"Rajkot"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(y["name"])
print(y["city"])
print()


# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
z="Hetal Jambukiya"
a = json.dumps(z)
# b = json.loads(a)
print(a)
print()
# a Python object (dict):
x = {
  "name": "Hetal",
  "age": 21,
  "city": "Rajkot"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print()

print(json.dumps({"name": "Rinku", "age": 22}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print()

x = {
  "name": "Bhavna",
  "age": 25,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
# y = json.dumps(x)
y=json.dumps(x, indent=4,separators=(". ", " = "))

# the result is a JSON string:
print(y)
