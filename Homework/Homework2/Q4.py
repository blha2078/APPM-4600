import numpy as np
import matplotlib.pyplot as plt
import random

### PART A ###

# time vector t
t = np.arange(0, 30*np.pi, np.pi)
# cos vector
y = np.cos(t)

# calculate the sum
S = np.sum(t * y)
print("The sum is: " + str(S))


### PART B ###

# function to compute x-values of the parametric curve
def x_parametric_curve(theta, R, delta_r, f, p):
    return R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)

# same as above for y
def y_parametric_curve(theta, R, delta_r, f, p):
    return R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

# Range of theta vals
theta_values = np.linspace(0, 2 * np.pi, 1000)
# constants
R = 1.2
delta_r = 0.1
f = 15
p = 0

# calculating values for x and y
x_values = x_parametric_curve(theta_values, R, delta_r, f, p)
y_values = y_parametric_curve(theta_values, R, delta_r, f, p)

# plotting
plt.figure(figsize=(10,10))
plt.plot(x_values, y_values)
plt.title("Parametric Curve for R=1.2, δr=0.1, f=15, p=0")
plt.axis("equal")
plt.savefig("Q4b_first_fig.png")
# plt.show()

# creating second figure
plt.figure(figsize=(10,10))
# doing the same as above for 10 curves
for i in range(1, 11):
    # constants
    R = i
    delta_r = 0.05
    f = 2 + i
    p = random.uniform(0, 2)

    # calculating x and y
    x_values = x_parametric_curve(theta_values, R, delta_r, f, p)
    y_values = y_parametric_curve(theta_values, R, delta_r, f, p)

    # plotting for each curve
    plt.plot(x_values, y_values, label = 'R=' + str(R) + ', δr=' + str(delta_r) + ', f=' + str(f) + ', p=' + '{:.2f}'.format(p))

plt.title('Wavy Circles with Varying Parameters')
plt.legend()
plt.axis('equal')
plt.savefig('Q4b_second_fig.png')
# plt.show()