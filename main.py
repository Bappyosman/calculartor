import time



def countdown_timer(seconds):

    while seconds:

        mins, secs = divmod(seconds, 60)

        timeformat = '{:02d}:{:02d}'.format(mins, secs)

        print(timeformat, end='\r')

        time.sleep(1)

        seconds -= 1

    print('Times Up!')



def main():

    try:

        duration = int(input("enter the countdown duration in seconds: "))

        countdown_timer(duration)

    except ValueError:

        print("Invalid input. Please enter a valid integer.")

if __name__=="__main__"