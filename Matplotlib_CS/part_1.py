from matplotlib import pyplot as plt

# show all styles
# print(plt.style.available)
# plt.style.use("tableau-colorblind10")
plt.xkcd()

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
# after axes format string possible, barely readable
plt.plot(ages_x, dev_y, '1k--', label='All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# explicit as arguments
plt.plot(ages_x, py_dev_y, color='#5a7d9a', linestyle="-", marker='o', label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, label='JavaScript')


# name for axes and title
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by age')

# one possibility aof labeling the plots
# plt.legend (needs list in order of adding lines to the plot)
# ex: plt.legend(['AllDevs', 'Python'])
# better is adding label directly to the plot and call legend empty
plt.legend()

# show a grid, if not included in style
# plt.grid(True)

# fixes the padding
plt.tight_layout()

# save as png
plt-plt.savefig('plot.png')

plt.show()
