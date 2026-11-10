class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self,containerarr=[]):
        self.containerarr = containerarr

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        self.containerarr.append(value)

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        try:
            self.containerarr.remove(value)
            return True
        except ValueError:
            return False

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        # TODO: implement this method
        size = len(self.containerarr)
        self.containerarr.sort()

        print(self.containerarr)
        if size == 0:
            print("No median value")
        medianindex = (size-1)//2
        
        return  self.containerarr[medianindex]

obj = Container()
obj.add(5)
obj.add(6)
obj.add(16)
obj.add(36)
obj.add(28)
obj.add(33)

print(obj.containerarr
      )

print(obj.get_median())

n=str(444)
sum =0 
for i in n:
    sum = sum + int(i)
print(sum)