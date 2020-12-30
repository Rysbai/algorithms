test_data = """
s 209027527 465681241
- 364109675
? 648433698
? 369072515
- 384851838
? 434465164
? 988187570
s 689656112 799574286
s 487889785 593663747
s 28062399 437825162
s 205291457 515367700
+ 554939149
+ 300593336
+ 595570265
s 146900570 390853981
+ 411987627
- 254345813
+ 227319692
? 265053786
? 227319692
+ 677382194
? 677382194
+ 629050678
s 841558476 217510399
- 411987627
s 0 677382194
s 948848788 956831062
- 929644014
+ 364027698
s 674697217 752227904
s 300593336 977975530
? 369972355
? 529396635
+ 370544842
? 597947844
? 727746481
? 211895675
s 370544842 211895675
s 233920146 75270979
? 536537986
s 634496442 75490832
? 862831291
? 499356174
+ 199630631
+ 719683043
+ 311904507
+ 154244273
- 719683043
- 154244273
+ 448167377
s 679990234 943538397
+ 976790042
+ 382632133
s 357092137 313354496
+ 946342891
+ 355553820
s 750004486 706266845
s 984477975 362304915
? 497555428
s 2415866 958678226
s 241433926 688367375
? 998552036
? 356089308
s 492352178 448614537
- 410890264
? 183570572
- 19601932
? 860952766
+ 342858131
s 904690407 860952766
- 860810490
- 65609594
? 607473467
s 231344136 803108170
- 388772919
+ 247080262
? 247080262
s 416523040 773713980
- 836719276
- 63927696
- 473138626
+ 889586345
s 867589292 731326422
? 423493606
+ 613737368
- 613737368
+ 137736145
s 853482950 248653408
? 661343974
s 87680021 951417152
s 448142088 311879218
? 167561091
- 727022254
- 782082532
- 790456616
+ 982275395
- 311879218
s 230737860 338172294
s 21713170 641411075
s 798020559 417718463
+ 591947955
? 798020559
- 230184996
? 591947955
+ 534111576
? 713638125
+ 480914390
s 255606523 263910716
? 959183165
+ 120759900
- 982487038
+ 344374296
- 641411075
s 352958324 926938085
? 576858998
s 727934045 521861441
- 777084
+ 195202155
? 721489401
s 150123290 944050687
? 405992381
s 455783517 557934389
? 627500266
? 378628793
+ 55608165
s 561832276 355759672
? 101975502
+ 114177930
s 567842196 361769592
+ 396542754
- 322454417
+ 513110143
- 437961016
- 98840021
- 840619198
? 396542754
s 999793292 793720688
- 368065190
- 654209559
- 465091617
- 16394592
- 707406745
s 107985617 257345638
? 535030022
? 535030022
- 535030022
+ 604265055
? 668950342
s 21713170 815640567
? 159163006
? 236158776
+ 538332248
+ 975601996
? 780972634
- 269040511
+ 507013212
- 387232663
? 899368917
? 899368917
? 902873067
s 348222918 936682404
+ 228235183
+ 7555876
? 504246446
s 215451512 221769960
? 555846477
? 555846477
s 21713170 815640567
+ 919740922
? 98128385
s 521286977 601766042
+ 497060888
+ 738200422
s 21713170 861004046
? 459532410
s 984184693 823475568
+ 461317072
s 335536187 547326622
- 818540898
s 343193180 182484055
- 124177632
+ 210461582
? 142394280
? 604292922
- 210461582
? 540857323
? 459532410
- 155496668
- 698887282
? 595895199
- 459532410
+ 936693273
s 982400031 936693273
- 135873475
+ 731009951
- 556033411
? 173879972
? 564379882
+ 15455050
+ 464862049
? 965360258
- 475716748
+ 815691131
s 601740169 464862049
? 555952654
+ 971023926
? 9234756
+ 273781028
- 840397754
- 220610268
+ 94335659
? 954313575
- 328940993
? 850629600
s 788370236 97552644
s 403181303 266303183
+ 218249085
s 258760806 274894391
? 604265055
+ 18983480
? 286595600
s 18983480 884835051
s 845364541 711216111
- 605778540
s 845364541 711216111
- 164496712
- 210043594
- 171832763
? 841442672
+ 229138448
? 653031706
s 630607560 678200994
+ 912627948
? 496560814
s 52034377 671970064
- 982105224
? 601592752
s 433039799 373937432
- 942983782
- 6066145
s 338607353 279504986
s 648409534 589307167
s 678371981 740653958
- 632079556
? 888547479
s 18983480 959881114
- 122509654
? 572805443
- 950871567
? 497169741
- 130316935
- 146340659
? 221386722
s 349967798 621740558
? 605430880
+ 771192880
- 573234030
? 895078299
+ 265737774
? 265737774
- 527190309
+ 776467788
- 764335869
+ 825328072
- 660606083
s 790534533 258001770
- 301762302
s 250645930 306398792
s 355619637 992470492
? 330304276
s 366598623 0
s 557307853 190709230
? 773988505
- 557307853
+ 904060958
- 190709230
+ 433662166
s 159546565 394836239
? 493285377
+ 114178264
? 969491289
s 21713170 895337794
+ 954503888
- 729777862
+ 234681583
? 70104200
+ 123704321
? 302910011
- 948618333
- 713812247
- 544663032
"""

import sys

prev_s = 0
p = 1000000001

sys.setrecursionlimit(100000)


class Node:
    key: int or None
    parent: 'Node' or None
    left: 'Node' or None
    right: 'Node' or None
    subtree_sum: int

    def __init__(self, key: int = None, parent: 'Node' = None,
                 left: 'Node' = None, right: 'Node' = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.subtree_sum = 0

    def search(self, key: int):
        stopped_node, is_found = self._search(key)

        print('Found' if is_found else 'Not found')
        return self._splay(stopped_node)

    def add(self, key) -> 'Node':
        if not self.key:
            self.key = key
            return self

        stopped_node, is_found = self._search(key)
        if is_found:
            return self._splay(stopped_node)

        side = 'left' if key < stopped_node.key else 'right'

        replace_node = stopped_node.__getattribute__(side)
        new_node = Node(key=key, **{side: replace_node})
        stopped_node.__setattr__(side, new_node)
        new_node.parent = stopped_node

        if replace_node:
            replace_node.parent = new_node

        new_node.update_subtree_sum()
        self._msg_parents_subtree_sum(new_node, amount=new_node.key, operator='+')
        return self._splay(new_node)

    def remove(self, key) -> 'Node':
        node = self
        new_root = None

        if node.key is None:
            return node

        if not node.left and not node.right and node.key == key:
            node.key = None
            return node

        stopped_node, is_found = self._search(key)
        if is_found:
            node = self._splay(stopped_node)
            if node.right:
                node.right.parent = None
            if node.left:
                node.left.parent = None
            else:
                return node.right

            new_root = self._merge(node.left, node.right)

        return new_root if new_root else self._splay(stopped_node)

    def section_sum2(self, left: int, right: int):
        global prev_s
        generic_root = self
        while True:
            if not generic_root.key:
                break

            if left <= generic_root.key <= right:
                break

            if generic_root.left and generic_root.left.key > left:
                generic_root = generic_root.left
                continue

            if generic_root.right and generic_root.right.key < right:
                generic_root = generic_root.right
                continue

            break
        generic_root = self._splay(generic_root)
        s = generic_root._section_sum(left, right)
        prev_s = s
        print(s)

        return self

    def section_sum(self, left: int, right: int):
        global prev_s
        l_node, _ = self._search(left)
        s = 0
        next_node = l_node
        while True:
            if not next_node or not next_node.key:
                break

            if next_node.key < left:
                next_node = self._next_node(next_node)
                continue

            if next_node.key > right:
                break

            s += next_node.key

            next_node = self._next_node(next_node)
        print(s)
        prev_s = s
        return self

    def _section_sum(self, left: int, right: int) -> int:
        s = 0
        if not self.key:
            return s

        if left <= self.key <= right:
            s += self.key

        if self.key > left and self.left:
            s += self.left._section_sum(left, right)

        if self.key < right and self.right:
            s += self.right._section_sum(left, right)

        return s

    @staticmethod
    def _next_node(node: 'Node') -> 'Node' or None:
        if node.right:
            return node.right.min()

        while True:
            if not node.parent:
                return None

            if node.parent.left == node:
                return node.parent

            node = node.parent

    @staticmethod
    def _msg_parents_subtree_sum(node: 'Node', amount: int, operator: str) -> None:
        parent = node.parent
        while parent:
            if operator == '+':
                parent.subtree_sum += amount
            else:
                parent.subtree_sum -= amount

            parent = parent.parent

    def _search(self, s_key) -> ('Node', bool):
        if self.key is None:
            return self, False

        node = self

        while True:
            if s_key == node.key:
                return node, True

            if s_key < node.key and node.left:
                node = node.left
                continue

            if s_key > node.key and node.right:
                node = node.right
                continue

            return node, False

    def _splay(self, node: 'Node') -> 'Node':
        while True:
            if node.parent is None:
                return node

            side = 'left' if node.parent.left == node else 'right'

            if node.parent.parent is None:
                node = self._zig(node, side=side)
                continue

            if node.parent.parent.__getattribute__(side) == node.parent:
                node = self._zig_zig(node, side=side)
            else:
                node = self._zig_zag(node, side=side)

    def _merge(self, l_node: 'Node', r_node: 'Node') -> 'Node':
        l_node = self._splay(l_node.max())
        l_node.right = r_node
        if r_node:
            r_node.parent = l_node

        return l_node

    def max(self) -> 'Node':
        node = self
        while True:
            if node.right:
                node = node.right
                continue
            break

        return node

    def min(self) -> 'Node':
        node = self
        while True:
            if node.left:
                node = node.left
                continue
            break

        return node

    @staticmethod
    def _zig_zig(node: 'Node', side: str) -> 'Node':
        opposite_side = 'right' if side == 'left' else 'left'
        c_parent = node.parent
        c_grandpa = c_parent.parent
        c_great_grandpa = c_grandpa.parent

        # current grandpa
        c_parent_op_child = c_parent.__getattribute__(opposite_side)
        c_grandpa.__setattr__(side, c_parent_op_child)
        if c_parent_op_child:
            c_parent_op_child.parent = c_grandpa
        c_grandpa.parent = c_parent

        # current parent
        c_parent.__setattr__(opposite_side, c_grandpa)
        c_node_op_child = node.__getattribute__(opposite_side)
        c_parent.__setattr__(side, c_node_op_child)
        if c_node_op_child:
            c_node_op_child.parent = c_parent
        c_parent.parent = node

        # current node
        node.__setattr__(opposite_side, c_parent)
        node.parent = c_great_grandpa
        if c_great_grandpa:
            if c_great_grandpa.left == c_grandpa:
                c_great_grandpa.left = node
            else:
                c_great_grandpa.right = node

        c_grandpa.update_subtree_sum()
        c_parent.update_subtree_sum()
        node.update_subtree_sum()

        return node

    def update_subtree_sum(self):
        s = 0
        if self.left:
            s += self.left.subtree_sum + self.left.key

        if self.right:
            s += self.right.subtree_sum + self.right.key

        self.subtree_sum = s

    @staticmethod
    def _zig_zag(node: 'Node', side: str) -> 'Node':
        opposite_side = 'right' if side == 'left' else 'left'
        c_parent = node.parent
        c_grandpa = c_parent.parent
        c_great_grandpa = c_grandpa.parent

        # current grandpa
        c_node_side_child = node.__getattribute__(side)
        c_grandpa.__setattr__(opposite_side, c_node_side_child)
        if c_node_side_child:
            c_node_side_child.parent = c_grandpa
        c_grandpa.parent = node

        # current parent
        c_node_op_child = node.__getattribute__(opposite_side)
        c_parent.__setattr__(side, c_node_op_child)
        if c_node_op_child:
            c_node_op_child.parent = c_parent
        c_parent.parent = node

        # current node
        node.__setattr__(side, c_grandpa)
        node.__setattr__(opposite_side, c_parent)
        node.parent = c_great_grandpa
        if c_great_grandpa:
            if c_great_grandpa.left == c_grandpa:
                c_great_grandpa.left = node
            else:
                c_great_grandpa.right = node

        c_grandpa.update_subtree_sum()
        c_parent.update_subtree_sum()
        node.update_subtree_sum()

        return node

    @staticmethod
    def _zig(node: 'Node', side: str) -> 'Node':
        opposite_side = 'right' if side == 'left' else 'left'
        c_parent = node.parent
        c_grandpa = c_parent.parent

        c_node_op_side = node.__getattribute__(opposite_side)
        c_parent.__setattr__(side, c_node_op_side)
        if c_node_op_side:
            c_node_op_side.parent = c_parent

        node.__setattr__(opposite_side, c_parent)
        c_parent.parent = node
        node.parent = c_grandpa
        if c_grandpa:
            if c_grandpa.left and c_grandpa.left.key == c_parent.key:
                node.parent.left = node
            elif c_grandpa.right and c_grandpa.right.key == c_parent.key:
                node.parent.right = node

        c_parent.update_subtree_sum()
        node.update_subtree_sum()
        return node

    def __str__(self, level=0, side='root'):
        ret = '\t'*level + f'{side}: ' + \
              str(self.key) + \
              f', parent: {self.parent and self.parent.key}, subtree_sum: {self.subtree_sum}' '\n'
        if self.left:
            ret += self.left.__str__(level + 1, 'left')

        if self.right:
            ret += self.right.__str__(level + 1, 'right')

        return ret


operators = {
    '+': 'add',
    '-': 'remove',
    '?': 'search',
    's': 'section_sum2'
}


def dev_version():
    node = Node()
    func = lambda x: (x % p + prev_s % p) % 1000000001
    for row in test_data.split('\n'):
        if not row:
            continue
        code, *params = row.split()
        node = node.__getattribute__(operators[code])(*[func(int(i)) for i in params])
        # print({'code': code, 'params': params, 'afterF': [func(int(i)) for i in params]})
        # print(node)
        # print('-'*100)


def main():
    func = lambda x: (x % p + prev_s % p) % 1000000001
    n = int(input())
    node = Node()
    for _ in range(n):
        code, *params = input().split()
        node = node.__getattribute__(operators[code])(*[func(int(i)) for i in params])


def test_section_sum():
    ten = Node(key=10)
    eight = Node(key=8, right=ten)
    ten.parent = eight
    five = Node(key=5)
    seven = Node(key=7, left=five, right=eight)
    eight.parent = seven
    five.parent = seven

    root = Node(key=15, left=seven)
    seven.parent = root

    print(root)
    root.section_sum2(4, 9)


if __name__ == '__main__':
    dev_version()
