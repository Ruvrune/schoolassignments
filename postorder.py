from Stack import Stack
#Bruker binærtrekode fra eksempel
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def getRoot(self):
        return self.root

    def postOrder(self):
        return

 # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return treeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size

    '''Så notatene fra traversing av binærtre før jeg selv prøvde å løse fremgangsmåten
     klarer ikke å u-se metoden som er brukt der, så denne er lik den i notatene
     '''
    def postOrder(self):
        if self.root == None:
            return
        stack = Stack()
        visited = []
        current = self.root
        stack.push(current)
        while (not stack.isEmpty()):
            current = stack.peek()
            if current.left != None and not current.left in visited:
                stack.push(current.left)
            elif current.right != None and not current.right in visited:
                stack.push(current.right)
            else:
                stack.pop()
                visited.append(current)
                print(current.element, end=" ") # visit

class treeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None

def main():

    testTre = BST()
    testTre2 = BST()

    testTre.insert(2)
    testTre.insert(10)
    testTre.insert(3)
    testTre.insert(14)
    testTre.insert(12)

    testTre2.insert(60)
    testTre2.insert(55)
    testTre2.insert(100)
    testTre2.insert(45)
    testTre2.insert(57)
    testTre2.insert(67)
    testTre2.insert(107)
    testTre2.insert(59)
    testTre2.insert(101)
    print("Traversert med postorder: ")
    testTre.postOrder()
    print("\nTraversert samme som eksempelet i Pearson: ")
    testTre2.postOrder()

main()