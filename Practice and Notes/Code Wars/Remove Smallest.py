# my long winded solution
def remove_smallest(numbers):
    try:
        smallest = min(x for x in numbers)
        numbers.remove(smallest)
    except:
        numbers = []
    return numbers

# elegant solution
def remove_smallest2(numbers):
    if numbers:
        return numbers.remove(min(numbers))
    return numbers