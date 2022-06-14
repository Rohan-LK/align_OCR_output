import numpy as np
from easyocr import Reader
reader = Reader(['en'])

class get_lines_cls:
    def __init__(self):
        None

    def get_lines(self, image_name):
        result = reader.readtext(image_name)

        bottom_left_y_list = []
        for i in range(len(result)):
            bottom_left_y = result[i][0][0][1]
            bottom_left_y_list.append(bottom_left_y)

        lines = []
        for i in range(len(bottom_left_y_list)):
            new_line = []
            new_line.append(i)
            for j in range(len(bottom_left_y_list)):
                if i!=j:
                    if bottom_left_y_list[j] < bottom_left_y_list[i]+10 and bottom_left_y_list[j] > bottom_left_y_list[i]-10:
                        new_line.append(j)
                    else:
                        pass
                else:
                    pass
            
            lines.append(np.sort(new_line))

        lines = np.unique(np.array([i.tolist() for i in lines]))

        all_lines = []
        for i in lines:
            a_line = []
            for j in i:
                a_line.append(result[j][1])
            all_lines.append(' '.join(a_line))

        return all_lines
