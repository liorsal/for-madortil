import math 
def lcm(numbers):
  lcm = numbers[0]
  for number in numbers[1:]:
    lcm = lcm * number // math.gcd(lcm, number)
  return lcm


def main():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(f"The least common multiple of {numbers} is {lcm(numbers)}.")


if __name__ == "__main__":
  main()