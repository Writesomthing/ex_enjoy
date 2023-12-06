
import sys
from collections import deque
input = sys.stdin.readline

# a, b, c, d ...
input_code = list(input().strip())

cnt_dic = {}
# 빈도수와 이진코드를 반환함.
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.code = None
        self.Sum = False

#
class BST:
    def __init__(self):
        # 그냥 제일 큰 수로 기준을 잡자.
        self.root = Node(Sum_str_len+1)
        self.left = None

        self.right = None
        self.res = {}

    def add_node(self, code_):
        # code_ == ascii 코드
        target_node = self.root
        binary_code = None

        # 적용 이후~ dp 적용 하면?
        def convert_binary(coord):
            nonlocal binary_code
            coord_ = str(coord)
            if binary_code is None:
                binary_code = coord_
            else:
                binary_code += coord_

        while target_node is not None:

#...
