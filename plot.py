import matplotlib.pyplot as plt

cores = [1, 2, 3, 4, 5, 6, 7, 8]
time = [1.1249938011169434,
        1.1120054721832275,
        0,
        1.221057415008545,
        0,
        0,
        1.1028337478637695,
        1.2261834144592285]

plt.plot(cores, time)

# Add labels and title
plt.xlabel('Number of Cores')
plt.ylabel('Time(s)')

# Show the plot
plt.show()