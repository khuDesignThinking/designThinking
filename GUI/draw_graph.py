"""
dev : 김희성
date : 2020/11/12
dependency : resource/data/count_blink.csv

This module is called, by GUI_main.py, every ten second
input data : resource/data/count_blink.csv
output data : resource/images/graph.jpg <ovewrite this image>
Next thing I have to do is fix error
ValueError: invalid literal for int() with base 10: ' 12.1'
"""
from matplotlib import pyplot as plt
import pandas as pd

def load_source(source_directory:str = "resource/data/count_blink.csv") -> "list[int,tuple]":
    """
    if there is no csv file, make basic count_blink.csv file
    """
    try:
        data = pd.read_csv(source_directory)
    except:
        with open("resource/data/count_blink.csv", 'w') as f:
            f.write("15, 12, 15, 16, 10, 14")
            
    data = pd.read_csv(source_directory)
    string_blink_count = list(data.columns)
    int_blink_count = [int(blink_data) for blink_data in string_blink_count]
    return int_blink_count
    

def update_graph() -> None:
    """
    param: 
        y_list : count blink.csv file의 list인 부분
        
    var:
        x_list : same lenth with y_list, indicate 10 second
    raise: make count_blink.csv to graph.jpg, update graph.jpg
    """
    directory = "resource/images/graph.jpg"
    y_list = load_source()
    y_lenth = len(y_list)
    x_list = [f"{10 * sec} sec" for sec in range(y_lenth)]
    plt.plot(x_list, y_list)
    plt.xlabel('ten second')
    plt.ylabel('Blink number')
    plt.title('Blink count')

    # if os.path.isfile(directory):
    #     os.remove(directory)
    plt.savefig(directory)
    plt.close()
    #plt.show()
    return None
    

def main():
    update_graph()


if __name__ == "__main__":
    main()