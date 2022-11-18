# libraries (pandas, numpy and statistics) which be used in the program. 
import pandas as pd
import numpy as np
import statistics

# get the excel file and assign the size of the data.
data = pd.read_excel("egitimbolumveri.xlsx")
number_of_rows = data['Sıra'].size

# print average, mod, median, standart deviation, variance, first and third quartile and inter quantile range of each column.
def print_statistics(column_name):
    our_list = list()
    for row_number in range(number_of_rows):
        our_list.append(data[column_name][row_number])

    print('Column: ' + str.upper(column_name) + '\n')
    print('Average: ' + str(np.average(our_list)))
    print("Mod: " + str(statistics.mode(our_list)))
    print('Median: ' + str(np.median(our_list)))
    print('Standart deviation: ' + str(np.std(our_list)))
    print('Variance: ' + str(np.var(our_list)))
    first_quantile = np.quantile(our_list, 0.25)
    third_quantile = np.quantile(our_list, 0.75)
    print('1st quartile: ' + str(first_quantile))
    print('3rd quartile: ' + str(third_quantile))
    print('Inter quartile range' , str(third_quantile-first_quantile))

    print('-'*25)

# call the function with column parameters.
print_statistics('Yaş')
print_statistics('SMK Süresi')
print_statistics('Vize')
print_statistics('Final')
print_statistics('Final Kategori')