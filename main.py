from mpmath import *

def main():
    ndigits = 3
    try:
      ndigits = int(input("How many digits for your PI(π)? "))
    except:
      print("Bad input, using default 3 digits PI(π)")
      ndigits = 3

    mp.dps = ndigits;
    mp.pretty = True
    print(f"here is your PI(π): {+pi}")

if __name__== "__main__":
  main()