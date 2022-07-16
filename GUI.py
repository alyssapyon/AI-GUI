from tkinter import *

# Variables for the model to access (INPUTS/OUTPUTS)
# Singleton Class
class InputOutput(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(InputOutput, cls).__new__(cls)
        return cls.instance

    def __init__(self, headline="", bodytext="", result=""):
        self.headline = headline
        self.bodytext = bodytext
        self.result = result

    def get_headline(self):
        return self.headline

    def set_headline(self, x):
        self.headline = x

    def get_bodytext(self):
        return self.bodytext

    def set_bodytext(self, x):
        self.bodytext = x

    def get_result(self):
        return self.result

    def set_result(self, x):
        self.result = x

Variables = InputOutput()

Variables.set_headline("First monkeypox case detected in Queensland")
Variables.set_bodytext("no local cases in Queensland...")
Variables.set_result("Disagree")

def showResults():
    # TODO: get results from model
    result = Variables.get_result()

    # DEBUG BELOW
    possibleresults = ["Agree", "Disagree", "Discusses", "Unrelated"]
    resultscolors = ["#77BA20", "#F13B3B", "#FDF73D", "#A181BD"]
    if result not in possibleresults:
        Variables.set_result("Disagree")
    index = possibleresults.index(result)
    newindex = (index+1)%4
    Variables.set_result(possibleresults[newindex])
    label_results.config(background=resultscolors[newindex])

    # refresh headline
    textbox_selectedheadline.delete(1.0, "end")
    textbox_selectedheadline.insert(1.0, Variables.get_headline())

    # refresh body text
    textbox_selectedbodytext.delete(1.0, "end")
    textbox_selectedbodytext.insert(1.0, Variables.get_bodytext())

    # refresh result
    textresult = "Predicted Stance: \n" + Variables.get_result()
    label_results.config(text = textresult)
    return

def changeHeadline(text):
    Variables.set_headline(text)
    textbox_selectedheadline.delete(1.0, "end")
    textbox_selectedheadline.insert(1.0, Variables.get_headline())

def changeBodytext(text):
    Variables.set_bodytext(text)
    textbox_selectedbodytext.delete(1.0, "end")
    textbox_selectedbodytext.insert(1.0, Variables.get_bodytext())

def getCustomHeadline():
    return customheadline_txt.get(1.0, "end-1c")

def getCustomBodytext():
    return custombodytext_txt.get(1.0, "end-1c")

# Font Size Options

class FontSize(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(FontSize, cls).__new__(cls)
        return cls.instance

    def __init__(self,):
        self.font = "Segoe UI"
        self.size = 10

    def get_font(self):
        return self.font
    def set_font(self, x):
        self.font = x

    def get_size(self):
        return self.size
    def increase_size(self):
        self.size = self.size + 2
    def decrease_size(self):
        self.size = self.size - 2
    def set_size(self, x):
        self.size = x

fontsize = FontSize()

def increaseFontSize():
    fontsize.set_font("Segoe UI")
    fontsize.increase_size()
    updateFontSize()
    return

def decreaseFontSize():
    fontsize.set_font("Segoe UI")
    fontsize.decrease_size()
    updateFontSize()
    return

def resetFontSize():
    fontsize.set_font("Segoe UI")
    fontsize.set_size(10)
    updateFontSize()
    return

def updateFontSize():
    x = (fontsize.get_font(), fontsize.get_size())
    bold = (fontsize.get_font(), fontsize.get_size(), 'bold')
    for i in all_labels:
        i.config(font=(bold))
    for j in all_buttons:
        j.config(font=(x))
    for k in all_text:
        k.config(font=(x))
    return
#################################################################################
# GUI BEGINS BELOW
# Create & Configure root
root = Tk()

root.title('Fake News Challenge - Stance Detection')
root.geometry("1000x500")
root.state('zoomed')

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

# Create & Configure frame
frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W, padx=10, pady=15)

# Create 6x5 (rows x columns) grid
Grid.rowconfigure(frame, 0, weight=7)
Grid.rowconfigure(frame, 1, weight=7)
Grid.rowconfigure(frame, 2, weight=100)
Grid.rowconfigure(frame, 3, weight=100)
Grid.rowconfigure(frame, 4, weight=50)
Grid.rowconfigure(frame, 5, weight=80)

Grid.columnconfigure(frame, 0, weight=50)
Grid.columnconfigure(frame, 1, weight=5)
Grid.columnconfigure(frame, 2, weight=40)
Grid.columnconfigure(frame, 3, weight=40)
Grid.columnconfigure(frame, 4, weight=40)

# HEADER
label_title = Label(frame, text = "FAKE NEWS CHALLENGE STAGE 1 (FNC-I) STANCE DETECTION")
label_title.config(height=0, width=0, padx=0)
label_title.config(background="#77BA20")
label_title.grid(row=0, column=0, columnspan=4, sticky=W)

# Widget Group (must nest in a frame to fit 2+ widgets in a single cell)
WG_fontbuttons = Frame(frame)
WG_fontbuttons.grid(row=0, column=4, sticky=N+S+E+W, padx=(5, 5), pady=(5, 5))
Grid.rowconfigure(WG_fontbuttons, 0, weight=1)
Grid.columnconfigure(WG_fontbuttons, 0, weight=1)
Grid.columnconfigure(WG_fontbuttons, 1, weight=2)
Grid.columnconfigure(WG_fontbuttons, 2, weight=1)

btn_decreaseFont = Button(WG_fontbuttons, text = "-", command=lambda:decreaseFontSize())
btn_decreaseFont.grid(row=0, column=0, sticky=N+S+E+W)
btn_resetFont = Button(WG_fontbuttons, text = "font", command=lambda:resetFontSize())
btn_resetFont.grid(row=0, column=1, sticky=N+S+E+W)
btn_increaseFont = Button(WG_fontbuttons, text = "+", command=lambda:increaseFontSize())
btn_increaseFont.grid(row=0, column=2, sticky=N+S+E+W)
#############################################

label_headline = Label(frame, text = "HEADLINE")
label_headline.config(height=0, width=0, padx=5)
label_headline.grid(row=1, column=0, columnspan=1, sticky=W)

label_bodytext = Label(frame, text = "BODY TEXT")
label_bodytext.config(height=0, width=0, padx=5)
label_bodytext.grid(row=1, column=2, columnspan=1, sticky=W)

# FOOTER
## Selected Headline
# Widget Group (must nest in a frame to fit 2+ widgets in a single cell)
WG_selectedheadline = Frame(frame)
WG_selectedheadline.grid(row=5, column=0, sticky=NW, padx=10, pady=(20,5))
Grid.rowconfigure(WG_selectedheadline, 0, weight=1)
Grid.rowconfigure(WG_selectedheadline, 1, weight=1)
Grid.columnconfigure(WG_selectedheadline, 0, weight=1)

label_selectedheadline = Label(WG_selectedheadline, text = "SELECTED HEADLINE")
label_selectedheadline.config(height=0, width=0, padx=0)
label_selectedheadline.grid(row=0, column=0, columnspan=1, sticky=NW)

textbox_selectedheadline = Text(WG_selectedheadline, height=3, width=35, padx=0, pady=0, wrap="word", relief='flat', background='#F0F0F0')
textbox_selectedheadline.insert(1.0, Variables.get_headline())
# textbox_selectedheadline.tag_configure("center", justify="center")
# textbox_selectedheadline.tag_add("center", 1.0, "end")
textbox_selectedheadline.grid(row=1, column=0)

## Selected Body Text
WG_selectedbodytext = Frame(frame)
WG_selectedbodytext.grid(row=5, column=2, columnspan=2, sticky=NW, padx=10, pady=(20,5))
Grid.rowconfigure(WG_selectedbodytext, 0, weight=1)
Grid.rowconfigure(WG_selectedbodytext, 1, weight=1)
Grid.columnconfigure(WG_selectedbodytext, 0, weight=1)

label_selectedbodytext = Label(WG_selectedbodytext, text = "SELECTED BODY TEXT")
label_selectedbodytext.config(height=0, width=0, padx=0)
label_selectedbodytext.grid(row=0, column=0, columnspan=1, sticky=NW)

textbox_selectedbodytext = Text(WG_selectedbodytext, height=3, width=70, padx=0, pady=0, wrap="word", relief='flat', background='#F0F0F0')
textbox_selectedbodytext.insert(1.0, Variables.get_bodytext())
textbox_selectedbodytext.grid(row=1, column=0)

## results and button
WG_getresults = Frame(frame)
WG_getresults.grid(row=5, column=4, columnspan=1, sticky=N, padx=5, pady=(10,5))
Grid.rowconfigure(WG_getresults, 0, weight=1)
Grid.rowconfigure(WG_getresults, 1, weight=1)
Grid.columnconfigure(WG_getresults, 0, weight=1)

btn_getresults = Button(WG_getresults, command=lambda:showResults(), text ="GET RESULTS")
btn_getresults.grid(row=0, column=0, columnspan=1, sticky=N)

textresult = "Predicted Stance: \n" + Variables.get_result()
label_results = Label(WG_getresults, text = textresult, background="#F13B3B")
label_results.config(height=0, width=0, padx=10, pady=10)
label_results.grid(row=1, column=0, columnspan=1, sticky=N, pady=10)

# BODY
## column 0 - HEADLINE
headline_NEWSa = "Gaming firm Razer sues IT vendor for nearly S$10 million in losses over leak of customers’ data"
headline_NEWSb = "First monkeypox case detected in Queensland"
btn_headline_NEWSa = Button(frame, wraplength=280, command=lambda:changeHeadline(headline_NEWSa), text = headline_NEWSa)
btn_headline_NEWSa.grid(row=2, column=0, sticky=N+S+E+W, padx=(5, 10), pady=(5, 5))
btn_headline_NEWSb = Button(frame, wraplength=280, command=lambda:changeHeadline(headline_NEWSb), text = headline_NEWSb)
btn_headline_NEWSb.grid(row=3, column=0, sticky=N+S+E+W, padx=(5, 10), pady=(5, 5))

# Widget Group (must nest in a frame to fit 2+ widgets in a single cell)
WG_customheadline = Frame(frame)
WG_customheadline.grid(row=4, column=0, sticky=N+S+E+W, padx=(5, 10), pady=(5, 5))
Grid.rowconfigure(WG_customheadline, 0, weight=1)
Grid.rowconfigure(WG_customheadline, 1, weight=1)
Grid.columnconfigure(WG_customheadline, 0, weight=1)


customheadline_txt = Text(WG_customheadline, height = 3, width = 30)
customheadline_txt.insert(1.0, "type your own headline here!")
customheadline_txt.grid(row=0, column=0, sticky=N+S+E+W)
btn_headline_CUSTOM = Button(WG_customheadline, text = "Custom", command=lambda:changeHeadline(getCustomHeadline()))
btn_headline_CUSTOM.grid(row=1, column=0, sticky=N+S+E+W)


## column 2-4 - BODY TEXT
bodytext_NEWSa_1 = "... Razer has pressed charges, claiming at least US$7 million (S$9.85 million) in losses from the vendor, French multinational IT company Capgemini..."
bodytext_NEWSa_2 = "... No, Razer did not take legal action against vendor, French multinational info-technology company Capgemini... no sensitive data such as credit card numbers or passwords were exposed..."
bodytext_NEWSa_3 = "... Razer allegedly sued Capgemini, which is an information technology services and consulting company...Capgemini had recommended the ELK Stack platform to Razer..."

bodytext_NEWSb_1 = "... Health authorities have detected the first confirmed case of monkeypox in Queensland on Monday...."
bodytext_NEWSb_2 = "... There are 'close to zero' concern about monkeypox, as there are no local cases in Queensland..."
bodytext_NEWSb_3 = "... Minister reportedly disappointed about the first local monkeypox case that was apparently imported from ..."

btn_bodytext_NEWSa_1 = Button(frame, wraplength=280, command=lambda:changeBodytext(bodytext_NEWSa_1), text = bodytext_NEWSa_1, )
btn_bodytext_NEWSa_1.grid(row=2, column=2, sticky=N+S+E+W, padx=(10, 5), pady=(5, 5))
btn_bodytext_NEWSa_2 = Button(frame, wraplength=280, command=lambda:changeBodytext(bodytext_NEWSa_2), text = bodytext_NEWSa_2)
btn_bodytext_NEWSa_2.grid(row=2, column=3, sticky=N+S+E+W, padx=( 5, 5), pady=(5, 5))
btn_bodytext_NEWSa_3 = Button(frame, wraplength=280, command=lambda:changeBodytext(bodytext_NEWSa_3), text = bodytext_NEWSa_3)
btn_bodytext_NEWSa_3.grid(row=2, column=4, sticky=N+S+E+W, padx=( 5, 5), pady=(5, 5))

btn_bodytext_NEWSb_1 = Button(frame, wraplength=280, command=lambda:changeBodytext(bodytext_NEWSb_1), text = bodytext_NEWSb_1)
btn_bodytext_NEWSb_1.grid(row=3, column=2, sticky=N+S+E+W, padx=(10, 5), pady=(5, 5))
btn_bodytext_NEWSb_2 = Button(frame, wraplength=280, command=lambda:changeBodytext(bodytext_NEWSb_2), text = bodytext_NEWSb_2)
btn_bodytext_NEWSb_2.grid(row=3, column=3, sticky=N+S+E+W, padx=( 5, 5), pady=(5, 5))
btn_bodytext_NEWSb_3 = Button(frame, wraplength=280, command=lambda:changeBodytext(bodytext_NEWSb_3), text = bodytext_NEWSb_3)
btn_bodytext_NEWSb_3.grid(row=3, column=4, sticky=N+S+E+W, padx=( 5, 5), pady=(5, 5))

# Widget Group (must nest in a frame to fit 2+ widgets in a single cell)
WG_custombodytext = Frame(frame)
WG_custombodytext.grid(row=4, column=2, columnspan=3, sticky=N+S+E+W, padx=(10, 5), pady=(5, 5))
Grid.rowconfigure(WG_custombodytext, 0, weight=1)
Grid.rowconfigure(WG_custombodytext, 1, weight=1)
Grid.columnconfigure(WG_custombodytext, 0, weight=1)

custombodytext_txt = Text(WG_custombodytext, height = 3)
custombodytext_txt.insert(1.0, "type your own body text here!")
custombodytext_txt.grid(row=0, column=0, sticky=N+S+E+W)
btn_bodytext_CUSTOM = Button(WG_custombodytext, text = "Custom", command=lambda:changeBodytext(getCustomBodytext()))
btn_bodytext_CUSTOM.grid(row=1, column=0, sticky=N+S+E+W)

# component list
all_labels = [label_title, label_headline, label_bodytext, label_selectedheadline, label_selectedbodytext, label_results]
all_buttons = [btn_increaseFont, btn_resetFont, btn_decreaseFont, btn_getresults, btn_headline_NEWSa, btn_headline_NEWSb, btn_headline_CUSTOM, btn_bodytext_NEWSa_1, btn_bodytext_NEWSa_2, btn_bodytext_NEWSa_3, btn_bodytext_NEWSb_1, btn_bodytext_NEWSb_2, btn_bodytext_NEWSb_3, btn_bodytext_CUSTOM]
all_text = [textbox_selectedheadline, textbox_selectedbodytext, customheadline_txt, custombodytext_txt]

updateFontSize()
for i in all_buttons:
    i.config(background="#D6F0B4")


mainloop()


# dynamic grid: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
# dynamic label wrap: https://stackoverflow.com/questions/62485520/how-to-wrap-the-text-in-a-tkinter-label-dynamically
