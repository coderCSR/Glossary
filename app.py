#core packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
from views import textconversion
# NLP Pkg

#Web Scrapping Pkg




window = Tk()
window.title("GLOSSARY CONVERTER")
window.geometry('700x500')


# Style
style = ttk.Style(window)
style.configure('lefttab.TNotebook',tabposition='wn')



# Tabs
tab_control=ttk.Notebook(window,style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# Add tabs to notebook
tab_control.add(tab1,text=f' {"Home":^25s}')
tab_control.add(tab2,text=f' {"File":^30s}')
tab_control.add(tab5,text=f' {"About":^30s}')

# Labels
label1 = Label(tab1,text='GLOSSARY',padx=5,pady=5)
label1.grid(column=0,row=0)
label2 = Label(tab2,text='File Processing',padx=5,pady=5)
label2.grid(column=0,row=0)
label5 = Label(tab5,text='About',padx=5,pady=5)
label5.grid(column=0,row=0)

tab_control.pack(expand=1,fill='both')

# Functions 
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("PDF Files",".pdf"),("All files","*")))
	

def get_file_summary():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("PDF Files",".pdf"),("All files","*")))
	a=textconversion.pdf_to_text(file1)
	final_text=a.get_text()
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)

def clear_text_file():
	displayed_file.delete('1.0',END)



#FILE PROCESSING TAB
l1=Label(tab2,text="Open File To Summarize")
l1.grid(row=1,column=1)

displayed_file = ScrolledText(tab2,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#c5cae9')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="#b9f6ca")
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab2,text="GLOSSARY", width=12,command=get_file_summary,bg='blue',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)


b3=Button(tab2,text="Close", width=12,command=window.destroy)
b3.grid(row=5,column=2,padx=10,pady=10)

# Display Screen

tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


# Allows you to edit
tab2_display_text.config(state=NORMAL)

window.mainloop()