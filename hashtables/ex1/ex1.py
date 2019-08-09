#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(limit)
    result = []
    potential_match = None

    """
    YOUR CODE HERE
    """

    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)

    for num in weights:
        potential_match = limit - num
        if hash_table_retrieve(ht, potential_match) is not None:
            result.append(hash_table_retrieve(ht, ht.storage[num].key))
            result.reverse()

    if len(result) > 0:
        return result
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
