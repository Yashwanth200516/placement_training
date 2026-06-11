class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  
        current.next = prev       
        prev = current          
        current = next_node      
    return prev  
def print_list(head):
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements))
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print("Before:")
print_list(head)
reversed_head = reverse_list(head)
print("After:")
print_list(reversed_head)