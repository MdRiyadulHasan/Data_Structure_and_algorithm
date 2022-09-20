queue=[]
def enqueue():
    element = input('Enter element : ')
    queue.append(element)
    print(f'{element} is entered ')
def dequeue():
    if not queue:
        print("Empty queue")
    else:
        e=queue.pop(0)
        print(f'{e} is removed')
def display():
    print(queue)

if __name__ == '__main__':
    while True:
        print('select the operation : 1. Enqueue 2. Deque 3.Display 4. Quit ')
        choice=int(input())
        if choice==1:
            enqueue()
        elif choice==2:
            dequeue()
        elif choice==3:
            display()
        elif choice==4:
            break
        else:
            print('Enter right choice')
        
