from matplotlib import pyplot as plt
from dataclasses import dataclass

@dataclass
class ComplexArea:
    x_min: float = 0
    x_max: float = 0
    y_min: float = 0
    y_max: float = 0

@dataclass
class MandelSet: 
    complex_area: ComplexArea
    matrix: list[list[int]]

    def __init__(self): 
        self.__parse_file()

    def __parse_file(self, filename="../matrix.txt"):
        with open(filename, 'r') as file:
            
            width = int(file.readline())
            x_min, x_max, y_min, y_max = map(float, file.readline().split())
            
            self.complex_area = ComplexArea(x_min, x_max, y_min, y_max)
            
            data = [int(x) for x in file.readline().split()]
            
        self.matrix = [data[i:i+width] for i in range(0, len(data), width)]
    

    def show(self) -> None:
        plt.imshow(self.matrix,
                   extent = (self.complex_area.x_min, 
                             self.complex_area.x_max, 
                             self.complex_area.y_min, 
                             self.complex_area.y_max),
                   cmap='rainbow',
                   aspect='auto')
        plt.axis('off')
        plt.show()


    def save(self, filename: str = "../mandel_res_reg.png") -> None:
        plt.imshow(self.matrix,
                   extent = (self.complex_area.x_min, 
                             self.complex_area.x_max, 
                             self.complex_area.y_min, 
                             self.complex_area.y_max),
                   cmap='twilight_shifted',
                   aspect='auto')
        plt.axis('off')
        plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)



if __name__ == "__main__":
    mandel_set = MandelSet()
    #mandel_set.save()
    mandel_set.show()