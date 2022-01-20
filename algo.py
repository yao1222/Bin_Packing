# n個物品, 不同重量w
# Bin的限重 = c

# Online Algo - Next Fit
# 裝不下就開新的箱子
# is a simple algorithm. It requires only O(n) time and O(1) extra space to process n items.
# Next Fit is 2 approximate, i.e.,
# the number of bins used by this algorithm is bounded by twice of optimal.
# Consider any two adjacent bins. The sum of items in these two bins must be > c;
# otherwise, NextFit would have put all the items of second bin into the first.
# The same holds for all other bins. 
# Thus, at most half the space is wasted, and so Next Fit uses at most 2M bins if M is optimal.
def nextfit(weight, c):
    res = 0
    rem = c
    for _ in range(len(weight)):
        if rem >= weight[_]:
            rem = rem - weight[_]
        else:
            res += 1
            rem = c - weight[_]
    return res
 
# Driver Code
weight = [8, 7, 5, 2, 4, 1, 3]
c = 10
 
print("Number of bins required in Next Fit :", nextfit(weight, c))


# Online Algo - First Fit
# 會先檢查前面的箱子是否剩下空間可用
# The above implementation of First Fit requires O(n2) time,
# but First Fit can be implemented in O(n Log n) time using Self-Balancing Binary Search Trees.
# If M is the optimal number of bins, then First Fit never uses more than 1.7M bins.
# So First-Fit is better than Next Fit in terms of upper bound on number of bins
# Returns number of bins required using first fit
def firstFit(weight, n, c):
     
    # Initialize result (Count of bins)
    res = 0
     
    # Create an array to store remaining space in bins
    # there can be at most n bins
    bin_rem = [0]*n
     
    # Place items one by one
    for i in range(n):
       
        # Find the first bin that can accommodate
        # weight[i]
        j = 0
        while( j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j+=1
             
        # If no bin could accommodate weight[i]
        if (j == res):
            bin_rem[res] = c - weight[i]
            res= res+1
    return res
     
# Driver program
weight = [2, 5, 4, 7, 1, 3, 8]
c = 10
n = len(weight)
print("Number of bins required in First Fit : ",firstFit(weight, n, c))


# Online algorithm - First Fit algorithm.
# 從最小的空間開始裝起
# Best Fit can also be implemented in O(n Log n) time using Self-Balancing Binary Search Trees.
# If M is the optimal number of bins, then Best Fit never uses more than 1.7M bins.
# So Best Fit is same as First Fit and better than Next Fit in terms of upper bound on number of bins.
# Returns number of bins required
# using first fit
def firstFit(weight, n, c):
     
    # Initialize result (Count of bins)
    res = 0;
 
    # Create an array to store
    # remaining space in bins
    # there can be at most n bins
    bin_rem = [0]*n;
 
    # Place items one by one
    for i in range(n):
         
        # Find the first bin that
        # can accommodate
        # weight[i]
        j = 0;
         
        # Initialize minimum space
        # left and index
        # of best bin
        min = c + 1;
        bi = 0;
 
        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):
                bi = j;
                min = bin_rem[j] - weight[i];
             
        # If no bin could accommodate weight[i],
        # create a new bin
        if (min == c + 1):
            bin_rem[res] = c - weight[i];
            res += 1;
        else: # Assign the item to best bin
            bin_rem[bi] -= weight[i];
    return res;
 
# Driver code
if __name__ == '__main__':
    weight = [ 2, 5, 4, 7, 1, 3, 8 ];
    c = 10;
    n = len(weight);
    print("Number of bins required in First Fit : ", firstFit(weight, n, c));


# Offline Algorithms 
# In the offline version, we have all items upfront.
# Unfortunately offline version is also NP Complete,
# but we have a better approximate algorithm for it.
# First Fit Decreasing uses at most (4M + 1)/3 bins if the optimal is M.

# 4. First Fit Decreasing: 
# A trouble with online algorithms is that packing large items is difficult,
# especially if they occur late in the sequence.
# We can circumvent this by *sorting* the input sequence,
# and placing the large items first.
# With sorting, we get First Fit Decreasing and Best Fit Decreasing,
# as offline analogues of online First Fit and Best Fit. 