import matplotlib.pyplot as plt
# provide data
intervals = ['5-10', '10-15','15-20','20-25','25-30']
frequencies = [20,30,25,15,10]
#creating the histogram
plt.bar(intervals, frequencies)
plt.xlabel('Filled Litters Interval')
plt.ylabel('Frequency')
plt.title('Histogram of number of lLiter of Gasoline Filled')
plt.show()