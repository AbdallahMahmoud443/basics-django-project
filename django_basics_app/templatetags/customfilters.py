from django import template
from num2words import num2words
register = template.Library()


def first_five_upper(value):
    return value[:5].upper()

def first_n_upper(value,n):
    return value[:n].upper()

def lengthLimit(value,limit):
    if len(value) > limit:
        result = value[:limit] +"....." 
    else:
        result = value 
    return result

def addRating(value):
    if float(value) >= 4:
        return value + "-Excellent"
    elif float(value) >= 3:
        return float(value) + "-Very Good"
    elif value >= 1.5:
         return float(value) + "-Average"
    else:
        return float(value) + "-Poor"

def convertDigitToText(value):
    return num2words(value)


register.filter("firstfiveupper",first_five_upper)
register.filter("firstnupper",first_n_upper)
register.filter("lengthlimit",lengthLimit)
register.filter("addrating",addRating)
register.filter("numtotext",convertDigitToText)