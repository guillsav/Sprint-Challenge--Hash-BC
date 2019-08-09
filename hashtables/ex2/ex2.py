#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"{self.source}, {self.destination}"


def reconstruct_trip(tickets, length):
    # length = length - 1
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Loop through the tickets array to get the first ticket.
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    counter = 0
    route[counter] = hash_table_retrieve(hashtable, "NONE")
    next_source = route[counter]

    while next_source != "NONE":
        destination = hash_table_retrieve(hashtable, route[counter])
        counter += 1
        route[counter] = destination
        next_source = hash_table_retrieve(hashtable, route[counter])
    route[counter + 1] = "NONE"

    return route


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]


reconstruct_trip(tickets, len(tickets))
