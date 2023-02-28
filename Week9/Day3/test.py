class MyClass:
  counter = 0

  @classmethod
  def add(cls, a):
    print(cls.counter)
    return cls.counter + a

my_class_add = MyClass.add(3)
print(my_class_add)

new_class = MyClass()
print(new_class.counter)
new_class.counter = 3
print(new_class.counter)

print(new_class.add(3))
