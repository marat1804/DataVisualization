import matplotlib.pyplot as plt

squares = []
input_values = []
for i in range(10):
    input_values.append(i)
    squares.append(i**2)
plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
