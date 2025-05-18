# lets be honest, im a dumbass for coding this entire project in one file, but its whatever. even if i did try to reorganize it,
# it'd take years since theres already like 800 lines.

# coding it in one file is gross because of well, organization

# [pre settings you can change if you wanna just mess around]
can_resize_window = True

from PIL import Image, ImageTk
import os
import tkinter as tk
import time
import ctypes
import configparser
import threading

tke = tk.Entry
tkl = tk.Label
tkb = tk.Button
tkc = tk.Checkbutton
tkf = tk.Frame
tks = tk.Scrollbar

bitmapicon = os.path.abspath('icon.ico')
iniconfig = configparser.ConfigParser()
bgcd = '#181818'
bgc = '#1f1f1f'

root = tk.Tk()

root.config(bg=bgc)
root.title('Untitled FNaF World Cheat (UFWC)')
root.iconbitmap(bitmapicon)
root.geometry('1147x650+0+0')
if not can_resize_window:
    root.resizable(False,False)
root.config(cursor=r'@assets/images/cursor.cur')

titlescreenbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\title.png').resize((1147,650)))
placeholderbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\placeholder.png').resize((1147,650)))
choppyswoodsbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\choppyswoods.png').resize((1147,650)))
dustingfieldsbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\dustingfields.png').resize((1147,650)))
lilygearlakebg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\lilygearlake.png').resize((1147,650)))
blacktombyardbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\blacktombyard.png').resize((1147,650)))
pinwheelcircusbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\pinwheelcircus.png').resize((1147,650)))

titlescreenbgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\title.png').resize((420,100)))
placeholderbgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\placeholder.png').resize((420,100)))
choppyswoodsbgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\choppyswoods.png').resize((420,100)))
dustingfieldsbgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\dustingfields.png').resize((420,100)))
lilygearlakebgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\lilygearlake.png').resize((420,100)))
blacktombyardbgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\blacktombyard.png').resize((420,100)))
pinwheelcircusbgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\pinwheelcircus.png').resize((420,100)))
minebgFITB = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\mine.png').resize((420,100)))
scottFITBG = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\scottfitbg.png').resize((420,100)))


halloweenbg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\halloween.png').resize((420,100)))
minebg = ImageTk.PhotoImage(Image.open('assets\\images\\backgrounds\\mine.png').resize((1147,650)))

titlescreenpckfltxt = ImageTk.PhotoImage(Image.open('assets\\images\\pickfiletxt.png').resize((400,35)))
transparentimg = ImageTk.PhotoImage(Image.open('assets\\images\\transparent.png').resize((400,35)))
titlescreenslchtxt = ImageTk.PhotoImage(Image.open('assets\\images\\selectcheattxt.png').resize((400,35)))
titlescreencanvas = tk.Canvas(root, bg=bgcd,width=1147,height=650)

titlescreenloads1 = ImageTk.PhotoImage(Image.open('assets\\images\\save1.png').resize((447,110)))
titlescreenloads2 = ImageTk.PhotoImage(Image.open('assets\\images\\save2.png').resize((447,110)))
titlescreenloads3 = ImageTk.PhotoImage(Image.open('assets\\images\\save3.png').resize((447,110)))

mainmenuadd = ImageTk.PhotoImage(Image.open('assets\\images\\add.png').resize((447,110)))
mainmenurev = ImageTk.PhotoImage(Image.open('assets\\images\\revoke.png').resize((447,110)))

mainmenupreset = ImageTk.PhotoImage(Image.open('assets\\images\\presets.png').resize((447,110)))

continueimg = ImageTk.PhotoImage(Image.open('assets\\images\\continue.png').resize((447,110)))

requiredasterisk = ImageTk.PhotoImage(Image.open('assets\\images\\required.png').resize((76,48)))

posimg = ImageTk.PhotoImage(Image.open('assets\\images\\position.png').resize((447,110)))
charimg = ImageTk.PhotoImage(Image.open('assets\\images\\char.png').resize((447,110)))
miscimg = ImageTk.PhotoImage(Image.open('assets\\images\\misc.png').resize((447,110)))
doneimg = ImageTk.PhotoImage(Image.open('assets\\images\\done.png').resize((167,60)))
idlistimg = ImageTk.PhotoImage(Image.open('assets\\images\\idlist.png').resize((350,83)))
setlevelimg = ImageTk.PhotoImage(Image.open('assets\\images\\setlevel.png').resize((350,83)))

dialogeimg = ImageTk.PhotoImage(Image.open('assets\\images\\dialogebox.png').resize((860,300)))
dialogeimgarrow = ImageTk.PhotoImage(Image.open('assets\\images\\dialogearrow.png'))

animFredbear1 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\1.png').resize((350,420)))
animFredbear2 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\2.png').resize((350,420)))
animFredbear3 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\3.png').resize((350,420)))
animFredbear4 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\4.png').resize((350,420)))
animFredbear5 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\5.png').resize((350,420)))
animFredbear6 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\6.png').resize((350,420)))
animFredbear7 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\7.png').resize((350,420)))
animFredbear8 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\8.png').resize((350,420)))
animFredbear9 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\9.png').resize((350,420)))
animFredbear10 = ImageTk.PhotoImage(Image.open('assets\\animated\\fredbear\\10.png').resize((350,420)))



createTitlescreenBG = titlescreencanvas.create_image(
    573, 325,
   image=titlescreenbg
)

createTitlescreenHeader = titlescreencanvas.create_image(
    570, 80,
   image=titlescreenpckfltxt
)



createTitlescreenB1 = titlescreencanvas.create_text(
    560, 275,
    text='Empty',
    fill = 'white',
    font = ('Itim',16)
)

createTitlescreenB2 = titlescreencanvas.create_text(
    560, 420,
    text='Empty',
    fill = 'white',
    font = ('Itim',16)
)

createTitlescreenB3 = titlescreencanvas.create_text(
    560, 565,
    text='Empty',
    fill = 'white',
    font = ('Itim',16)
)

#---------------------------------------------------------------------------------------------------------------






titlescreencanvas.pack()

# titlescreenbgl = tkl(image=titlescreenbg)
# titlescreenbgl.pack()

headerlabel = tkl(text=root.title(), bg=bgcd, fg='white', font=('Arial', 32))

#headerlabel.pack(fill='x')

os.chdir('C:\\users\\'+os.getlogin()+'\\appdata\\roaming\\MMFApplications\\')

iniconfig.read('info')
if iniconfig.has_option('info','mode1'):
    fnafw1mode = iniconfig.getint('info','mode1')
if iniconfig.has_option('info','diff1'):
    fnafw1diff = iniconfig.getint('info','diff1')
if iniconfig.has_option('info','mode2'):
    fnafw2mode = iniconfig.getint('info','mode2')
if iniconfig.has_option('info','diff2'):
    fnafw2diff = iniconfig.getint('info','diff2')

if iniconfig.has_option('info','mode3'):
    fnafw3mode = iniconfig.getint('info','mode3')
if iniconfig.has_option('info','diff3'):
    fnafw3diff = iniconfig.getint('info','diff3')

if iniconfig.has_option('info','min1'):
    fnafw1min = iniconfig.getint('info','min1')
if iniconfig.has_option('info','min2'):
    fnafw2min = iniconfig.getint('info','min2')
if iniconfig.has_option('info','min3'):
    fnafw3min = iniconfig.getint('info','min3')

if iniconfig.has_option('info','hour1'):
    fnafw1hour = iniconfig.getint('info','hour1')
if iniconfig.has_option('info','hour2'):
    fnafw2hour = iniconfig.getint('info','hour2')
if iniconfig.has_option('info','hour3'):
    fnafw3hour = iniconfig.getint('info','hour3')

if os.path.exists('fnafw1'):
    if fnafw1mode == 1:
        fnafw1model = 'Adventure'
    elif fnafw1mode == 2:
        fnafw1model = 'Fixed Party'

    if fnafw1diff == 1:
        fnafw1diffl = 'Normal'
    elif fnafw1diff == 2:
        fnafw1diffl = 'Hard mode'

if os.path.exists('fnafw2'):
    if fnafw2mode == 1:
        fnafw2model = 'Adventure'
    elif fnafw2mode == 2:
        fnafw2model = 'Fixed Party'

    if fnafw2diff == 1:
        fnafw2diffl = 'Normal'
    elif fnafw2diff == 2:
        fnafw2diffl = 'Hard mode'

if os.path.exists('fnafw3'):
    if fnafw3mode == 1:
        fnafw3model = 'Adventure'
    elif fnafw3mode == 2:
        fnafw3model = 'Fixed Party'

    if fnafw3diff == 1:
        fnafw3diffl = 'Normal'
    elif fnafw3diff == 2:
        fnafw3diffl = 'Hard Mode'



def showinfo(msg:str,title:str):
    ctypes.windll.user32.MessageBoxW(0, msg, title, 0x40)


def notice():
    root.withdraw()
    global noticeroot
    global noticetkca
    global FredbearAnim
    noticeroot = tk.Toplevel()
    
    noticeroot.title('Untitled FNaF World Cheat (UFWC)')
    noticeroot.geometry('1147x650')
    noticeroot.iconbitmap(bitmapicon)
    noticeroot.config(cursor=r'@assets/images/cursor.cur')

    noticetkca = tk.Canvas(noticeroot, bg=bgcd,width=1147,height=650)
    noticebg = noticetkca.create_image(573, 325, image=titlescreenbg)
    FredbearAnim = noticetkca.create_image(140, 450, image=animFredbear1)
    
    def destroynotice():
        noticeroot.destroy()


    DialogeBoxArrow = noticetkca.create_image(273, 300, image=dialogeimgarrow)
    DialogeBox = noticetkca.create_image(573, 150, image=dialogeimg)
    DialogeBoxDone = tkb(noticeroot,bg='black',image=doneimg,text='Done',relief='flat',command=destroynotice)
    DialogeBoxDone.place(x=800,y=214)
    DialogeBoxText = noticetkca.create_text(420, 148, 
        text='Dear User,\n\nJust a heads up that this cheat works by writing to the config. This means you cannot be playing the game while applying cheats. By \'Not playing\' counts to:\n\nBeing in the party menu (fastest),\nBeing in the game\'s start screen,\nBeing in a shop menu,\nPlaying DeeDee\'s fishing game\n..etc, just any menu.\n\nYour changes may be overwritten by the game if you apply any cheat changes while the game is actively playing.',
        fill='white',
        font=('Itim',12),
        width=500
    )



    noticetkca.pack()
    root.wait_window(noticeroot)
    root.deiconify()



def animFredbearLoop(frame=1):
    if noticeroot.winfo_exists():
        global FredbearAnim
        anim_frames = [
            animFredbear1,
            animFredbear2,
            animFredbear3,
            animFredbear4,
            animFredbear5,
            animFredbear6,
            animFredbear7,
            animFredbear8,
            animFredbear9,
            animFredbear10
        ]

        if noticeroot.focus_get():
            noticetkca.itemconfig(FredbearAnim,image=anim_frames[frame%len(anim_frames)])
        noticeroot.after(30,animFredbearLoop,(frame + 1)%len(anim_frames))




def settings():
    if not os.path.exists('ufwc'):
        os.mkdir('ufwc')
        notice()
        threading.Thread(target=animFredbearLoop).start()
    else:
        pass

settings()




applyslot = None

def loadSlot1():
    global applyslot
    applyslot = 'fnafw1'
    threading.Thread(target=FindCoordsIni,args=(applyslot,),daemon=True).start()
    LaunchMainApp()

def loadSlot2():
    global applyslot
    applyslot = 'fnafw2'
    threading.Thread(target=FindCoordsIni,args=(applyslot,),daemon=True).start()
    LaunchMainApp()

def loadSlot3():
    global applyslot
    applyslot = 'fnafw3'
    threading.Thread(target=FindCoordsIni,args=(applyslot,),daemon=True).start()
    LaunchMainApp()

loadslot1 = tkb(text='Slot 1',bg='green',fg='white',command=loadSlot1,image=titlescreenloads1,relief='flat')
loadslot2 = tkb(text='Slot 2',bg='green',fg='white',command=loadSlot2,image=titlescreenloads2,relief='flat')
loadslot3 = tkb(text='Slot 3',bg='green',fg='white',command=loadSlot3,image=titlescreenloads3,relief='flat')

if os.path.exists('fnafw1'):
    titlescreencanvas.itemconfig(createTitlescreenB1, text=f'{fnafw1model}: {fnafw1diffl}: {fnafw1hour}:{fnafw1min}')
else:
    loadslot1.config(state='disabled')

if os.path.exists('fnafw2'):
    titlescreencanvas.itemconfig(createTitlescreenB2, text=f'{fnafw2model}: {fnafw2diffl}: {fnafw2hour}:{fnafw2min}')
else:
    loadslot2.config(state='disabled')

if os.path.exists('fnafw3'):
    titlescreencanvas.itemconfig(createTitlescreenB3, text=f'{fnafw3model}: {fnafw3diffl}: {fnafw3hour}:{fnafw3min}')
else:
    loadslot3.config(state='disabled')

loadslot1.place(x=350,y=157,width=437,height=109)
loadslot2.place(x=350,y=302,width=437,height=109)
loadslot3.place(x=350,y=447,width=437,height=109)


def LaunchMainApp():
    loadMainApp(applyslot)
    loadMainAppW()


def loadMainApp(slot):
    loadslot1.place_forget()
    loadslot2.place_forget()
    loadslot3.place_forget()
    titlescreencanvas.pack_forget()
    mainmenubgFHtkca.pack()


def loadMainAppW():
    loadPosition.place(x=350,y=157,width=437,height=109)
    loadCharacters.place(x=350,y=302,width=437,height=109)
    loadMisc.place(x=350,y=447,width=437,height=109)


def FindCoordsIni(slot):
    global realcoords
    global hasloadedposgui
    while True:
        iniconfig.read(slot)
        coordx = iniconfig.getint('fnafw','x')
        coordy = iniconfig.getint('fnafw','y')
        realcoords = f'{coordx} {coordy}'
        if hasloadedposgui:
          root.after(0,update_pos)
        root.after(0,findArea)
        time.sleep(0.6)


def update_pos():
    global realcoords
    mainmenubgFHtkca.itemconfig(yourcurrentpos,text='You\'re at '+realcoords)

# [places and their location]
pFazbearHills = 0
pChoppysWoods = 2
pDustingFields = 5
pLilyGearLake = 8
pBlacktombYard = 14
pMysteriousMine = 11
pPinwheelCircus = 20
pDeepMetalMine = 17
pHalloweenBackstage = 'HalloweenBackstage' # it doesnt have an area code lol
pScott = 'Scott' # ALSO doesnt have an area code 

lFazbearHills = 'Fazbear Hills'
lChoppysWoods = 'Choppys Woods'
lDustingFields = 'Dusting Fields'
lLilyGearLake = 'Lilygear Lake'
lBlacktombYard = 'Blacktomb Yard'
lMysteriousMine = 'Mysterious Mine'
lPinwheelCircus = 'Pinwheel Circus'
lDeepMetalMine = 'Deep-Metal Mine'
lHalloweenBackstage = 'Halloween Backstage'
lScott = 'Scott'

locxFazbearHills = 1829
locyFazbearHills = 1024
locxChoppysWoods = 1673
locyChoppysWoods = 1628
locxDustingFields = 918
locyDustingFields = 1726
locxLilyGearLake = 2787
locyLilyGearLake = 833
locxBlacktombYard = 3275
locyBlacktombYard = 1922
locxPinwheelCircus = 2544
locyPinwheelCircus = 3685
locxMysteriousMine = 2193
locyMysteriousMine = 1570
locxHalloweenBackstage = 1173
locyHalloweenBackstage = 934
locxScott = 1324
locyScott = 486


characterlist = '''real quick side note that character versions are abbreviated example like NPuppet, TBonnie, and PBB (PBB is Phantom Balloon Boy, TBonnie Toy Bonnie, NPuppet NightmarePuppet.. etc)
FreddyFazbear = '1'
Bonnie = '2'
Chica = '3'
Foxy = '4'
TBonnie = '5'
TChica = '6'
TFreddy = '7'
Mangle = '8'
BB = '9'
JJ = '10'
PFreddy = '11'
PChica = '12'
PBB = '13'
PFoxy = '14'
PMangle = '15'
WBonnie = '16'
WChica = '17'
WFreddy = '18'
WFoxy = '19'
WSFreddy = '20'
Puppet = '21'
PPuppet = '22'
GFreddy = '23'
PaperPals = '24'
NFreddy = '25'
NBonnie = '26'
NChica = '27'
NFoxy = '28'
Endo01 = '29'
Endo02 = '30'
Plushtrap = '31'
EndoPlush = '32'
SpringTrap = '33'
RXQ = '34'
CryingChild = '35'
FFoxy = '36'
NFredbear = '37'
Nightmare = '38'
Fredbear = '39'
Springbonnie = '40'
JBonnie = '41'
JChica = '42'
Animdude = '43'
Chipper = '44'
NBB = '45'
NPuppet = '46'
Coffee = '47'
PurpleGuy = '48'
'''

if not os.path.exists('ufwc\\charlist.txt'):
    with open('ufwc\\charlist.txt', 'w') as charlisttxt:
        charlisttxt.write(characterlist)
else:
    with open('ufwc\\charlist.txt', 'r') as charlisttxt:
        characterlisttext = charlisttxt.read()
        if not characterlisttext == characterlist:
            with open('ufwc\\charlist.txt', 'w') as charlisttxt:
                charlisttxt.write(characterlist)


def modifycoordscpre(slot,xc,yc):

    xcp = f'{xc}'
    ycp = f'{yc}'

    iniconfig.set('fnafw','x',xcp)
    iniconfig.set('fnafw','y',ycp)

    with open(slot,'w') as configfile:
        iniconfig.write(configfile)

    tpFazbearHills.place_forget()
    tpChoppysWoods.place_forget()
    tpDustingFields.place_forget()
    tpLilyGearLake.place_forget()
    tpBlacktombYard.place_forget()
    tpPinwheelCircus.place_forget()
    tpMysteriousMine.place_forget()
    tpHalloweenBackstage.place_forget()
    tpScott.place_forget()

def tpcustompreenter(area):
    if area == pFazbearHills:
        modifycoordscpre(xc=locxFazbearHills,yc=locyFazbearHills,slot=applyslot)
    elif area == pChoppysWoods:
        modifycoordscpre(xc=locxChoppysWoods,yc=locyChoppysWoods,slot=applyslot)
    elif area == pDustingFields:
        modifycoordscpre(xc=locxDustingFields,yc=locyDustingFields,slot=applyslot)
    elif area == pLilyGearLake:
        modifycoordscpre(xc=locxLilyGearLake,yc=locyLilyGearLake,slot=applyslot)
    elif area == pBlacktombYard:
        modifycoordscpre(xc=locxBlacktombYard,yc=locyBlacktombYard,slot=applyslot)
    elif area == pPinwheelCircus:
        modifycoordscpre(xc=locxPinwheelCircus,yc=locyPinwheelCircus,slot=applyslot)
    elif area == pMysteriousMine:
        modifycoordscpre(xc=locxMysteriousMine,yc=locyMysteriousMine,slot=applyslot)
    elif area == pHalloweenBackstage:
        modifycoordscpre(xc=locxHalloweenBackstage,yc=locyHalloweenBackstage,slot=applyslot)
    elif area == pScott:
        modifycoordscpre(xc=locxScott,yc=locyScott,slot=applyslot)

    tppresetsb.place(x=350,y=447,width=437,height=109)
    modifycoordsb.place(x=350,y=324,width=437,height=109)

    xmodifycoordse.place(x=350,y=184,width=437,height=60)
    ymodifycoordse.place(x=350,y=247,width=437,height=60)


charlabel = tkl(text='Manage Characters',bg=bgc,fg='white',pady=10,font=('Arial'))
misclabel = tkl(text='Misc',bg=bgc,fg='white',pady=10,font=('Arial'))

mainmenubgFHtkca = tk.Canvas(root, bg=bgcd,width=1147,height=650)




loadPosition = tkb(text='Position',bg='green',fg='white',command=lambda: loadPosGui(applyslot),image=posimg,relief='flat')
loadCharacters = tkb(text='Characters',bg='green',fg='white',command=lambda: loadCharGui(applyslot),image=charimg,relief='flat')
loadMisc = tkb(text='Miscellaneous',bg='green',fg='white',command=lambda: loadMiscGui(applyslot),image=miscimg,relief='flat')

unibuttoncolor = 'green'

makemainmenubg = mainmenubgFHtkca.create_image(573, 325,image=titlescreenbg)

def syncbuttoncolors():
    loadMisc.config(bg=unibuttoncolor)
    loadCharacters.config(bg=unibuttoncolor)
    loadPosition.config(bg=unibuttoncolor)
    loadMisc.config(bg=unibuttoncolor)
    modcharida.config(bg=unibuttoncolor)
    modcharidr.config(bg=unibuttoncolor)
    showcharid.config(bg=unibuttoncolor)
    modifycoordsb.config(bg=unibuttoncolor)
    tppresetsb.config(bg=unibuttoncolor)



def findArea():
    whereistheareaarea = iniconfig.getint('fnafw','area')
    global yourcurrentarea
    global unibuttoncolor
    if whereistheareaarea == pFazbearHills:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lFazbearHills)
        
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=titlescreenbg)
        unibuttoncolor = 'green'

    elif whereistheareaarea == pChoppysWoods:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lChoppysWoods)

        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=choppyswoodsbg)
        unibuttoncolor = '#606d05'

    elif whereistheareaarea == pDustingFields:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lDustingFields)

        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=dustingfieldsbg)
        unibuttoncolor = '#6aaee7'
    elif whereistheareaarea == pLilyGearLake:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lLilyGearLake)

        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=lilygearlakebg)
        unibuttoncolor = '#223ff8'

    elif whereistheareaarea == pBlacktombYard:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lBlacktombYard)
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=blacktombyardbg)
        unibuttoncolor = '#192920'

    elif whereistheareaarea == pPinwheelCircus:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lPinwheelCircus)
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=pinwheelcircusbg)
        unibuttoncolor = '#54ab00'

    elif whereistheareaarea == pMysteriousMine:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lMysteriousMine)
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=minebg)
        unibuttoncolor = '#331a01'
        #794d22 - fixme, preserved to add the secondbuttoncolor

    elif whereistheareaarea == pHalloweenBackstage:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lHalloweenBackstage)
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=placeholderbg)
        unibuttoncolor = 'white'

    elif whereistheareaarea == pDeepMetalMine:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text=lDeepMetalMine)
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=minebg)
        unibuttoncolor = '#331a01'
        #794d22 - fixme, preserved to add the secondbuttoncolor

    else:
        if hasloadedposgui:
            mainmenubgFHtkca.itemconfig(yourcurrentarea,text='Can\'t find Area.')
        updbg = mainmenubgFHtkca.itemconfig(makemainmenubg, image=placeholderbg)
        unibuttoncolor = 'black'
    syncbuttoncolors()


def loadpresetmenu():
    tppresetsb.place_forget()
    modifycoordsb.place_forget()
    ymodifycoordse.place_forget()
    xmodifycoordse.place_forget()

    tpFazbearHills.place(x=150,y=184,width=437,height=65)
    tpChoppysWoods.place(x=150,y=252,width=437,height=65)
    tpDustingFields.place(x=150,y=320,width=437,height=65)
    tpLilyGearLake.place(x=150,y=388,width=437,height=65)
    tpBlacktombYard.place(x=150,y=456,width=437,height=65)
    tpPinwheelCircus.place(x=150,y=524,width=437,height=65)
    tpMysteriousMine.place(x=600,y=184,width=437,height=65)
    tpHalloweenBackstage.place(x=600,y=252,width=437,height=65)
    tpScott.place(x=600,y=320,width=437,height=65)

def getallcharacters():
    for i in range(1, 49):
        addCharacterlist(slot=applyslot,id=i,aor='a')

def startnotepadtoshowthecharactersid(): #comically large name
    if os.path.exists('ufwc\\charlist.txt'):
        os.startfile('ufwc\\charlist.txt')
    else:
        showinfo('Dear user, it seems that you may be missing your character list file. Simply restarting the app will regenerate it. Sorry for any inconvience!', 'Oh noes!')


ymodifycoordse = tke(width=10,bg=bgcd,fg='white',font=('Arial',16))
xmodifycoordse = tke(width=10,bg=bgcd,fg='white',font=('Arial',16))

Charshowinfob = tkb(text='ⓘ',width=3,bg=bgcd,fg='white',command=lambda: showinfo('Each character is represented using a unique identifier, as shown on the side of the screen.\nType the Numeric ID into the box and submit your choice.','Info'),font=('Arial',16),relief='flat')
showcharid = tkb(text='View Character ID\'s',bg='green',fg='white',command=startnotepadtoshowthecharactersid,image=idlistimg,relief='flat')


setlevelchare = tke(width=20,bg=bgcd,fg='white',font=('Arial',26))
setlevelb = tkb(text='Set Level',bg='green',fg='white',command=lambda: managelevels(slot=applyslot,levels=setlevelchare.get(),id=entercharid),image=setlevelimg,relief='flat')

getallcharactersb = tkb(text='Get All Characters',width=20,bg=bgcd,fg='white',font=('Arial',16),pady=10,command= lambda: getallcharacters())


settokense = tke(width=20,bg=bgcd,fg='white',font=('Arial',26))
settokensb = tkb(text='Set Tokens',width=20,bg=bgcd,fg='white',font=('Arial',16),pady=10,command= lambda: managetokens(slot=applyslot,tokens=settokense.get()))
skipfishclb = tkb(text='Skip DeeDee Fish Cooldown',width=25,bg=bgcd,fg='white',font=('Arial',16),pady=10,command= lambda: skipfishcooldown(slot=applyslot))

entercharid = tke(width=20,bg=bgcd,fg='white',font=('Arial',26))

modcharida = tkb(text='ADD',bg='green',fg='white',command=lambda: addCharacterlist(slot=applyslot,id=entercharid.get(),aor='a'),image=mainmenuadd,relief='flat')
modcharidr = tkb(text='REVOKE',bg='green',fg='white',command=lambda: addCharacterlist(slot=applyslot,id=entercharid.get(),aor='r'),image=mainmenurev,relief='flat')

tppresetsb = tkb(text='Presets',bg='green',fg='white',command=loadpresetmenu,image=mainmenupreset,relief='flat')
modifycoordsb = tkb(text='Teleport',bg='green',fg='white',command=lambda: modifycoords(applyslot),image=continueimg,relief='flat')

entercharid.insert(0,'ID')
setlevelchare.insert(0,'LEVELS')



tpFazbearHills = tkb(text=lFazbearHills,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pFazbearHills),image=titlescreenbgFITB)
tpChoppysWoods = tkb(text=lChoppysWoods,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pChoppysWoods),image=choppyswoodsbgFITB)
tpDustingFields = tkb(text=lDustingFields,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pDustingFields),image=dustingfieldsbgFITB)
tpLilyGearLake = tkb(text=lLilyGearLake,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pLilyGearLake),image=lilygearlakebgFITB)
tpBlacktombYard = tkb(text=lBlacktombYard,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pBlacktombYard),image=blacktombyardbgFITB)
tpPinwheelCircus = tkb(text=lPinwheelCircus,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pPinwheelCircus),image=pinwheelcircusbgFITB)
tpMysteriousMine = tkb(text=lMysteriousMine,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pMysteriousMine),image=minebgFITB)
tpHalloweenBackstage = tkb(text=lHalloweenBackstage,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pHalloweenBackstage),image=halloweenbg)
tpScott = tkb(text=lScott,bg=bgcd,pady=10,fg='white',height=2,font=('Arial',9),command=lambda: tpcustompreenter(pScott),image=scottFITBG)



# posmenuLtpFazbearHills = tkl(text=lFazbearHills,font=('Itim',16))
# posmenuLtpChoppysWoods = tkl(text=lChoppysWoods,font=('Itim',16))
# posmenuLtpDustingFields = tkl(text=lDustingFields,font=('Itim',16))
# posmenuLtpLilyGearLake = tkl(text=lLilyGearLake,font=('Itim',16))
# posmenuLtpBlacktombYard = tkl(text=lBlacktombYard,font=('Itim',16))
# posmenuLtpPinwheelCircus = tkl(text=lPinwheelCircus,font=('Itim',16))
# posmenuLtpMysteriousMine = tkl(text=lMysteriousMine,font=('Itim',16))
# posmenuLtpHalloweenBackstage = tkl(text=lHalloweenBackstage,font=('Itim',16))

# so i was going to add them for a label on the presets menu but id have to make so much canvas gazebos i just didnt
# you can if you want lmao



def addCharacterlist(slot,id:str,aor:str):

    checkifiseqid = id.lower()

    if id == '' or not checkifiseqid.isdigit() or not (1 <= int(id) <= 48):
        showinfo('ID Field cannot be blank and must be numeric. Numeric value ranges from 1-48','UFWC')
    else:
        if aor == 'a':
            charid = f'{id}have'
            iniconfig.read(slot)
            iniconfig.set('fnafw',charid,'1')
            with open(slot,'w') as configfile:
                iniconfig.write(configfile)
        elif aor == 'r':
            iniconfig.read(slot)
            charid = f'{id}have'
            iniconfig.set('fnafw',charid,'0')
            with open(slot,'w') as configfile:
                iniconfig.write(configfile)
                
def managetokens(slot,tokens:str):
    iniconfig.read(slot)
    iniconfig.set('fnafw','tokens',tokens)
    with open(slot,'w') as configfile:
        iniconfig.write(configfile)

def managelevels(slot,levels:str,id:str):
    iniconfig.read(slot)
    iniconfig.set('fnafw',f'{id}lv',levels)
    with open(slot, 'w') as configfile:
        iniconfig.write(configfile)

def skipfishcooldown(slot):
    iniconfig.read(slot)
    iniconfig.set('fnafw','fish','0')
    with open(slot,'w') as configfile:
        iniconfig.write(configfile)


exitmenub = tkb(text='Done',bg=bgcd,fg='white',font=('Arial',16),image=doneimg,command= lambda: exitmenus())

hasloadedposgui = False
def exitmenus():
    global yourcurrentpos
    global hasloadedposgui
    global charidrequired

    try:
        mainmenubgFHtkca.delete(yourcurrentpos) # prevent python from going full fucking PANIC because except pass makes python forget it ever happened
        mainmenubgFHtkca.delete(yourcurrentarea)
    except NameError:
        pass

    hasloadedposgui = False
    mainmenubgFHtkca.itemconfig(Mainmenuheader, image=titlescreenslchtxt)


    try:
         mainmenubgFHtkca.delete(charidrequired) # another "shut the fuck up" to python
    except NameError:
        pass

    try:
        mainmenubgFHtkca.delete(nothingtoseeheretxt) # once again, so python will shut its trap
    except NameError:
        pass
    

    entercharid.place_forget()
    modcharida.place_forget()
    modcharidr.place_forget()
    setlevelchare.place_forget()
    setlevelb.place_forget()    
    Charshowinfob.place_forget()
    showcharid.place_forget()
    # getallcharactersb.place_forget() - fixme, add 'get all' button soon

    misclabel.pack_forget()
    settokense.pack_forget()
    settokensb.pack_forget()
    skipfishclb.pack_forget()

    tpFazbearHills.place_forget()
    tpChoppysWoods.place_forget()
    tpDustingFields.place_forget()
    tpLilyGearLake.place_forget()
    tpBlacktombYard.place_forget()
    tpPinwheelCircus.place_forget()
    tpMysteriousMine.place_forget()
    tpHalloweenBackstage.place_forget()
    tpScott.place_forget()

    tppresetsb.place_forget()
    modifycoordsb.place_forget()
    xmodifycoordse.place_forget()
    ymodifycoordse.place_forget()

    exitmenub.place_forget()

    LaunchMainApp()


Mainmenuheader = mainmenubgFHtkca.create_image(570, 80,image=titlescreenslchtxt)

def loadCharGui(slot):
    global charidrequired
    mainmenubgFHtkca.itemconfig(Mainmenuheader, image=transparentimg)

    loadMisc.place_forget()
    loadPosition.place_forget()
    loadCharacters.place_forget()

    showcharid.place(x=10,y=552)

    exitmenub.place(x=960,y=570)

    entercharid.place(x=350,y=84,width=437,height=60)
    setlevelchare.place(x=350,y=168,width=437,height=60)
    modcharida.place(x=342,y=242)
    modcharidr.place(x=342,y=362)

    charidrequired = mainmenubgFHtkca.create_image(
        301, 115,
        image=requiredasterisk
    )



    # modcharidr.pack()
    setlevelb.place(x=386,y=484)
    # Charshowinfob.place(x=750,y=550)
    # getallcharactersb.place(x=510,y=70)



def loadMiscGui(slot):
    global nothingtoseeheretxt
    mainmenubgFHtkca.itemconfig(Mainmenuheader, image=transparentimg)
    loadPosition.place_forget()
    loadCharacters.place_forget()
    loadMisc.place_forget()

    nothingtoseeheretxt = mainmenubgFHtkca.create_text(
        573, 325,
        text='Updated Misc GUI coming in later update.\n\nThere\'s nothing to see here yet :(',
        fill='white',
        font=('Itim',26)
    )

    exitmenub.place(x=960,y=570)

    # misclabel.pack()
    # settokense.pack(pady=5)
    # settokensb.pack(pady=5)
    # skipfishclb.pack(pady=5)


xmodifycoordse.insert(0,string='X')
ymodifycoordse.insert(0,string='Y')

def loadPosGui(slot):
    global yourcurrentarea
    global yourcurrentpos
    global hasloadedposgui
    if not hasloadedposgui:
        hasloadedposgui = True

    yourcurrentpos = mainmenubgFHtkca.create_text(570, 80, text='Finding POS',font=('itim',46),fill='white')
    yourcurrentarea = mainmenubgFHtkca.create_text(570, 140, text='Finding Area',font=('itim',34),fill='white')
    
    mainmenubgFHtkca.itemconfig(Mainmenuheader, image=transparentimg)

    loadMisc.place_forget()
    loadPosition.place_forget()
    loadCharacters.place_forget()


    tppresetsb.place(x=350,y=447,width=437,height=109)
    modifycoordsb.place(x=350,y=324,width=437,height=109)

    xmodifycoordse.place(x=350,y=184,width=437,height=60)
    ymodifycoordse.place(x=350,y=247,width=437,height=60)

    exitmenub.place(x=960,y=570)



def modifycoords(slot):
    iniconfig.set('fnafw','x',xmodifycoordse.get())
    iniconfig.set('fnafw','y',ymodifycoordse.get())

    with open(slot,'w') as configfile:
        iniconfig.write(configfile)


root.mainloop()
