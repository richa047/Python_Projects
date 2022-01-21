from tkinter import *
from tkinter.ttk import ComboBox


root = Tk()
root.geometry('500x400')
root.title('Translator')
#root.iconbitmap('translator.ico')
root.resizable(False,False)
root.configure(bg='turquoise1')

lan_dict = {'german': 'de', 'belarusian': 'be', 'galician': 'gl', 'macedonian': 'mk',
 'urdu': 'ur', 'polish': 'pl', 'sesotho': 'st', 'swahili': 'sw', 'icelandic': 'is', 'turkish': 'tr', 'romanian': 'ro', 
 'somali': 'so', 'hmong': 'hmn', 'indonesian': 'id', 'khmer': 'km', 'hungarian': 'hu', 'catalan': 'ca', 
 'kyrgyz': 'ky', 'finnish': 'fi', 'sundanese': 'su', 'serbian': 'sr', 'italian': 'it', 'portuguese': 'pt',
  'czech': 'cs', 'basque': 'eu', 'japanese': 'ja', 'amharic': 'am', 'persian': 'fa', 'tajik': 'tg', 
  'yiddish': 'yi', 'xhosa': 'xh', 'estonian': 'et', 'telugu': 'te', 'marathi': 'mr', 'shona': 'sn', 'pashto': 'ps',
   'gujarati': 'gu', 'dutch': 'nl', 'malagasy': 'mg', 'latin': 'la', 'igbo': 'ig', 'yoruba': 'yo', 'french': 'fr',
    'armenian': 'hy', 'afrikaans': 'af', 'filipino': 'tl', 'english': 'en', 'uzbek': 'uz', 'albanian': 'sq',
     'vietnamese': 'vi', 'latvian': 'lv', 'javanese': 'jw', 'croatian': 'hr', 'scots gaelic': 'gd', 'slovak': 'sk', 
     'spanish': 'es', 'esperanto': 'eo', 'corsican': 'co', 'hindi': 'hi', 'danish': 'da', 'bulgarian': 'bg', 'maori': 'mi',
      'hawaiian': 'haw', 'bosnian': 'bs', 'georgian': 'ka', 'malay': 'ms', 'luxembourgish': 'lb', 'haitian creole': 'ht', 
      'chichewa': 'ny', 'bengali': 'bn', 'russian': 'ru', 'thai': 'th', 'tamil': 'ta', 'cebuano': 'ceb', 'Filipino': 'fil',
       'chinese (traditional)': 'zh-tw', 'malayalam': 'ml', 'hausa': 'ha', 'irish': 'ga', 'kurdish (kurmanji)': 'ku', 
       'kannada': 'kn', 'mongolian': 'mn', 'hebrew': 'iw', 'arabic': 'ar', 'sinhala': 'si', 'swedish': 'sv', 'zulu': 'zu', 
       'samoan': 'sm', 'slovenian': 'sl', 'azerbaijani': 'az', 'sindhi': 'sd', 'korean': 'ko', 'lao': 'lo',
        'myanmar (burmese)': 'my', 'ukrainian': 'uk', 'welsh': 'cy', 'lithuanian': 'lt', 'norwegian': 'no', 
        'maltese': 'mt', 'kazakh': 'kk', 'nepali': 'ne', 'punjabi': 'pa', 'greek': 'el', 'Hebrew': 'he',
         'chinese (simplified)': 'zh-cn', 'frisian': 'fy'}
############################################ ComboBox languages
languages = StringVar()
font_box = Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(1)
font_box.place(x=300,y=0)
#########################################Entry box
varname1 = StringVar()
entry1 = Entry(root,width=30,textvariable=varname1,font=('times',15,'italic bold'))
entry1.place(x=150,y=40)


varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable=varname2,font=('times',15,'italic bold'))
entry2.place(x=150,y=100)

################################################# Labels

label1 = Label(root,text=' Enter Words : ',font=('times',15,'italic bold'),bg='turquoise1')
label1.place(x=5,y=40)

label2 = Label(root,text='Traslated : ',font=('times',15,'italic bold'),bg='turquoise1')
label2.place(x=5,y=100)

label3 = Label(root,text='',font=('times',15,'italic bold'),bg='turquoise1')
label3.place(x=10,y=250)

################################################# buttons

imgbt1 = PhotoImage(file='touch.png')
imgbt2 = PhotoImage(file='logout.png')

imgbt1 = imgbt1.subsample(2,2)
imgbt2 = imgbt2.subsample(2,2)


btn1 = Button(root,text='Click',bd=10,bg='yellow',activebackground='red',height =70,width=100,font=('times',15,'italic bold'),image=imgbt1,compound=RIGHT)
btn1.place(x=70,y=170)

btn2 = Button(root,text='Exit',bd=10,bg='yellow',activebackground='red',height =70,width=100,font=('times',15,'italic bold'),image=imgbt2,compound=RIGHT)
btn2.place(x=280,y=170)

root.mainloop()
#refer to try.py to change key value pair to value key pair.