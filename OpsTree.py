class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    p = head
    q = None
    r = None
    while p is not None:
        r = q;
        q = p;
        p = p.next;
        q.next = r
    return q

def llToNum(head):
    num=0
    while head is not None:
        num = num*10 + head.data
        head = head.next
    return num

def addition(head1, head2):
    num1 = llToNum(head1)
    num2 = llToNum(head2)
    res = num1 + num2
    newHead = Node(0)
    temp = newHead
    while res>0:
        newNode = Node(res%10)
        res = res//10
        temp.next = newNode
        temp=temp.next
    return reverse(newHead.next)

def addition2(head1, head2):
    tempHead1 = head1
    tempHead2 = head2
    tempHead1 = reverse(tempHead1)
    tempHead2 = reverse(tempHead2)
    newHead = Node(0)
    temp = newHead
    carry = 0
    while (tempHead1 is not None) and (tempHead2 is not None):
        val = tempHead1.data + tempHead2.data + carry
        carry = val//10
        val = val%10
        newNode = Node(val)
        temp.next = newNode
        temp=temp.next
        tempHead1=tempHead1.next
        tempHead2=tempHead2.next
    
    while tempHead1 is not None:
        val = tempHead1.data + carry
        carry = val//10
        val = val%10
        newNode = Node(val)
        temp.next = newNode
        temp=temp.next
        tempHead1=tempHead1.next
    
    while tempHead2 is not None:
        val = tempHead2.data + carry
        carry = val//10
        val = val%10
        newNode = Node(val)
        temp.next = newNode
        temp=temp.next
        tempHead2=tempHead2.next
    
    while carry>0:
        val = carry
        carry = val//10
        val = val%10
        newNode = Node(val)
        temp.next = newNode
        temp=temp.next
    
    return reverse(newHead.next)

def subtraction(head1, head2):
    num1 = llToNum(head1)
    num2 = llToNum(head2)
    if(num1>num2):
        res = num1-num2
    else:
        res = num2-num1
    newHead = Node(0)
    if(res == 0):
        return newHead
    temp = newHead
    while res>0:
        newNode = Node(res%10)
        res = res//10
        temp.next = newNode
        temp=temp.next
    return reverse(newHead.next)
    
    
def multiplication(head1, head2):
    num1 = llToNum(head1)
    num2 = llToNum(head2)
    res = num1 * num2
    newHead = Node(0)
    temp = newHead
    while res>0:
        newNode = Node(res%10)
        res = res//10
        temp.next = newNode
        temp=temp.next
    return reverse(newHead.next)

def numToLL(num):
    newHead = Node(0)
    temp = newHead
    while num>0:
        newNode = Node(num%10)
        num = num//10
        temp.next = newNode
        temp=temp.next
    return reverse(newHead.next)

def printLL(head):
    while head is not None:
        if head.next == None:
            print(head.data)
        else:
            print(head.data, end = "->")
        head=head.next

n1 = int(input("Enter first Number: "))
n2 = int(input("Enter second Number: "))

head1 = numToLL(n1)
head2 = numToLL(n2)

res1 = addition(head1, head2)
res2 = subtraction(head2, head1)
res3 = multiplication(head1, head2)

printLL(res1)
printLL(res2)
printLL(res3)