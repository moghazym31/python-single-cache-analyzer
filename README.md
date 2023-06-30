# Cache Performance Analyzer

## Overview

This is a cache performance analyzer implemented in Python. It calculates various metrics such as the number of hits, misses, hit ratio, miss ratio, average memory access time, number of cache accesses, and total number of accesses.

## Usage

1. Edit memory addresses from `data.txt`.
2. Run program by executing 'python main.py' in the terminal or command prompt.
3. Provide the number of clock cycles needed to access the cache (between 1 and 10).
4. Enter the cache size and line size.
5. The program will process each memory address and simulate the cache system.
6. After processing all addresses, it will display the cache state, including the index, valid bit, and tag.
7. Finally, it will present the performance metrics, including the number of memory accesses, hit ratio, miss ratio, average memory access time, number of cache accesses, and total number of accesses.

## Implementation Details

The implementation consists of the following steps:

1. Read the user-provided memory addresses from a text file.
2. Obtain user inputs for the number of clock cycles, cache size, and line size.
3. Extract tags and indices from each memory address using regular expressions.
4. Generate the cache structure and initialize valid bits and tags.
5. Process each memory address and compare the indices and tags with the cache entries.
6. Update hit and miss counts accordingly and modify cache entries as necessary.
7. Display the cache state after each memory address is processed.
8. Calculate performance metrics based on hit, miss, and user inputs.
9. Present the performance metrics in a clear and concise format.

## Sample Input

```
10101010101010101010101111010101
11111110000011111000001111110001
10010011100110011010111010101001
01101000000111001101100001101011
10000000000000111111111111101001
01111111111111111101100001111011
10010011100110011010111010101001
11111111111111111111100000010101
10000000000011111111111111100000
10010011100110011010111010101001
01101000000111001101100001101011
01110101111111111101100001111011
11111111110101010101011111010101
01100101011111111111100001111011
10010011111111111110111010101001
01101000000111001101100001101011
01101010101111101011100001111011
10010011100110011010111010101001
11111010101010101001010101010101
11111111110101010101011111010101
```

Cycles : 5

Cache size : 32

Line size : 4

## Sample Output

```

Index |  V   | Tag
-------------------------------------------
000   |  N   |  0
001   |  N   |  0
010   |  N   |  0
011   |  N   |  0
100   |  N   |  0
101   |  Y   |  101010101010101010101011110
110   |  N   |  0
111   |  N   |  0
.
.
.

Index |  V   | Tag
-------------------------------------------
000   |  Y   |  100000000000111111111111111
001   |  N   |  0
010   |  Y   |  100100111001100110101110101
011   |  N   |  0
100   |  Y   |  111111100000111110000011111
101   |  Y   |  111111111101010101010111110
110   |  Y   |  011010101011111010111000011
111   |  N   |  0


The number of memory accesses :  19
The hit ratio :  0.05
The miss ratio :  0.95
The average memory access time : 100.0 cycles
The number of the cache accesses : 1
The total number of accesses : 20


```
