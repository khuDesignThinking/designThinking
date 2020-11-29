from matplotlib import pyplot as plt
import csv

# < int_blink_count = [int(blink_data) for blink_data in string_blink_count] 
#   ValueError: invalid literal for int() with base 10: '' > 
# 오류가 뜨는 경우 count_blink.csv 파일을 지우세요

def load_source(source_directory:str = "dataset/count_blink.csv"):
    """
    If there is no csv file, This function make count_blink.csv file
    """
    try: #Check whether count_blink.csv exist.
        with open(source_directory, 'r') as f:
            pass
    except:
        with open(source_directory, 'w', newline='') as f:
            writer = csv.writer(f)
            d = [0]
            writer.writerows([d]) # this is test data
    with open(source_directory, 'r') as f:
        data = f.read()
    string_blink_count = data.split(",")
    int_blink_count = [int(blink_data) for blink_data in string_blink_count]
    return int_blink_count
    

def update_graph(image_directory: str = "dataset/graph.jpg"):
    """
    This function make "resource/images/graph.jpg" file
    param: 
        y_list : count blink.csv file's value
        
    var:
        x_list : same lenth with y_list, indicate 10 second
    raise: make count_blink.csv to graph.jpg, update graph.jpg
    """
    y_list = load_source()
    y_lenth = len(y_list)
    x_list = [f"{10 * sec} sec" for sec in range(y_lenth)]
    plt.plot(x_list, y_list)
    plt.xlabel('ten second')
    plt.ylabel('Blink number')
    plt.title('Blink count')
    plt.savefig(image_directory)
    plt.close()
    if(len(x_list)>8):
        del x_list[0]
        del y_list[0]
    return None
    

def main():
    update_graph()


if __name__ == "__main__":
    main()
