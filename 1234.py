import serial
f = open('xyz3.txt', 'w')


class SerialArduino:
    def __init__(self):

        get_inputbtn = int(input('input 0 to start: '))
        if get_inputbtn == 0:
            ser = serial.Serial('COM5',  baudrate=115200)
        while True and get_inputbtn == 0:
            line = ser.readline()
            self.check_inf(line)
        ser.close()

    def check_inf(self, input_inf):
        if input_inf != b'':
            get_cm = str(input_inf).split("\t")
            
            # print('input_inf: ', get_cm)
            print('input_inf is' ,get_cm,'\n')
            f.writelines(get_cm+"\n")


if __name__ == '__main__':
    try:
        SerialArduino()
    except KeyboardInterrupt:
        print("Shutting down")
        f.close()
