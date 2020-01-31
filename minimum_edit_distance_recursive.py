
def minimum_edit_distance(i, j, A, B):
    if i == 0:
        return j
    if j == 0:
        return i
    return min(minimum_edit_distance(i - 1, j, A, B) + 1,
               minimum_edit_distance(i, j - 1, A, B) + 1,
               minimum_edit_distance(i - 1, j - 1, A, B) + (A[i - 1] != B[j - 1]))


def unit_tests():
    sequence_one_1 = 'abc'
    sequence_two_1 = 'abc'
    n_1 = sequence_one_1.__len__()
    m_1 = sequence_two_1.__len__()

    print('Minimum Edit Distance of sequence one =', sequence_one_1, ' and sequence two =', sequence_two_1, ' is ', minimum_edit_distance(n_1, m_1, sequence_one_1, sequence_two_1))

    sequence_one_2 = 'abc'
    sequence_two_2 = 'abcd'
    n_2 = sequence_one_2.__len__()
    m_2 = sequence_two_2.__len__()

    print('Minimum Edit Distance of sequence one =', sequence_one_2, ' and sequence two =', sequence_two_2, ' is ', minimum_edit_distance(n_2, m_2, sequence_one_2, sequence_two_2))

    sequence_one_3 = 'abc'
    sequence_two_3 = 'def'
    n_3 = sequence_one_3.__len__()
    m_3 = sequence_two_3.__len__()

    print('Minimum Edit Distance of sequence one =', sequence_one_3, ' and sequence two =', sequence_two_3, ' is ', minimum_edit_distance(n_3, m_3, sequence_one_3, sequence_two_3))


unit_tests()
