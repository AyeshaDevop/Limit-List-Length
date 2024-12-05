MAX_LENGTH = 3 

def shorten(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each element removed.
    """
    while len(lst) > MAX_LENGTH: 
        last_elem = lst.pop()  
        print(last_elem) 

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  
        lst.append(elem)  
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst
def main():
    """
    Main function to execute the program logic.
    """
    lst = get_lst() 
    shorten(lst)  
if __name__ == '__main__':
    main()