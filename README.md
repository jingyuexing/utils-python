# Python Utils


- [Cookie](utils/Cookies/__init__.py)
- [Query](utils/Query/__init__.py)
- [memo](utils/func.__init__.py)
- [pipeline](utils/func.__init__.py)
- [compose](utils/func.__init__.py)
- [times](utils/func.__init__.py)


- **Cookie**

```py
@Cookie
class People
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

p = People("Alex",21,"MEN")
print(p) # name=Alex;age=21;gender=MEN
```

- **Query**

```py
@Query
class People
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

p = People("Alex",21,"MEN")
print(p) # name=Alex&age=21&gender=MEN
```

- **pipeline**

Pipeline takes the output of the previous function as the input for the next one.

```py
def one(x):
    return x * x
def two(x):
    return x * 2
def three(x):
    return x * 3
@pipeline(one,two,three) # The execution order is: one(x) -> two(one(x)) -> three(two(one(x)))
def p(x):
    print(x)
```

- **compose**

Compose is a concept in functional programming used to combine multiple functions into a new function. Its primary functionality is to create a function that sequentially executes the given functions in the specified order, passing the output of each function as the input to the next one.

The execution order of a composed function is from right to left, meaning that the function on the far right executes first. Its output serves as the input for the next function to the left, continuing this sequence until all functions have been executed.

```py
def one(x):
    return x * x
def two(x):
    return x * 2
def three(x):
    return x * 3
@compose(one,two,three) # The execution order is: one(two(three(x)))
def p(x):
    print(x)
```

- **times**

times will cause the function to execute a specified number of times, and beyond that limit, the function will no longer execute.

```py

@times(3)
def hello():
    print("hello")


hello() # will print "hello"
hello() # will print "hello"
hello() # will print "hello"
hello() # reutrn None

```
