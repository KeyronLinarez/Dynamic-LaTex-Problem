import sys
import math

def length_helper(words, i, j):
    """
    length_helper() calculates the total of the words

    Input:
    (list) words - the array of words
    (int) i - starting index
    (int) j - ending index
    Output:
    (int) total_length -  the length of characters between index i and j
    """
    # Calculate the sum of the lengths of words from index i to j-1, adding 1 for each space
    total_length = sum(len(words[k]) + 1 for k in range(i, j))
    # Add the length of the last word w_j (no space after the last word)
    total_length += len(words[j])
    return total_length 


def j_helper(words, end, L):
    """
    j_helper() - given a word list and an index, you want to find the place j, where the word can cover up to that point

    Input: 
    (list) words - the array of words
    (int) end - the ending index
    (int) L - the max length any line can be
    """
    start_index = end 
    word_length = length_helper(words, start_index, end)
    # You keep going until you can no longer cover that point
    while word_length <= L:
        start_index -= 1
        word_length = length_helper(words, start_index, end)
    return start_index 


def format_dp(arr, L):
    """
    format_dp runs the dp algorithm and prints the final penalty and string formatted

    Input: 
    (list) arr - array of strings
    (int) L - the max length any letter can be
    """
    # arrays to cover the penalties and breaks
    penalty = []
    breaks = []

    for i in range(0, len(arr)):
        # This is the case where we can write everything into a single line
        if (length_helper(arr,0, i) <= L):
            breaks.append(0) #B[i] = 0
            cur_penalty = (L - length_helper(arr, 0, i)) ** 3
            penalty.append(cur_penalty)
        # in this scenario, it searches for the minimum penalty that can be found at each point
        else:
            cur_min = math.inf
            cur_break= -1
            start_j = j_helper(arr, i, L)

            # in charge of looking at all the following scenarios in how you can format current string
            for j in range(start_j, i):
                cur_penalty = (penalty[j]) + ((L-length_helper(arr, j+1, i)) ** 3)
                if(cur_penalty < cur_min):
                    cur_min = cur_penalty
                    cur_break = j + 1

            breaks.append(cur_break)
            penalty.append(cur_min)

    # obtaining the final penalty and the returned string
    final_penalty = penalty[-1]
    start, end = breaks[-1], len(arr)
    res = ''
    while start >= 0: 
        line = " ".join(arr[start:end])
        res = line + "\n" + res
        end = start
        if start <= 0: 
            break
        start = breaks[start-1]
    
    # Removes the last new line of a string
    if res.endswith('\n'):
        res= res[:-1]

    # print final penalty and res
    print(final_penalty)
    print(res)
      

def main(): 
    """
    main() runs the entire program
    """
    # Get input and output file names from command line arguments
    L = int(sys.argv[1])
    infile = sys.argv[2]
    # opening the file and adding the contents to the array

    with open(infile, 'r') as file: 
        contents = file.read() # read file into an array of strings
    
    # Splitting data into an array and then calling the dp function into it
    text_arr = contents.split()
    format_dp(text_arr, L)


   
if __name__ == "__main__":
    main()
