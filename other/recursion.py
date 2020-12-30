# Simple iterative algorithm
houses = ["Eric's House", "Kenny's House", "Kyle's House", "Stan's House",
          "Emily's House"]


def deliver_presents_iteratively():
    for house in houses:
        print("Santa delivering to: ", house)

# Simple recursive algorithm


def deliver_presents_recursively(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering to: ", house)
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

# A recursive function is a function defined in terms of itself via
# self-referential expressions. This means that the function will continue to
# call itself and repeat it's behaviour until some condition is met to return a
# result. All recursive functions share a common structure made up of two
# parts: base case adn recursive case

# Calculating the factorial of a number recursively


def factorial(n):
    # Base case: 1! = 1
    if n == 1:
        return 1
    # Recursive case: N! = n * (n-1)!
    else:
        return factorial(n - 1) * n
        print(factorial(n - 1) * n)


if __name__ == "__main__":
    deliver_presents_recursively(houses)
    factorial(6)
