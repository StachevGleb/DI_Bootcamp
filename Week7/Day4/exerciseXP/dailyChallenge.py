# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Buit-in exceptions of Python


try:
    x = 5/0
except ZeroDivisionError:
        print("Oops! It's infinity")