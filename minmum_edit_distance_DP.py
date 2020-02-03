import numpy as np


def minimum_edit_distance_DP(n, m, A, B):
    cache = np.zeros((n + 1, m + 1))

    for i in range(n + 1):
        for j in range(m + 1):

            if i == 0:
                cache[i][j] = j     # If A is empty, Insert all characters of B. MED is the length of B and store that in the cache

            elif j == 0:
                cache[i][j] = i     # If B is empty, Insert all characters of A. MED is the length of A and store that in the cache

            elif A[i - 1] == B[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]       # If the last characters are the same, edit is not needed, continue on and store the previous value in the cache

            else:
                cache[i][j] = 1 + min(cache[i][j - 1],  # If the last characters are different, edit is needed, test inserting, removing, and replacing. Return the minimum and store it in the cache
                                      cache[i - 1][j],
                                      cache[i - 1][j - 1])

    return int(cache[n][m])


def unit_tests():
    sequence_one_1 = 'abc'
    sequence_two_1 = 'abc'
    n_1 = sequence_one_1.__len__()
    m_1 = sequence_two_1.__len__()

    print('Minimum Edit Distance of sequence one =', sequence_one_1, ' and sequence two =', sequence_two_1, ' is ', minimum_edit_distance_DP(n_1, m_1, sequence_one_1, sequence_two_1))

    sequence_one_2 = 'abc'
    sequence_two_2 = 'abcd'
    n_2 = sequence_one_2.__len__()
    m_2 = sequence_two_2.__len__()

    print('Minimum Edit Distance of sequence one =', sequence_one_2, ' and sequence two =', sequence_two_2, ' is ', minimum_edit_distance_DP(n_2, m_2, sequence_one_2, sequence_two_2))

    sequence_one_3 = 'abc'
    sequence_two_3 = 'def'
    n_3 = sequence_one_3.__len__()
    m_3 = sequence_two_3.__len__()

    print('Minimum Edit Distance of sequence one =', sequence_one_3, ' and sequence two =', sequence_two_3, ' is ', minimum_edit_distance_DP(n_3, m_3, sequence_one_3, sequence_two_3))


def read_list_of_common_misspellings():
    common_misspellings_arr = []
    incorrect_spellings = []
    correct_spellings = []
    common_misspellings_dict = {}

    with open('list_of_common_misspellings.txt') as CM:
        common_misspellings_arr = CM.read().splitlines()

    for i in range(common_misspellings_arr.__len__()):
        incorrect_spellings.append(common_misspellings_arr[i].split('->')[0])
        correct_spellings.append(common_misspellings_arr[i].split('->')[1])

    for i in range(correct_spellings.__len__()):
        correct_spellings[i] = correct_spellings[i].split(', ')

    for i in range(incorrect_spellings.__len__()):
        common_misspellings_dict[incorrect_spellings[i]] = correct_spellings[i]

    return common_misspellings_dict


def test_list_of_common_misspellings():
    common_misspellings_dict = read_list_of_common_misspellings()

    print(common_misspellings_dict)

    for incorrect_word in common_misspellings_dict:
        for correct_word in common_misspellings_dict[incorrect_word]:
            n = incorrect_word.__len__()
            m = correct_word.__len__()
            A = incorrect_word
            B = correct_word
            print('Key: ', incorrect_word, '    Value: ', correct_word, '      MED: ', minimum_edit_distance_DP(n, m, A, B))



# unit_tests()
test_list_of_common_misspellings()
