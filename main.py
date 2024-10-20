import sys


def length_helper(words, i, j):
    """
    this calculates the total of the words
    """
    # Calculate the sum of the lengths of words from index i to j-1, adding 1 for each space
    # if i != j:
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
    return start_index + 1


# def dp(arr, L):
#     # penalty = [0 for _ in range(len(arr) + 1)]
#     # breaks = [0 for _ in range(len(arr) + 1)]
#     # penalty[0], breaks[0] = 0, 0
#     penalty = []
#     breaks = []

#     penalty.append(0)
#     breaks.append(0)

#     for i in range(1, len(arr) + 1): # might have to swap the 0 for 1
#         if (length_helper(arr,1, i) <= L):
            


def main(): 

    words = ["Dogs", "are", "cuter", "than", "moles"]
    print(j_helper(words, 3, 12))
    # print(length_helper(words, 0, 4))
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
