# Инкапсуляция

class Map:
    __count = 0
    def __init__(self):
        Map.__count += 1
    def __del__(self):
        Map.__count -= 1
    def qtyObject():
        return Map.__count
 
a = Map()
b = Map()
print(Map.qtyObject())