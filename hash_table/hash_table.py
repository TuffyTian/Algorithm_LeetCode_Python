"""
 * @Author: TuffyTian 
 * @Date: 2020-06-07 20:45:14 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-06-07 20:45:14 

 hash table
"""


class Employee():
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.next = None


class LinkedList():
    head: Employee = None

    def __init__(self, index: int):
        self.index = index

    def add(self, id: int, name: str):
        new_employee = Employee(id=id, name=name)
        if self.head is None:
            self.head = new_employee
            return
        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.next = new_employee

    def find(self, id: int):
        if not self.head:
            print("not found.")
            return
        pointer = self.head
        while pointer:
            if pointer.id == id:
                print("found employee:" + "id: " + str(pointer.id) + "name: " + pointer.name)
                return
        print("Not found.")

    def print_list(self):
        print(str(self.index + 1) + " linked list -> ", end="")
        if self.head is None:
            print("No Data.")
            return
        pointer = self.head
        while pointer:
            print("id: " + str(pointer.id) + " name: " + pointer.name, end="")
            pointer = pointer.next
        print()


class HashTable():
    def __init__(self, count: int):
        self.count = count
        self.lists = [LinkedList(index=i) for i in range(count)]

    def get_hash(self, id: int):
        index = id % self.count
        return index

    def add_employee(self, id: int, name: str):
        index = self.get_hash(id)
        linked_list = self.lists[index]
        linked_list.add(id, name)

    def find_employee(self, id: int):
        index = self.get_hash(id)
        linked_list = self.lists[index]
        linked_list.find(id=id)

    def print_hash_table(self):
        for i in range(self.count):
            linked_list = self.lists[i]
            linked_list.print_list()


if __name__ == "__main__":
    hash_table = HashTable(5)
    hash_table.add_employee(1, "ttf")
    hash_table.add_employee(3, "tuffy")
    hash_table.add_employee(6, "shawn")
    hash_table.add_employee(10, "bryan")
    hash_table.print_hash_table()

    hash_table.find_employee(2)
