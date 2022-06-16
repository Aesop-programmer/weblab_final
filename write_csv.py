import serial
import csv
f = open('xyz3.txt', 'w')
namefile = 'pos.csv'

header0= "packnum"
header1 = "gx"
header2 = "gy"
header3 = "gz"
header4 = "ax"
header5 = "ay"
header6 = "az"

fieldnames = [header0,header1, header2, header3,header4,header5,header6]

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
            get_cm = str(input_inf).split("'")[1].split("\\")[0]
            # print('input_inf: ', get_cm)
            print('input_inf is' ,get_cm,'\n')
            f.writelines(get_cm+"\n")
            f.flush



cnt=1
if __name__ == '__main__':
    try:
        SerialArduino()
    except KeyboardInterrupt:
        print("Shutting down")
        f.close()
        with open(namefile,'w') as csv_file:
            csv_writer =csv.DictWriter(csv_file,fieldnames=fieldnames)
            csv_writer.writeheader()
        with open(namefile, 'a',newline='') as csv_file:
            csv_writer=csv.DictWriter(csv_file, fieldnames=fieldnames)
            with open('xyz3.txt', 'r') as f:
                for line in f:
                    if (len(line.split(","))==9):
                        info= {
                            header0: cnt,
                            header1:line.split(",")[0],
                            header2:line.split(",")[1],
                            header3:line.split(",")[2],
                            header4:line.split(",")[3],
                            header5:line.split(",")[4],
                            header6:line.split(",")[5]
                            
                        }
                        cnt+=1
                        csv_writer.writerow(info)
            
    