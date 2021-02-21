# Implement FreqStack, a class which simulates the operation of a stack-like data structure.

# FreqStack has two functions:

# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


# Example 1:

# Input:
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].

# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].

# pop() -> returns 5.
# The stack becomes [5,7,4].

# pop() -> returns 4.
# The stack becomes [5,7].
#
#brute force

class FreqStack:

#     def __init__(self):
#         self.stack = []
#         self.most_freq = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)


#     def pop(self) -> int:
#         [num, pos] = self.find_most_freq()

#         del self.stack[pos]

#         return num

#     def find_most_freq(self) -> list:
#         freqs = {}

#         for i in range (len(self.stack)):
#             number = self.stack[i]

#             if freqs.get(number):
#                 val = freqs.get(number)[0] + 1
#             else:
#                 val = 1

#             freqs[number] = [val, i]

#         max_freq_number = None

#         for number, freq in freqs.items():
#             if not max_freq_number or freq > freqs.get(max_freq_number[0]):
#                 max_freq_number = [number, freqs.get(number)[1]]
#             elif not max_freq_number or freq == freqs.get(max_freq_number[0]):
#                 curr_number_pos = freqs.get(number)[1]
#                 max_freq_number_pos = freqs.get(max_freq_number[1])

#                 if curr_number_pos > max_freq_number_pos:
#                     max_freq_number = [number, curr_number_pos]

#         return max_freq_number

#more optimal appraoch

    def __init__(self):
        #keep track of the frequency of each element
        self.freq = collections.Counter()

        #keep track of all of the elements that occur at a certain frequency
        self.group = collections.defaultdict(list)

        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f

        if f > self.maxfreq:
            self.maxfreq = f

        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1

        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
