class Node:
    # Blueprint for a node of a linked list
    def __init__(self, value):
        self.data = value;
        self.next = None

class LinkedList:
    # constructor for creating a linked list 
    # and storing it in self.head
    def __init__(self):
        pass

    def traversal(self):
        itr = self.head
        while itr is not None:
            print(itr.data)
            itr = itr.next
    # 'newNode' - pointer to the node to be inserted
    # 'prevNode' - pointer to the node after which insertion occurs
    def insertion(self, prevNode, newNode):
        newNode.next = prevNode.next
        prevNode.next = newNode

    # 'targetNode' - pointer to the node to be deleted
    # 'prevNode' - pointer to the node after which deletion occurs
    def deletion(self, prevNode, targetNode):
        prevNode.next = targetNode.next
        targetNode.next = None

    def search(self, key):
        itr = self.head
        while itr is not None:
            if itr.data == key: return True
            itr = itr.next
        return False # key not found!