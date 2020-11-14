from matplotlib import pyplot as plt


def load_source(source_directory:str = "C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\dataset\\count_blink.csv") -> list:
    """
    If there is no csv file, This function make count_blink.csv file
    """
    try: #Check whether count_blink.csv exist.
        with open(source_directory, 'r') as f:
            pass
    except:
        with open(source_directory, 'w') as f:
            f.write("15, 12, 15, 16, 10, 14") # this is test data

    with open(source_directory, 'r') as f:
        data = f.read()
    string_blink_count = data.split(",")
    int_blink_count = [int(blink_data) for blink_data in string_blink_count]
    return int_blink_count
    

def update_graph(image_directory: str = "C:\\Users\\dkwjd\\Desktop\\eye_blink_detector-master\\eye_blink_detector-master\\dataset\\graph.jpg") -> None:
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
    #plt.show()
    return None
    

def main():
    update_graph()


if __name__ == "__main__":
    main()
