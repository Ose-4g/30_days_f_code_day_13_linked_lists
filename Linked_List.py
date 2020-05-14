class Node:
    '''
    Class for each node of a lnked list
    '''  
    def __init__(self,val):
        assert type(val)==int
        self.value=val
        self.next=None

def append(head,val):
    '''
    adds an element to the linked list
    '''
    assert type(head)==Node and type(val)==int
    while head.next:
        head=head.next
    head.next=Node(val)
    

def pop(head):
    '''
    removes the last element from the list
    '''
    assert type(head)==Node
    if head.next==None:
       head=head.next
    else:
        h=head
        while h.next.next:
            h=h.next
        h.next=None


