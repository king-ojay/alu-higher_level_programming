#!/usr/bin/python3
class MyInt(int):
    """
    MyInt is a subclass of int with inverted == and != operators.
    
    Attributes:
        value (int): The integer value.
    """
    
    def __eq__(self, other):
        """
        Override the == operator to invert its functionality.
        
        Args:
            other (int): The other integer to compare.
        
        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return int(self) != other

    def __ne__(self, other):
        """
        Override the != operator to invert its functionality.
        
        Args:
            other (int): The other integer to compare.
        
        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return int(self) == other

# Testing the class
if __name__ == "__main__":
    m = MyInt(3)
    print(m)  # Should print 3
    print(issubclass(MyInt, int))  # Should print True
    m = MyInt(0)
    print(m == 0)  # Should print False
    print(m != 0)  # Should print True
    m = MyInt(89)
    print(m == 89)  # Should print False
    print(m != 89)  # Should print True
    m = MyInt(-89)
    print(m == -89)  # Should print False
    print(m != -89)  # Should print True
