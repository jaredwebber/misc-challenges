# https://leetcode.com/problems/clone-graph

from typing import Optional


# Provided Node class
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        val_map: dict[int, list[int]] = {}

        nodes: list[Node] = [node]
        while len(nodes) > 0:
            curr: Node = nodes.pop()
            curr_list: list[int] = []
            if curr:
                for n in curr.neighbors:
                    if not val_map.get(n.val):
                        nodes.insert(0, n)

                    curr_list.append(n.val)
                val_map[curr.val] = curr_list

        node_map: dict[int, Node] = {}
        for val, neighbors in val_map.items():
            if not node_map.get(val):
                node_map[val] = Node(val=val, neighbors=[])
            for n in neighbors:
                if not node_map.get(n):
                    node_map[n] = Node(val=n, neighbors=[])
                node_map[val].neighbors.append(node_map[n])

        return node_map.get(node.val)
