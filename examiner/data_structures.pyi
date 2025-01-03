from typing import Self, List, Any, Optional
from collections import deque

class ListNode:
    def __init__(self, val: Any = 0, next: Optional[Self] = None) -> None:
        """
        Initialize a new ListNode.

        Args:
            val (Any): Value of the node.
            next (Optional[ListNode]): Pointer to the next node. Default is None.

        初始化一个新的链表节点。

        参数：
            val (Any): 节点的值。
            next (Optional[ListNode]): 指向下一个节点的指针，默认为 None。
        """
        self.val: Any
        self.next: Optional[Self]

    @classmethod
    def from_list(cls, values: List[Any]) -> Optional[Self]:
        """
        Create a linked list from a list of values.

        Args:
            values (List[Any]): List of values to create the linked list.

        Returns:
            Optional[ListNode]: Head of the linked list.

        从一个值列表创建链表。

        参数：
            values (List[Any]): 用于创建链表的值列表。

        返回：
            Optional[ListNode]: 链表的头节点。
        """
        ...

    def to_list(self) -> List[Any]:
        """
        Convert the linked list to a list of values.

        Returns:
            List[Any]: List of values in the linked list.

        将链表转换为值列表。

        返回：
            List[Any]: 链表中的值列表。
        """
        ...

    def __eq__(self, other: Optional[Self]) -> bool:
        """
        Compare two linked lists for equality.

        Args:
            other (Optional[ListNode]): The other linked list to compare.

        Returns:
            bool: True if the linked lists are equal, False otherwise.

        比较两个链表是否相等。

        参数：
            other (Optional[ListNode]): 要比较的另一个链表。

        返回：
            bool: 如果链表相等返回 True，否则返回 False。
        """
        ...

    def __str__(self) -> str:
        """
        Return a string representation of the linked list.

        Returns:
            str: String representation of the linked list.

        返回链表的字符串表示形式。

        返回：
            str: 链表的字符串表示形式。
        """
        ...

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the linked list.

        Returns:
            str: Detailed string representation of the linked list.

        返回链表的详细字符串表示形式。

        返回：
            str: 链表的详细字符串表示形式。
        """
        ...


class TreeNode:
    def __init__(self, val: Any = 0, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        """
        Initialize a new TreeNode.

        Args:
            val (Any): Value of the node.
            left (Optional[TreeNode]): Left child node. Default is None.
            right (Optional[TreeNode]): Right child node. Default is None.

        初始化一个新的二叉树节点。

        参数：
            val (Any): 节点的值。
            left (Optional[TreeNode]): 左子节点，默认为 None。
            right (Optional[TreeNode]): 右子节点，默认为 None。
        """
        self.val: Any
        self.left: Optional[Self]
        self.right: Optional[Self]

    @classmethod
    def from_list(cls, values: List[Any]) -> Optional[Self]:
        """
        Create a binary tree from a level-order list of values.

        Args:
            values (List[Any]): Level-order list of values (use None for empty nodes).

        Returns:
            Optional[TreeNode]: Root of the binary tree.

        从按层序排列的值列表创建二叉树。

        参数：
            values (List[Any]): 按层序排列的值列表（用 None 表示空节点）。

        返回：
            Optional[TreeNode]: 二叉树的根节点。
        """
        ...

    def to_list(self) -> List[Any]:
        """
        Convert the binary tree to a level-order list of values.

        Returns:
            List[Any]: Level-order list of values (None for empty nodes).

        将二叉树转换为按层序排列的值列表。

        返回：
            List[Any]: 按层序排列的值列表（空节点用 None 表示）。
        """
        ...

    def __eq__(self, other: Optional[Self]) -> bool:
        """
        Compare two binary trees for equality.

        Args:
            other (Optional[TreeNode]): The other tree to compare.

        Returns:
            bool: True if the trees are equal, False otherwise.

        比较两个二叉树是否相等。

        参数：
            other (Optional[TreeNode]): 要比较的另一棵树。

        返回：
            bool: 如果二叉树相等返回 True，否则返回 False。
        """
        ...

    def __str__(self) -> str:
        """
        Return a string representation of the binary tree.

        Returns:
            str: String representation of the binary tree.

        返回二叉树的字符串表示形式。

        返回：
            str: 二叉树的字符串表示形式。
        """
        ...

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the binary tree.

        Returns:
            str: Detailed string representation of the binary tree.

        返回二叉树的详细字符串表示形式。

        返回：
            str: 二叉树的详细字符串表示形式。
        """
        ...
