class Node:
    def __init__(self, item=None, left=None, right=None):
        """
        Initialize a node in a binary search tree.

        Parameters
        ----------
        item : Any
            The data to be stored in the node.
        left : Node or None
            The left child node.
        right : Node or None
            The right child node.
        """
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        """
        Initialize the binary search tree.
        """
        self.root = None

    def insert(self, data):
        """
        Insert a new node with the given data into the BST.

        Parameters
        ----------
        data : Any
            The value to insert into the tree.
        """
        self.root = self._rinsert(self.root, data)

    def _rinsert(self, root, data):
        """
        Recursively insert a node into the BST.

        Parameters
        ----------
        root : Node or None
            The current node in the recursion.
        data : Any
            The value to insert into the tree.

        Returns
        -------
        Node
            The updated root node.
        """
        if root is None:
            return Node(data)  # Create a new node if the current root is empty
        if data < root.item:
            root.left = self._rinsert(root.left, data)  # Insert in left subtree
        elif data > root.item:
            root.right = self._rinsert(root.right, data)  # Insert in right subtree
        return root

    def search(self, data):
        """
        Search for a node with the given data.

        Parameters
        ----------
        data : Any
            The value to search for in the tree.

        Returns
        -------
        Node or None
            The node if found, or None if not found.
        """
        return self._rsearch(self.root, data)

    def _rsearch(self, root, data):
        """
        Recursively search for a node in the BST.

        Parameters
        ----------
        root : Node or None
            The current node in the recursion.
        data : Any
            The value to search for.

        Returns
        -------
        Node or None
            The node if found, or None if not found.
        """
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self._rsearch(root.left, data)
        return self._rsearch(root.right, data)

    def inorder(self):
        """
        Perform an inorder traversal of the BST.

        Returns
        -------
        List[Any]
            The inorder traversal result as a list of node values.
        """
        result = []
        self._rinorder(self.root, result)
        return result

    def _rinorder(self, root, result):
        """
        Recursively perform inorder traversal.

        Parameters
        ----------
        root : Node or None
            The current node in the recursion.
        result : List[Any]
            The list to append node values to.
        """
        if root:
            self._rinorder(root.left, result)  # Traverse the left subtree
            result.append(root.item)  # Append the root value
            self._rinorder(root.right, result)  # Traverse the right subtree

    def preorder(self):
        """
        Perform a preorder traversal of the BST.

        Returns
        -------
        List[Any]
            The preorder traversal result as a list of node values.
        """
        result = []
        self._rpreorder(self.root, result)
        return result

    def _rpreorder(self, root, result):
        """
        Recursively perform preorder traversal.

        Parameters
        ----------
        root : Node or None
            The current node in the recursion.
        result : List[Any]
            The list to append node values to.
        """
        if root:
            result.append(root.item)  # Append the root value
            self._rpreorder(root.left, result)  # Traverse the left subtree
            self._rpreorder(root.right, result)  # Traverse the right subtree

    def postorder(self):
        """
        Perform a postorder traversal of the BST.

        Returns
        -------
        List[Any]
            The postorder traversal result as a list of node values.
        """
        result = []
        self._rpostorder(self.root, result)
        return result

    def _rpostorder(self, root, result):
        """
        Recursively perform postorder traversal.

        Parameters
        ----------
        root : Node or None
            The current node in the recursion.
        result : List[Any]
            The list to append node values to.
        """
        if root:
            self._rpostorder(root.left, result)  # Traverse the left subtree
            self._rpostorder(root.right, result)  # Traverse the right subtree
            result.append(root.item)  # Append the root value

    def min_value(self):
        """
        Find the minimum value in the BST.

        Returns
        -------
        Any
            The minimum value in the tree.
        """
        current = self.root
        while current.left is not None:
            current = current.left  # Traverse to the leftmost node
        return current.item

    def max_value(self):
        """
        Find the maximum value in the BST.

        Returns
        -------
        Any
            The maximum value in the tree.
        """
        current = self.root
        while current.right is not None:
            current = current.right  # Traverse to the rightmost node
        return current.item

    def delete(self, data):
        """
        Delete a node with the specified data from the BST.

        Parameters
        ----------
        data : Any
            The value to delete from the tree.
        """
        self.root = self._rdelete(self.root, data)

    def _rdelete(self, root, data):
        """
        Recursively delete a node from the BST.

        Parameters
        ----------
        root : Node or None
            The current node in the recursion.
        data : Any
            The value to delete from the tree.

        Returns
        -------
        Node or None
            The updated root node.
        """
        if root is None:
            return root  # Return None if the node to delete is not found
        if data < root.item:
            root.left = self._rdelete(root.left, data)  # Search in the left subtree
        elif data > root.item:
            root.right = self._rdelete(root.right, data)  # Search in the right subtree
        else:
            # Node to delete found
            if root.left is None:
                return root.right  # Return right subtree if no left child
            elif root.right is None:
                return root.left  # Return left subtree if no right child
            root.item = self.min_value(root.right)  # Replace with inorder successor
            root.right = self._rdelete(root.right, root.item)  # Delete successor
        return root

    def size(self):
        """
        Calculate the size (number of nodes) of the BST.

        Returns
        -------
        int
            The total number of nodes in the tree.
        """
        return len(self.inorder())  # Use inorder traversal to count nodes
