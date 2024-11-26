from typing import Generic, Iterator, TypeVar, Optional

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, data: T, next: Optional["Node[T]"] = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

'''
з початком програми як ми писали на парі в мене код не працював
виводило наступну помилку:
line 1, in <module>
    from node import Node, T, Self
ImportError: cannot import name 'Self' from 'node'
'''
class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.__head: Node[T] | None = None
        self.__len: int = 0

    def __str__(self) -> str:
        # node_datas: list[str] = []
        #
        # current: Node[T] | None = self.__head
        # while current:
        #     node_datas.append(str(current.data))
        #     current = current.next
        #
        # return f"[{' => '.join(node_datas)}]"
        return " => ".join(str(node) for node in self)

    def __len__(self) -> int:
        # length = 0
        #
        # current: Node = self.__head
        # while current:
        #     length += 1
        #     current = current.next
        #
        # return length
        return self.__len

    def __getitem__(self, idx: int) -> T:
        current_idx: int = 0
        current: Node[T] | None = self.__head

        while current:
            if current_idx == idx:
                return current.data
            current_idx += 1
            current = current.next

        raise IndexError("list index out of range")

    def __setitem__(self, idx: int, data: T) -> None:
        current_idx: int = 0
        current: Node[T] | None = self.__head

        while current:
            if current_idx == idx:
                current.data = data
                return
            current_idx += 1
            current = current.next

        raise IndexError("list index out of range")

    def __iter__(self) -> Iterator[Node]:
        current: Node[T] | None = self.__head
        while current:
            yield current
            current = current.next

    def append(self, data: T) -> None:
        self.__len += 1
        if not self.__head:
            self.__head = Node(data)
            return
        current: Node[T] = self.__head

        while current.next:
            current = current.next

        current.next = Node(data)

    def remove(self, data: T) -> None:
        if not self.__head:
            raise ValueError(f"LinkedList.remove(x): {data} not in list")

        if self.__head.data == data:
            self.__head = self.__head.next
            self.__len -= 1
            return

        current: Node[T] = self.__head

        while current.next and current.next.data  != data:
            current = current.next

        if not current.next:
            raise ValueError(f"LinkedList.remove(x): {data} not in list")
        else:
            current.next = current.next.next
            self.__len -= 1

    # ============================================================================================== #
    # ======================================== LAB 8 =============================================== #
    # ============================================================================================== #
    def reverse(self) -> "LinkedList[T]":
        reversed_list = LinkedList[T]()
        current = self.__head

        while current:
            new_node = Node(current.data)
            new_node.next = reversed_list.__head
            reversed_list.__head = new_node
            reversed_list.__len += 1
            current = current.next

        return reversed_list
    # ============================================================================================== #
    # ============================================================================================== #
    # ============================================================================================== #


if __name__ == '__main__':
    ll = LinkedList[int]()

    ll.append(1)
    ll.append(2)
    ll.append(-5)
    ll.append(105)

    print(f"{ll} has len {len(ll)}")
    print(ll[0], ll[2])
    ll[0] = 10000
    print(ll)

    for node in ll:
        print(node)

    ll.remove(2)
    print(f"{ll} has len {len(ll)}")