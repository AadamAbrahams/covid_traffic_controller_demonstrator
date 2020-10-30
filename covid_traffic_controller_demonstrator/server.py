from Tkinter import *
import tkFont
import time
from OmlaxTCP import TCP

window = Tk()
window.geometry("1920x1080")
count = 0
Flag = False
fontStyle = tkFont.Font(family="Lucida Grande", size=55)
label = Label(window, text = "There are currently \n" + str(count)+ "\n individuals inside the shopping center.", fg = "black", bg = "light blue", font = fontStyle)
label2 = Label(window, text = "Please stand infront of the temperature sensor, \n until the screen displays either a green or red background, \n if you wish to enter.", fg = "black", bg = "light blue", font = fontStyle)
label.pack(expand = True, fill = BOTH)
label2.pack(expand = True, fill = BOTH)
TCP.server_setup(5)

while True:
	window.update_idletasks()
        data = TCP.server_recieve(512)
	if (data == '1') and (Flag == True):
		Flag = False
		label['bg'] = "light blue"
		label2['bg'] = "light blue"
		label2['text'] = "Please stand infront of the temperature sensor, \n until the screen displays either a green or red background, \n if you wish to enter."
		if count == 20:
			pass
		else:
			if count == 0:
				count = count + 1
				label['text'] = "There is currently \n" + str(count) + "\n individual inside the shopping center."
			else:
				count = count + 1
				label['text'] = "There are currently \n" + str(count) + "\n individuals inside the shopping center."
		window.update_idletasks()

	if data == '0':
		label['bg'] = "light blue"
		label2['bg'] = "light blue"
		label2['text'] = "Please stand infront of the temperature sensor, \n until the screen displays either a green or red background, \n if you wish to enter."

		if count == 0:
			pass
		else:
			if count == 2:
				count = count -1
				label['text'] = "The is currently \n" + str(count) + "\n individual inside the shopping center."
			else:
				count = count - 1
				label['text'] = "There are currently \n" + str(count) + "\n individuals inside the shopping center."
		window.update_idletasks()

	if (data != '0') and (data != '1'):
		if (float(data) < 38):
			Flag = True
			label['bg'] = "pale green"
			label2['bg'] = "pale green"
			label2['text'] = "Normal temperature detected. \n You may proceed."
		if (float(data) >= 38):
			label['bg'] = "salmon"
			label2['bg'] = "salmon"
			label2['text'] = "Above normal temperature detected. \n Access denied."
			window.update_idletasks()
			time.sleep(5)
			label2['text'] = "Please stand infront of the temperature sensor, \n until the screen displays either a green or red background, \n if you wish to enter."
			label2['bg'] = "light blue"
			label['bg'] = "light blue"
		window.update_idletasks()
	print data




