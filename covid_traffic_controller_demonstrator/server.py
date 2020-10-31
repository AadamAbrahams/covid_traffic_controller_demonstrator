from Tkinter import *
import tkFont
import time
from OmlaxTCP import TCP


def main():
    """
    Generates GUI to illustrate number of individuals within a building
    Listens for messages on port 1234 for updates on directional movement
    and temperature, and further updates the GUI accordingly.
    """
    window = Tk()
    # Creates a new GUI window.
    window.geometry("1920x1080")
    # Configures display ratio for the window.
    count = 0
    Flag = False
    fontStyle = tkFont.Font(family="Lucida Grande", size=55)
    # Configure GUI text font
    label = Label(window, text="There are currently \n"
                  + str(count) + "\n individuals inside the shopping center.",
                  fg="black", bg="light blue", font=fontStyle)
    # Creates a label to display number of individuals in building.
    label2 = Label(window,
                   text="Please stand infront of the temperature sensor,"
                   "\n until the screen displays either a green or red "
                   "background, \n if you wish to enter.",
                   fg="black", bg="light blue", font=fontStyle)
    # Creates a label to display instruction the user is requested to perform.
    label.pack(expand=True, fill=BOTH)
    # Link the label to the GUI window.
    label2.pack(expand=True, fill=BOTH)
    # Link the label to the GUI window.
    TCP.server_setup(5)
    # Establish device as a server and open port for listening.

    while True:
        window.update_idletasks()
        # Updates entire GUI layout and text.
        data = TCP.server_recieve(512)
        # Retrieves message sent by client.
        if (data == '1') and Flag:
            Flag = False
            label['bg'] = "light blue"
            # Changes top half of GUI background to light blue.
            label2['bg'] = "light blue"
            # Changes bottom half of GUI background to light blue.
            label2['text'] = "Please stand infront of the temperature "
            "sensor, \n until the screen displays either a green or "
            "red background, \n if you wish to enter."
            if count == 20:
                pass
            else:
                if count == 0:
                    count = count + 1
                    # Increment number of individuals in store.
                    label['text'] = "There is currently \n" + str(count)
                    "\n individual inside the shopping center."
                    # Changes top half text to new number in building.
                else:
                    count = count + 1
                    # Increment number of individuals in store.
                    label['text'] = "There are currently \n" + str(count)
                    "\n individuals inside the shopping center."
                    # Changes top half text to new number in building.
            window.update_idletasks()
            # Updates entire GUI layout and text.

        if data == '0':
            # Checks if message reflects an individual leaving building
            label['bg'] = "light blue"
            # Changes top half of GUI background to light blue.
            label2['bg'] = "light blue"
            # Changes bottom half of GUI background to light blue.
            label2['text'] = "Please stand infront of the temperature "
            "sensor, \n until the screen displays either a green or "
            "red background, \n if you wish to enter."
            if count == 0:
                pass
            else:
                if count == 2:
                    count = count - 1
                    # Decrement number of individuals in store.
                    label['text'] = "The is currently \n" + str(count)
                    "\n individual inside the shopping center."
                    # Changes top half text to new number in building.
                else:
                    count = count - 1
                    # Decrement number of individuals in store.
                    label['text'] = "There are currently \n" + str(count)
                    "\n individuals inside the shopping center."
                    # Changes top half text to new number in building.
            window.update_idletasks()
            # Updates entire GUI layout and text.

        if (data != '0') and (data != '1'):
            # Checks if recieved message is a temperature value.
            if (float(data) < 38):
                # Checks if individuals temperature is regular.
                Flag = True
                label['bg'] = "pale green"
                # Changes top half of GUI background to pale green.
                label2['bg'] = "pale green"
                # Changes bottom half of GUI background to pale green.
                label2['text'] = "Normal temperature detected. "
                "\n You may proceed."
                # Changes bottom half text to indicate normal temp scan.
            if (float(data) >= 38):
                # Checks if individuals temperature is above the norm.
                label['bg'] = "salmon"
                # Changes top half of GUI background to salmon.
                label2['bg'] = "salmon"
                # Changes bottom half of GUI background to salmon.
                label2['text'] = "Above normal temperature detected. "
                "\n Access denied."
                # Changes bottom half text to indicate above normal temp scan.
                window.update_idletasks()
                # Updates entire GUI layout and text.
                time.sleep(5)
                label2['text'] = "Please stand infront of the temperature "
                "sensor, \n until the screen displays either a green or "
                "red background, \n if you wish to enter."
                # Changes bottom half text to request temperature scan.
                label2['bg'] = "light blue"
                # Changes top half of GUI background to light blue.
                label['bg'] = "light blue"
                # Changes bottom half of GUI background to light blue.
            window.update_idletasks()
            # Updates entire GUI layout and text.
        print(data)
        # Prints message recieved from client.


if __name__ == "__main__":
    setup()
    main()
