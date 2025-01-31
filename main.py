import pyautogui as pyg
import webbrowser as wb
import datetime
import time
import click

# **** Example of how to run the script: 

### **     python main.py --zoom_link "https://thingy.zoom.us/j/93562575369?pwd=WHlEd3R1ek0rZHoyd2hNUU8vdGIxUT09" --meeting_date "12-31-2021" --meeting_time "09-29-00"

# functions to format date, time
def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))

def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):

    # YY, DD, MM, HH, MM, SS - americanized
    # Year, day, month, hour (24h format, 2#), seconds
    return datetime.datetime(given_date[2], given_date[0], given_date[1], given_time[0], given_time[1], given_time[2]) # america

# join the meeting
def join_meeting(zoom_link, meeting_date, meeting_time):

    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    wait_time_sec = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print("Your ZOOM meeting starts in: " + str(wait_time_sec/60) + " min")
    time.sleep(wait_time_sec)

    # zoom app related
    ##******You need to set the path of your Brave installation below, Chrome SUX
    wb.get(using='C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s').open(zoom_link, new=2) #open zoom link in a new window
    time.sleep(5) # given time for the link to show app top-up window
    # Need to find and set the x,y coordinates on your screen of where the "Open link in Zoom" window appears on browser after the browser goes to the link supplied.
    pyg.click(x=1040, y=217, clicks=1, interval=0, button='left') # Clicks on open zoom.app option

@click.command()
@click.option('--zoom_link',
              help="The full ZOOM.us meeting link thingy",
              required=True)

@click.option('--meeting_date',
              help="Date of the meeting in the format MM-DD-YYYY",
              required=True)

@click.option('--meeting_time',
              help="Time of the meeting in the format HH-MM-SS",
              required=True)

##
def zoom_meeting(zoom_link, meeting_date, meeting_time):
    join_meeting(zoom_link, meeting_date, meeting_time)

if __name__ == '__main__':
    zoom_meeting()
