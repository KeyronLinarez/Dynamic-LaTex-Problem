import sys
import math

def length_helper(words, i, j):
    """
    this calculates the total of the words


    """
    # Calculate the sum of the lengths of words from index i to j-1, adding 1 for each space
    total_length = sum(len(words[k]) + 1 for k in range(i, j))
    # Add the length of the last word w_j (no space after the last word)
    total_length += len(words[j])
    return total_length 

# calculate
def j_helper(words, end, L):
    """
    given a word list and an index, you want to find the place j, where the word can cover up to that point
    """
    start_index = end - 1
    word_length = length_helper(words, start_index, end)
    while word_length < L:
        start_index -= 1
        word_length = length_helper(words, start_index, end)
    # Because you can keep throwing it back until the word_length is larger
    return start_index 


def dp(arr, L):
    # penalty = [0 for _ in range(len(arr) + 1)]
    # breaks = [0 for _ in range(len(arr) + 1)]
    # penalty[0], breaks[0] = 0, 0
    penalty = []
    # our breaks will be 0-indexed
    breaks = []
    # penalty.append(0)
    # breaks.append(0)

    for i in range(0, len(arr)): # might have to swap the 0 for 1
        if (length_helper(arr,0, i) <= L):
            breaks.append(0) #B[i] = 0
            cur_penalty = (L - length_helper(arr, 0, i)) ** 3
            penalty.append(cur_penalty) # P[i] = (L - length(a, 1, i))^3
        else:
            cur_min = math.inf
            cur_break= -1
            start_j = j_helper(arr, i, L)

            for j in range(start_j, i):
                print(penalty[j])
                print(j)
                cur_penalty = penalty[j] + ((L-length_helper(arr, j+1, i)) ** 3)
                if(cur_penalty < cur_min):
                    cur_min = cur_penalty
                    cur_break = j

            breaks.append(cur_break)
            penalty.append(cur_min)

    print(penalty)
    print(breaks)

def main(): 

    words = ["Dogs", "are", "cuter", "than", "moles"]
    print(dp(words, 12))
    # print(j_helper(words, 3, 12))
    # print(length_helper(words, 0, 0))
    # # Get input and output file names from command line arguments
    # infile = sys.argv[1]
    # outfile = sys.argv[2]
    # stock_arr = []
    # # opening the file and adding the contents to the array

    # with open(infile, 'r') as file: 
    #     contents = file.readlines() # read file into an array of strings
    #     # get out of a list of strings


   
if __name__ == "__main__":
    main()
