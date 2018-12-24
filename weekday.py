import calendar
from datetime import date
from datetime import datetime
def main():    
    while(True):
        cdate = input("(Ctrl+C = Quit)\nPlease enter required date[Use dd/mm/yyyy]: ")
        cdobj = datetime.strptime(cdate,'%d/%m/%Y')
        print(calendar.day_name[cdobj.weekday()])
    return
#-----------------------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print("--------- Program Terminated ---------")
