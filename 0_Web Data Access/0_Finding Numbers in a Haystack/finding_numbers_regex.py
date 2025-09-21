import re
hand = open('regex_sum_2070614.txt')
#hand = open('regex_sum_42.txt ')
print(sum([int(i) for i in re.findall('[0-9]+', hand.read())]))

#read() read all file and returns jut one big string, out of loop and reading all new lines etc


