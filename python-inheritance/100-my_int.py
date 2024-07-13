#!/usr/bin/python3
class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    
    def __eq__(self, other):
        return int(self) != other
    
    def __ne__(self, other):
        return int(self) == other
