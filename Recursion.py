def factorial(n):
    if n  <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

houses = ["T house", "B house", "C house"]

def deliver_presents_recursively(houses):
    if len(houses) == 1:
        print("Delivering presents to", houses[0])

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        #first elf
        deliver_presents_recursively(first_half)
        #second elf
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)