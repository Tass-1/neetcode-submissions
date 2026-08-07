class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        res = []
        que = deque([root])
        
        while que:
            node = que.popleft()
            if node is None:
                res.append('null')
            else:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
                
        return " ".join(res)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        vals = data.split(" ")
        root = TreeNode(int(vals[0]))
        que = deque([root])
        i = 1
        
        while que:
            node = que.popleft()
            
            if vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                que.append(node.left)
            i += 1
            
            if vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                que.append(node.right)
            i += 1
            
        return root