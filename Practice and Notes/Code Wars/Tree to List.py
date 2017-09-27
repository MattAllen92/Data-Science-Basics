class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    values = [tree_root.data]
    targets = tree_root.child_nodes
    
    while targets:
        target = targets.pop(0)
        values.append(target)
        if target.child_nodes:
            targets += target.child_nodes
    
    return values