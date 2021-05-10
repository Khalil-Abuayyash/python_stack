class SList:

    def __init__(self):
        self.head = None

    def print_values(self):

        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self
    
    def add_to_front(self, value):

        new_node = SLNode(value)
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self,value):

        if self.head == None:
            self.add_to_front(value)
            return self
            
        new_node = SLNode(value)
        runner = self.head

        while(runner.next != None):
            runner = runner.next
        
        runner.next =  new_node
        return self
    
    def remove_from_front(self):
        node_tobe_removed = self.head
        self.head = node_tobe_removed.next
        # node_tobe_removed.next = None
        returned_value = node_tobe_removed.value
        # del node_tobe_removed
        return returned_value
    
    def remove_from_back(self):
        runner = self.head
        while(runner.next.next != None):
            runner = runner.next
        returned_value = runner.next.value
        runner.next = None
        return returned_value
    
    def value_at(self, value):
        runner = self.head
        counter = 0
        while(runner != None):
            if runner.value == value:
                if runner.next != None:
                    return counter
                else:
                    return -1 # last element
            counter += 1
            runner = runner.next  
        return -2 # no value

    def remove_val(self, value):
        at = self.value_at(value)
        if at > 0:
            runner = self.head
            i = 0
            while(i < at-1):
                runner = runner.next
                i += 1
            runner.next = runner.next.next

        elif at == 0:
            self.remove_from_back()

        elif at == -1:
            self.remove_from_back()
        
        elif at == -2:
            return "The list hasn't this value"
    
    def last_index(self):
        i = 0
        runner = self.head
        while(runner.next != None):
            runner = runner.next
            i += 1
        return i
        
    
    def insert_at(self, value, n):
        last_idx = self.last_index()

        if n == last_idx:
            self.add_to_back(value)
            return self

        elif n > last_idx:
            print("Not Allowed")
            return self
        
        elif n == 0:
            self.add_to_front(value)
            return self
        
        runner = self.head
        i = 0

        while(i < n-1 ):
            runner = runner.next
            i += 1    
        new_node = SLNode(value)
        new_node.next = runner.next
        runner.next = new_node        
        return self

class SLNode:

    def __init__(self, value):
        self.value = value
        self.next = None
    


    