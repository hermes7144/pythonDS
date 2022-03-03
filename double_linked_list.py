class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    # 소멸자: 객체가 사라지기 전 반드시 호출됩니다.
    # 삭제 연산 때 삭제되는 것을 확인하고자 작성했습니다.
    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
      return self.__next

    @next.setter
    def next(self, n):
        self.__next = n
 

class DoubleLinkedList:
  def __init__(self):
    # 리스트의 맨 처음과 마지막은 실제 데이터를
    # 저장하지 않는 노드입니다.이를더미노드라고 합니다.
    self.head = Node();
    self.tail = Node();

    # 초기화
    # head와 tail을 연결합니다.
    self.head.next = self.tail;
    self.tail.prev = self.head;
    # 데이터를 개수를 저장할 변수입니다.
    self.d_size = 0;
  
  def empty(self):
    if self.d_size == 0:
      return True
    else:
      return False
  
  def size(self):
    return self.d_size