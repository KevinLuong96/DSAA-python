# R-1.1
# Returns true if n is a multiple of m else false
def multiple(n,m):
  return True if m%n ==0 else False;


# R-1.3
# returns the smallest and largest numbers in the form of a tuple of length 2
def minmax(data):
  min = max = None;
  for number in data:
    if not min or number < min: min = number
    elif not max or number > max : max = number 
  return min,max

# R 1.5
# using comprehension syntax return the value of the sum of squares of all 
# integers less than n
def sumLowerSquares(n):
  return sum([k*k for k in range(n)]);

# R 1.11
# Using list comprehension produce [1,2,4,8,16,32,64] etc
def doublingList(n):
  return [pow(2,k) for k in range(n)]

# C 1.14
# Takes a sequence of integers and determines if there is a distinct pair
# which has an odd product
def oddProductInSequence(seq):
  # if there are two distinct odd numbers, the criterion is filled
  return True if len([k for k in seq if k %2 != 0]) >1 else False

# C 1.15
# Taking a sequence, return true if all values are distinct
def uniqueSequence(seq):
  return True if len(set(seq)) == len(seq) else False

# C 1.18
# using list comprehension produce the list [0,2,6,12,20 ...]
def produceList(n):
  return [k * (k+1) for k in range(n)];

# C 1.22
# Return the dot product of two equal length int arrays
def dotProduct(a,b):
  return sum([a[k]*b[k] for k in range(len(a))]);








