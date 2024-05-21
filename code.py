def deleteTailNode(head):
    curr==head
    if curr==None or curr.next==None:
        return None
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head
def deleteHeadNode(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode
def deleteNodeAtSpecificPosition(head,position):
    if position==0:
        return deleteHeadNode(head)
    CurrIndex=0
    CurrentNode=head
    while currentIndex!=position-1:
        currentIndex+=1
        currentNode=currentNode.next
    nodetobedeleted=currentNode.next
    currentNode.next=nodetobedeleted.next
    nodetobedeleted.next=None
    return head 
def enQueue(Q,ele):
    print(ele,"enqueued successfully")
def deQueue(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    print(Q[0], " element is getting deleted")
    Q.pop(0)
     
Q=[]
enQueue(Q,10)
enQueue(Q,20)
enQueue(Q,30)
enQueue(Q,40)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)
 
deQueue(Q)
print(Q)