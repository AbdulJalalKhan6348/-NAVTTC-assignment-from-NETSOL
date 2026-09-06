fruits = ("Bnana","Orange","Apple" , "Mango")
it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

#containing a sequence of characters
txt = "Bnana"
it = iter(txt)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#Looping Through an Iterator
name =("Jalal","Jamal","Ghafar",)
for n in name:
    print(n)

#StopIteration
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#Python Datetime
import datetime
x = datetime.datetime.now()
print(x)
#Date Output
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


import datetime

x = datetime.datetime.now()

print(x)
#json
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

#Convert from Python to JSON
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)

