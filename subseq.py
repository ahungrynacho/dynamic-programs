from copy import deepcopy

def longest_subseq(str1, str2):
    table = [[0 for y in range(0, len(str1)+1)] for x in range(0, len(str2)+1)]
    
    for i in range(0, len(str2)):
        for j in range(0, len(str1)):
            if str2[i] != str1[j]:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
            else:
                table[i+1][j+1] = table[i][j] + 1
                
    for line in table:
        print(line)
    
    subseq = ""
    i = len(str2)
    j = len(str1)
    
    while i != 0 and j != 0:
        if table[i-1][j] == table[i][j-1]:
            subseq += str2[i-1]
            i -= 1
            j -= 1
        elif table[i][j-1] < table[i-1][j]:
            i -= 1
        elif table[i-1][j] < table[i][j-1]:
            j -= 1

    return sorted(subseq)
if __name__ == "__main__":
    print(longest_subseq("abcdaf", "acbcf"))