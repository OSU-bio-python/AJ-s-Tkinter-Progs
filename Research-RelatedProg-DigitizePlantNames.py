#Requires the text files famgen.txt and floraS_table.txt

from Tkinter import *
from tkFileDialog   import askopenfilename, asksaveasfile
import os
from decimal import *

getcontext().prec = 2

allfamily = []
allgenus = []
famgen_dict = {}

floraS_data = file("floraS_table.txt", "r").readlines()

with open("famgen.txt", "r") as famgen_data:
    for line in famgen_data:
        line = line.split()
        if line[0] not in allgenus:
            allgenus.append(line[0])
        if line[1] not in allfamily:
            allfamily.append(line[1])
        famgen_dict[line[0]] = line[1]        
famgen_data.close()

def OpenFile():
    varone.set(0)
    vartwo.set(0)
    varthree.set(0)
    varinfrasp.set(0)

    gen = []
    fam = []
    sp = []
    
    save_gen = []
    save_fam = []
    save_sp = []
            
    FindIT_name = askopenfilename()
    data = file(FindIT_name, "r").readlines()
    filename.set(FindIT_name)
    
    for line in data:
        line = line.strip("\n")
        correct_name = line.split("\t")
        
        if len(correct_name) == 2:

            correct_name = correct_name[1]
            correct_name = correct_name.split()

            if len(correct_name) == 1:
                if correct_name[0] in allfamily:
                    fam.append(1)
                elif correct_name[0] in allgenus:
                    if correct_name not in save_gen:
                        save_gen.append(correct_name[0])
                        gen.append(1)
                        
            elif len(correct_name) == 2:
                if correct_name[0] not in save_gen:                 
                    save_gen.append(correct_name[0])
                    gen.append(1)
                if " ".join(correct_name) not in save_sp:
                    save_sp.append(" ".join(correct_name))
                    sp.append(1)
                        
    num_fam = len(fam)
    num_gen = len(gen)
    num_sp = len(sp)

    varone.set(num_fam)
    vartwo.set(num_gen)
    varthree.set(num_sp)

def stop():
    root.destroy()
    root.quit()

def ss():
    by_spec = fileinf_ent.get()
    data = file(by_spec, "r").readlines()
    infile = asksaveasfile(mode="w", defaultextension=".csv", title="Save List of Taxa Sorted Alphabetically By Species Name")
    outfilename.set(infile.name)
    infile.write("Species & Lower Ranks,Species,Family,Genus\n")
    for line in data:
        line = line.strip("\n")
        correct_name = line.split("\t")
        
        if len(correct_name) == 2:

            correct_name = correct_name[1]
            correct_name = correct_name.split()
            
            if len(correct_name) == 2:
                colzero = ""
                colone = " ".join(correct_name)
                colthree = correct_name[0]
                coltwo = famgen_dict.get(correct_name[0], "Unavailable")
                infile.write(colzero + "," + colone + "," + coltwo + "," + colthree + "\n")
    infile.flush()
    infile.close()
                    
    
def get_expected():
    varfour.set(0)
    varfive.set(0)
    varsix.set(0)
    varseven.set(0)

    for line in floraS_data:
        aline = line.split("\t")
        if str(aline[0]) == str(accnum_ent.get()):
            varfour.set(aline[2])
            varfive.set(aline[3])
            varsix.set(aline[5])
            varseven.set(aline[4])
            
def Load():

    gen = []
    fam = []
    sp = []
    OTUs = []
    
    save_gen = []
    save_fam = []
    save_sp = []

    findfile = askopenfilename(title="Navigate To Your Working Output File")
    data = file(findfile, "r").readlines()
    outfilename.set(findfile)
    
    for i, line in enumerate(data):
        if i == 0:
            line = line.strip("\n")
            line = line.split(",")
            infrasp_loc = line.index("Species & Lower Ranks")
            spec_loc = line.index("Species")
            gen_loc = line.index("Genus")
            fam_loc = line.index("Family")

    for i, line in enumerate(data):
        if i > 0:
            
            line = line.strip("\n")
            correct_name = line.split(",")
            
            if correct_name[spec_loc] != "" and correct_name[spec_loc] not in save_sp:
                save_sp.append(correct_name[spec_loc])
                sp.append(1)
            if correct_name[gen_loc] != "" and correct_name[gen_loc] not in save_gen:
                save_gen.append(correct_name[gen_loc])
                gen.append(1)
            if correct_name[fam_loc] != "" and correct_name[fam_loc] != "Unavailable" and correct_name[fam_loc] not in save_fam:
                save_fam.append(correct_name[fam_loc])
                fam.append(1)
            if correct_name[infrasp_loc] != "":
                OTUs.append(1)
       
    num_fam = len(fam)
    num_gen = len(gen)
    num_sp = len(sp)
    num_OTUs = len(OTUs)

    varone.set(num_fam)
    vartwo.set(num_gen)
    varthree.set(num_sp)
    varinfrasp.set(num_OTUs)

    
def refresh():

    findfile = askopenfilename(title="Navigate To Your Working Output File")
    data = file(findfile, "r").readlines()
    outfilename.set(findfile)

    gen = []
    fam = []
    sp = []
    OTUs = []
    
    save_gen = []
    save_fam = []
    save_sp = []

    
    for i, line in enumerate(data):
        if i == 0:
            line = line.strip("\n")
            line = line.split(",")
            infrasp_loc = line.index("Species & Lower Ranks")
            spec_loc = line.index("Species")
            gen_loc = line.index("Genus")
            fam_loc = line.index("Family")

    for i, line in enumerate(data):
        if i > 0:
            
            line = line.strip("\n")
            correct_name = line.split(",")
            
            if correct_name[spec_loc] != "" and correct_name[spec_loc] not in save_sp:
                save_sp.append(correct_name[spec_loc])
                sp.append(1)
            if correct_name[gen_loc] != "" and correct_name[gen_loc] not in save_gen:
                save_gen.append(correct_name[gen_loc])
                gen.append(1)
            if correct_name[fam_loc] != "" and correct_name[fam_loc] != "Unavailable" and correct_name[fam_loc] not in save_fam:
                save_fam.append(correct_name[fam_loc])
                fam.append(1)
            if correct_name[infrasp_loc] != "":
                OTUs.append(1)
       
    num_fam = len(fam)
    num_gen = len(gen)
    num_sp = len(sp)
    num_OTUs = len(OTUs)

    varone.set(num_fam)
    vartwo.set(num_gen)
    varthree.set(num_sp)
    varinfrasp.set(num_OTUs)   


def calc():
    vareight.set("na")
    varnine.set("na")
    varten.set("na")
    vareleven.set("na")

    if int(entryfour.get()) != 0:
        perc_fam = int(100 * (Decimal(int(entryone.get()))/Decimal(int(entryfour.get()))))
        vareight.set(str(perc_fam) + "%")
    if int(entryfive.get()) != 0:
        perc_gen = int(100 * (Decimal(int(entrytwo.get()))/Decimal(int(entryfive.get()))))
        varnine.set(str(perc_gen) + "%")
    if int(entrythree.get()) != 0:
        perc_sp = int(100 * (Decimal(int(entrythree.get()))/Decimal(int(entrysix.get()))))
        varten.set(str(perc_sp) + "%")
    if int(entryseven.get()) != 0:
        perc_infrasp = int(100 * (Decimal(int(entryeight.get()))/Decimal(int(entryseven.get()))))
        vareleven.set(str(perc_infrasp) + "%")

def stat_out():

    statfile = asksaveasfile(mode="w", defaultextension=".csv", title="Save Stats for this Flora")
    statfile.write(accnum_ent.get() + "\n")
    statfile.write("\n")
    statfile.write(",Family,Genus,Species, Species & Lower Ranks\n")
    statfile.write("Reported Values in FloraS Database:," + str(entryfour.get()) + "," + str(entryfive.get()) + "," + str(entrysix.get()) + "," + str(entryseven.get()) + "\n")
    statfile.write("Curated List:," + str(entryone.get()) + "," + str(entrytwo.get()) + "," + str(entrythree.get()) + "," + str(entryeight.get()) + "\n")
    statfile.write("\n")
    statfile.write("Unnamed Hybrids removed: " + hy_count.get() + "\n")
    statfile.write("Unnamed species (sp.) removed: " + unnamed_sp_count.get() + "\n")
    statfile.flush()
    statfile.close()

    varone.set(0)
    vartwo.set(0)
    varthree.set(0)
    varinfrasp.set(0)
    varfour.set(0)
    varfive.set(0)
    varsix.set(0)
    varseven.set(0)
    
    vareight.set("na")
    varnine.set("na")
    varten.set("na")
    vareleven.set("na")
    
    default_acc_num.set(0)
    
    filename.set('None')
    outfilename.set('None')

    rm_hybrids_num.set(0)
    rm_sp_num.set(0)
    
root = Tk()
root.minsize(600,400)
root.geometry("600x400")
root.wm_title("Curate Digitized Names")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Get FindIt Input", command=OpenFile)
filemenu.add_command(label="Load Working Output File", command=Load)
filemenu.add_command(label="Save Stats and  Clear Data", command=stat_out)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=stop)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Generate .csv file of taxa", command=ss)
menubar.add_cascade(label="Process", menu=editmenu)

varone = StringVar()
vartwo = StringVar()
varthree = StringVar()
varfour = StringVar()
varfive = StringVar()
varsix = StringVar()
varseven = StringVar()
varinfrasp = StringVar()

varone.set(0)
vartwo.set(0)
varthree.set(0)
varinfrasp.set(0)
varfour.set(0)
varfive.set(0)
varsix.set(0)
varseven.set(0)

vareight = StringVar()
varnine = StringVar()
varten = StringVar()
vareleven = StringVar()

vareight.set("na")
varnine.set("na")
varten.set("na")
vareleven.set("na")

default_acc_num = StringVar()
default_acc_num.set(0)

filename = StringVar()
filename.set('None')

outfilename = StringVar()
outfilename.set('None')

rm_hybrids_num = StringVar()
rm_hybrids_num.set(0)

rm_sp_num = StringVar()
rm_sp_num.set(0)

framea = Frame(root)
accnum_lab = Label(framea, text="FloraS Accession Number:")
accnum_lab.grid(row=0, column=0)
accnum_ent = Entry(framea, bg=root.cget('bg'),textvariable=default_acc_num)
accnum_ent.grid(row=0, column=2, columnspan=2)
get_expected_button = Button(framea, text = "Get Reported Values", command = get_expected)
get_expected_button.grid(row=0, column=4, padx = 1)
framea.grid(row=0, column=0, columnspan=5, rowspan=1, sticky=N+E+S+W, pady=2)
                   
frameb = Frame(root, background="WHITE")
headerone = Label(frameb, text="Families", background="WHITE")
headerone.grid(row=2, column=2)
headertwo = Label(frameb, text="Genera", background="WHITE")
headertwo.grid(row=2, column=3)
headerthree = Label(frameb, text="Species", background="WHITE")
headerthree.grid(row=2, column=4)
headerfour = Label(frameb, text="Species & Lower Ranks", background="WHITE")
headerfour.grid(row=2, column=5)
rowheaderone = Label(frameb, text="Reported", background="WHITE")
rowheaderone.grid(row=3, column=1)
rowheadertwo = Label(frameb, text="Detected", background="WHITE")
rowheadertwo.grid(row=4, column=1)
entryone = Entry(frameb, textvariable=varone, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryone.grid(row=4, column=2)
entrytwo = Entry(frameb, textvariable=vartwo, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entrytwo.grid(row=4, column=3)
entrythree = Entry(frameb, textvariable=varthree, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entrythree.grid(row=4, column=4)
entryfour = Entry(frameb, textvariable=varfour, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryfour.grid(row=3, column=2)
entryfive = Entry(frameb, textvariable=varfive, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryfive.grid(row=3, column=3)
entrysix = Entry(frameb, textvariable=varseven, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entrysix.grid(row=3, column=4)
entryseven = Entry(frameb, textvariable=varsix, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryseven.grid(row=3, column=5)
entryeight = Entry(frameb, textvariable=varinfrasp, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryeight.grid(row=4, column=5)
frameb.grid(row=2, column=0, columnspan=4, rowspan=3, sticky=N+E+S+W, pady=2)

framec = Frame(root)
fileinf_lab = Label(framec, text="Working FindIt Data File:")
fileinf_lab.grid(row=5, column=0)
fileinf_ent = Entry(framec, bg=root.cget('bg'),textvariable=filename)
fileinf_ent.grid(row=5, column=2, columnspan=2)
change_file_button = Button(framec, text = "Switch FindIt Data File", command = OpenFile)
change_file_button.grid(row=5, column=4, padx = 1)
framec.grid(row=5, column=0, columnspan=5, rowspan=1, sticky=N+E+S+W, pady=2)

framed = Frame(root)
outfileinf_lab = Label(framed, text="Working Output File:")
outfileinf_lab.grid(row=6, column=0)
outfileinf_ent = Entry(framed, bg=root.cget('bg'),textvariable=outfilename)
outfileinf_ent.grid(row=6, column=2, columnspan=2)
change_outfileinf_button = Button(framed, text = "Update Numbers From Working Output File", command = refresh)
change_outfileinf_button.grid(row=6, column=4, padx = 1)
framed.grid(row=6, column=0, columnspan=5, rowspan=1, sticky=N+E+S+W, pady=2)

frameE = Frame(root, background="WHITE")
calc_label = Button(frameE, text="Calculate\nDetected/Reported", command=calc)
calc_label.grid(row=7, rowspan=2, sticky=N+E+S+W, padx=1)
headeruno = Label(frameE, text="Families", background="WHITE")
headeruno.grid(row=7, column=2)
headerdos = Label(frameE, text="Genera", background="WHITE")
headerdos.grid(row=7, column=3)
headertres = Label(frameE, text="Species", background="WHITE")
headertres.grid(row=7, column=4)
headerquatro = Label(frameE, text="Species & Lower Ranks", background="WHITE")
headerquatro.grid(row=7, column=5)
entryuno = Entry(frameE, textvariable=vareight, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryuno.grid(row=8, column=2)
entrydos = Entry(frameE, textvariable=varnine, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entrydos.grid(row=8, column=3)
entrytres = Entry(frameE, textvariable=varten, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entrytres.grid(row=8, column=4)
entryquatro = Entry(frameE, textvariable=vareleven, disabledbackground="WHITE", justify=CENTER, state=DISABLED)
entryquatro.grid(row=8, column=5)
frameE.grid(row=7, column=0, columnspan=5, rowspan=2, sticky=N+E+S+W, pady=2)

frameF = Frame(root)
about_hy = Label(frameF, text="Removed\nUnnamed Hybrids")
about_hy.grid(row=9, column=0, padx=1)
hy_count = Spinbox(frameF, state="readonly", textvariable=rm_hybrids_num, from_=0, to=9999, increment=1)
hy_count.grid(row=9, column=1, padx=1)
about_un_sp = Label(frameF, text="Removed\nUnnamed Species (sp.)")
about_un_sp.grid(row=9, column=2, padx=1)
unnamed_sp_count = Spinbox(frameF, state="readonly", textvariable=rm_sp_num, from_=0, to=9999, increment=1)
unnamed_sp_count.grid(row=9, column=3, padx=1)
frameF.grid(row=9, column=0, columnspan=5, rowspan=1, sticky=N+E+S+W, pady=2)

root.config(menu=menubar)
root.mainloop()

