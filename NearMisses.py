# Title- Looking for Fermat's Last Theorem Near Misses
# Filename- NearMisses.py
# Necessary files- N/A
# Created external files- NearMisses.exe which is an executable for windows
# Name- Amar Babu Ganta
# Email- AmarBabuGanta@lewisu.edu
# Course and Sections- Software Engineering- 003
# Date- Nov 18 2022
# Explanation- This Program helps an interactive user search for near misses
#               of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
#               are positive integers, 2< n <12, 10 <= x <= k, and 10 <= y <= k
# Resource- N/A
# Programming language- Python 3.10.3

def calculate_misses(n, k):
    """
    Calculate near misses using of Fermat's Last Theorem formula
    
    Calculate x^n + y^n = z^n, and then look for the minimum miss for which
    z^n < (x^n + y^n) < (z+1)^n satisfies. Find out which one (either z^n or (z+1)^n) is
    closer to (x^n + y^n), and determine the miss as the smallest of these two 
    values: [(x^n + y^n) - z^n] or [(z+1)^n- (x^n + y^n)]. Then get the
    RELATIVE size of the miss divide that miss by (x^n + y^n) and print the values

    """

    relative_miss = -1
    # Outer loop for first variable x of function x^n + y^n = z^n
    for x in range(10, k):
        # loop for y
        for y in range(10, k):
            # calculate (x^n + y^n) using python's built in pow method
            xysum_pow = pow(x, n) + pow(y, n)
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow)
            relative_miss_temp = miss / xysum_pow

            if relative_miss_temp < relative_miss or relative_miss == -1:
                relative_miss = relative_miss_temp
                print("\nx = {}      y = {}      z = {}       Miss = {}      Relative Miss = {}%".format(x, y, z, miss, round(relative_miss*100,2)))
    # print the final 
    print("\nFinal result for misses- \n") 
    print("x = {}      y = {}      z = {}       Miss = {}      Relative Miss = {}%".format(x, y, z, miss, round(relative_miss*100,2)))
           
if __name__ == "__main__":
    """
    Get the input of n(power) and k(limit) from user then call the calculate function
    """
    n = int(input("Exponent value,n= "))
    while n<3 or n>11:
        # check if n is bigger than 2
        n = int(input("Enter Exponent value bigger than 2 and less than 11= "))

    k = int(input("Limit value,k= "))
    while k<11:
        # check if k is bigger than 10
        k = int(input("Enter Limit Value bigger than 10= "))
    calculate_misses(n, k)
    tmp = input("Prees Enter for exit...")