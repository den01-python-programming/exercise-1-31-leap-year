# Exercise 1.31 - Leap Year

A year is a leap year if it is divisible by 4. However, if the year is divisible by 100, then it is a leap year only when it is also divisible by 400.

Write a program that reads a year from the user, and checks whether or not it is a leap year.

```plaintext
Give a year: 
*2011*
The year is not a leap year.
```

```plaintext
Give a year: 
*2012*
The year is a leap year.
```

```plaintext
Give a year: 
*1800*
The year is not a leap year.
```

```plaintext
Give a year: 
*2000*
The year is a leap year.
```

**Hint 1:** *The divisibility by a particular number can be checked using the modulo operator, aka `%`, in the following way.*

```python
number = 5

if (number % 5 == 0):
    print("The number is divisible by five!")

if (number % 6 != 0):
    print("The number is not divisible by six!")
```


```plaintext
The number is divisible by five!
The number is not divisible by six!
```

**Hint 2:** *Think of the problem as a chain of if, elif, elif, ... comparisons, and start building the program from a situation in which you can be certain that the year is not a leap year.*

```python
number = int(input("Give a year:"))

if (number % 4 != 0):
    print("The year is not a leap year.")

elif (...):
    ...
```
