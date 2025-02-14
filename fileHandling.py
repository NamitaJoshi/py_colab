import src as s


def file_read_mode(file_name, mode):
    try:
        with open(file_name, mode) as file:
            count = 0
            print(f"file {file_name} is success fully worked in {mode}")
            mode_r_w_a(file , str(count) )
            count += 1
    except Exception as e:
        print(e)
        display_error_output_read(file_name, mode)
        return None


def get_file_exist():
    return "C:\\Users\\dell\\PycharmProjects\\py_colab\\resources\\" + "description.txt"


def get_random_file():
    return "newfile.txt"


def mode_r():
    #print("hello")
    file_read_mode(get_random_file(), "r")
    file2 = file_read_mode(get_file_exist(), 'r')


def display_error_output_read(file_name, mode):
    print(f"failed to read as file {file_name} don't exist using mode {mode}")



def mode_w():#write only
    file_read_mode(get_random_file(), "w")
    #file_read_mode(get_file_exist(), 'w')

def mode_append():
    file_read_mode(get_random_file(), "a")
    print("\n")
    file_read_mode(get_file_exist(), 'a+')

def mode_r_w_a(file, count):
    file.write("here I am at line "+count)


if __name__ == "__main__":
    #mode_w()
    mode_append()
    #mode_r_w_a()
    #mode_append()
    #mode_r()

