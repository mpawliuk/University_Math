import time
start = time.time()

# Modify this n.
n = 4 

a = 0
b = 1

#Right hand rule
def right(n):
    """Return the nth Riemann sum for x^2 on [0,1] using RHR."""
    delta = (b - a) / n
    return sum([delta * (a + (i) * delta)**2 for i in range(1, n + 1)])

#Left hand rule
def left(n):
    """Return the nth Riemann sum for x^2 on [0,1] using LHR."""
    delta = (b - a) / n
    return sum([delta * (a + (i - 1) * delta)**2 for i in range(1, n+1)])

# Display
print("The Righthand Riemann sum for n={} is {}".format(n, right(n)))
print("The Lefthand Riemann sum for n={} is {}".format(n, left(n)))

# Print the run time
print("Run time: {:.2f} seconds".format(time.time() - start))
