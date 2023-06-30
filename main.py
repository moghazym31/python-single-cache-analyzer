import math
import re

hit = 0
miss = 0
time = 0
AMAT = 0


def remove_first_group(m):
    return m.group(2)


def remove_second_group(m):
    return m.group(1)


with open("data.txt", "r") as f:
    inputted_addresses = f.read().splitlines()


print('Enter the number of cycles needed to access the cache (between 1 and 10) : ')
cycles_needed_to_access_cache = input()

while (int(cycles_needed_to_access_cache) > 10 or int(cycles_needed_to_access_cache) < 1):
    print('Invalid number of cycles......Please enter a number between 1 and 10  : ')
    cycles_needed_to_access_cache = input()


with open("data.txt", "r") as f:
    inputted_addresses = f.read().splitlines()


array_of_MEM_tags = []
array_of_CACHE_tags = []

array_of_MEM_indices = []
array_of_last_n_digits = []

CACHE = []

print('Enter the cache size : ')
cache_size = input()  # S

print('Enter the line size : ')
line_size = input()  # L

no_of_CACHE_blocks = int(cache_size) / int(line_size)  # C = S / L


displacement = str(bin(int(math.log(int(line_size), 2)))).replace('0b', '')

x = 0
for i in inputted_addresses:
    org_string = i
    size = 32

    m = "(.*)(.{"+str(len(displacement))+"}$)"
    index_and_tag = re.sub(m, remove_second_group, i)
    size_of_index = int(math.log(int(no_of_CACHE_blocks), 2))

    m = "(.*)(.{"+str(size_of_index)+"}$)"
    array_of_MEM_tags.append(re.sub(m, remove_second_group, index_and_tag))

    m = "(^.{"+str(32-len(displacement)-size_of_index)+"})(.*)"
    array_of_MEM_indices.append(re.sub(m, remove_first_group, index_and_tag))

    while len(array_of_MEM_indices[x]) < int(math.log(int(no_of_CACHE_blocks), 2)):
        array_of_MEM_indices[x] = '0' + str(array_of_MEM_indices[x])

    x = x + 1


array_of_CACHE_tags = []
array_of_valid_bits = []

# CACHE Loop
for i in range(int(no_of_CACHE_blocks)):
    CACHE.append(bin(i).replace('0b', ''))
    while len(CACHE[i]) < int(math.log(int(no_of_CACHE_blocks), 2)):
        CACHE[i] = '0' + CACHE[i]

    array_of_valid_bits.append('N')
    array_of_CACHE_tags.append(0)


for i in range(len(inputted_addresses)):
    for j in range(int(no_of_CACHE_blocks)):
        if array_of_MEM_indices[i] == CACHE[j]:
            if (array_of_MEM_tags[i] == array_of_CACHE_tags[j]):
                hit = hit + 1
                array_of_valid_bits[j] = 'Y'

            else:
                array_of_CACHE_tags[j] = array_of_MEM_tags[i]
                array_of_valid_bits[j] = 'Y'
                miss = miss + 1
    print('\n')
    print('Index'+' |  '+'V'+'   | '+'Tag')
    print('-------------------------------------------')
    for k in range(int(no_of_CACHE_blocks)):
        print(CACHE[k] + '   |  ' + array_of_valid_bits[k] +
              '   |  ' + str(array_of_CACHE_tags[k]))


print('\n')

print('The number of memory accesses :  ' + str(miss))
print('The hit ratio :  ' + str(float(hit)/float(hit + miss)))
print('The miss ratio :  ' + str(float(miss)/float(hit + miss)))

miss_rate = (miss/(hit+miss))
miss_time = 100
hit_time = cycles_needed_to_access_cache

AMAT = float(hit_time) + float(miss_rate) * float(miss_time)

print('The average memory access time : ' + str(AMAT) + ' cycles')
print('The number of the cache accesses : ' + str(hit))
print('The total number of accesses : ' + str(hit + miss))
print('\n')
