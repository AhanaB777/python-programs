"""
Count Consecutive Increase Blocks”
● Problem statement:Input a sequence of 8 integers, count how many blocks of
consecutive increasing numbers exist. A block is defined as one or more numbers such
that each number after the first in the block is strictly greater than its predecessor. For
example [2, 3, 5, 1, 2, 3, 3, 4] has: first block [2,3,5], then second block [1,2,3], skip the 3 to
3 since not strictly greater, then third block [3,4]. So the answer would be 3. Also print the
length of the longest block.
● Input: A list of integers (length ≥ 1).
● Output: Two integers: number of increasing-blocks, and length of the longest block.
● Processing logic:
■ Initialize block_count = 0, current_length = 1, longest = 1.
■ Loop from second element to end: compare current with previous.
○ If current > previous: increment current_length.
○ Else: end of block → increment block_count; update longest =
max(longest, current_length); reset current_length = 1.
■ After loop, handle the last block (increment block_count; update longest).
■ Print block_count and longest.

"""
n=int(input("enter number of terms : "))
count=1
no_block=1
max_block_length=1
block_length=1

while count<=n :
    num=int(input("enter a number: "))
    if count==1 :
        value=num
    else :
        if num>value :
            block_length +=1
            value=num
        else :
            no_block += 1
            if block_length > max_block_length :
                max_block_length = block_length
            block_length=1
    count+=1
print(f"Max block length is {max_block_length} ")