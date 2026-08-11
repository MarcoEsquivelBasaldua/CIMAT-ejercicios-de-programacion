class TreeNode:
    def __init__(self, freeSeats):
        self.freeSeats = freeSeats
        self.isLeaf    = True
        self.leftNode  = None
        self.rightNode = None

    def getMinMax(self):
        seatRemoved = self.freeSeats - 1

        _min = seatRemoved // 2
        _max = seatRemoved - _min

        return _min, _max

def vitsitTree(node, k):
    if node:
        if node.isLeaf:
            node.isLeaf = False
            _min, _max = root.getMinMax()
            
            # Create new nodes
            node.leftNode  = TreeNode(_min)
            node.rightNode = TreeNode(_max)

            print("For K = ", k, ", the min and max are: ", _min, ", ", _max)
        else:
            vitsitTree(node.leftNode, k)
            vitsitTree(node.rightNode, k)


N = 8
K = 2

for k in range(1, K+1):
    if k == 1:
        root        = TreeNode(8)
        root.isLeaf = False

        _min, _max = root.getMinMax()

        # Create new nodes
        root.leftNode = TreeNode(_min)
        root.rightNode = TreeNode(_max)

        print("For K = ", k, ", the min and max are: ", _min, ", ", _max)
    else:
        # Visit tree nodes
        vitsitTree(root, k)




A binary tree may not be needed

    
