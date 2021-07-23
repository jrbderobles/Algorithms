from collections import deque

class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = left

def make_tree(elements):
    tree = Node(elements[0])
    for element in elements[1:]:
        insert(tree, element)
    return tree

def insert(temp, data):
    queue = []
    queue.append(temp)
    while len(queue):
        temp = queue[0]
        queue.pop(0)

        if temp.left: queue.append(temp.left)
        else:
            if data: temp.left = Node(data)
            else: temp.left = Node(0)
            break

        if temp.right: queue.append(temp.right)
        else:
            if data: temp.right = Node(data)
            else: temp.right = Node(0)
            break

def height(root):
    if root:
        left_height = height(root.left)
        right_height = height(root.right)

        if left_height > right_height: return left_height + 1
        else: return right_height + 1

    else: return 0

def print_given_level(root, level):
    if root is None: return
    if level == 1: print(root.data, end = ' ')
    elif level > 1 :
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)

# For printing out the tree (1st way)
def level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i)

# For printing out the tree (2nd way)
def level_order_traversal(root):
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        print(current.data, end = ' ')
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

# Recursion
# Since we have to travel to each node once, the time complexity is O(n). We cannot do better than that, since at the very least we have to visit each node to invert it.
# Because of recursion, O(h) function calls will be placed on the stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).
# If we have a horribly unbalanced tree, i.e. a chain of n nodes, our worst case auxiliary space is O(n) as well.
# As with any recursive problem, stack overflow can happen for a large tree.
def invert_tree_recursion(root):
    if root:
        root.left, root.right = invert_tree_recursion(root.right), invert_tree_recursion(root.left)
        return root

# Iteration
# Since each node in the tree is visited or added to the queue only once, the time complexity is O(n), where n is the number of nodes in the tree.
# Space complexity is O(n), since in the worst case, the queue will contain all nodes in one level of the binary tree.
# For a full binary tree, the leaf level has ⌈n/2⌉ = O(n) leaves.
# We no longer have to worry about the call stack, and so these iterative cases are more robust.

# 1. DFS using stacks (DFS involves searching a node and all its children before proceeding to its siblings)
def invert_tree_dfs(root):
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root

# 2. BFS using queues (BFS involves searching a node and its siblings before going on)
def invert_tree_bfs(root):
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

'''''''''''''''''''''''''''
            4
    2               7
1       3       6       9
'''''''''''''''''''''''''''
tree = make_tree([4, 2, 7, 1, 3, 6, 9])

level_order_traversal(tree)
print('\n')


'''''''''''''''''''''''''''
            4
    7               2
9       6       3       1
'''''''''''''''''''''''''''
level_order_traversal(invert_tree_recursion(tree)) # 4 7 2 9 6 3 1
print('\n')

tree = make_tree([4, 2, 7, 1, 3, 6, 9])
level_order_traversal(invert_tree_dfs(tree)) # DFS stack 4 7 2 9 6 3 1
print('\n')

tree = make_tree([4, 2, 7, 1, 3, 6, 9])
level_order_traversal(invert_tree_bfs(tree)) # BFS queue 4 7 2 9 6 3 1
