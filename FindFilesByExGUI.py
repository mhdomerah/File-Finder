import tkinter as tk
from tkinter import messagebox,filedialog,ttk
import os, shutil, re

#Main Varible
root = tk.Tk()
root.title('Files Finder v1.0')
root.geometry('600x400')
root.config(bg='white')
root.resizable(False,False)
Path_ = ' '
TargetFolderName = ' '
CountFiles = 0
CountExt = 0 
FundedFilesList = []

#Browes (Lable)
Browes_lbl = tk.Label(root, text='Select folder :', font=('bold',12),bg='white')
Browes_lbl.place(x=5,y=15)

#Browes (Button)
Browes_btn = tk.Button(root, text ='Browse', command = lambda:BrowesFolder(), font=('bold'),bg='blue',fg='white',height = 1, width = 6) 
Browes_btn.place(x=100,y=12)

#Browes (Entry)
Browes_ent = tk.Entry(root,width=47,font=('bold',12))
Browes_ent.place(x=170,y=17)

#Extention (Lable)
Ext_lbl = tk.Label(root, text='Select form list', font=('bold',12),bg='white')
Ext_lbl.place(x=5,y=60)

#Selected Extention (Lable)
Ext_slbl = tk.Label(root,width=11,font=('bold',12),bg='#fff7d8')
Ext_slbl.place(x=115,y=60)

#Find (Button)
Search_btn = tk.Button(root, text ='Find', command = lambda:FindFilesByExtension(), font=('bold'),bg='blue',fg='white', height = 1, width = 6) 
Search_btn.place(x=230,y=55)

#Exprot (Button)
Export_btn = tk.Button(root, text ='Exprot List', command = lambda:ExportFilesListToText(), font=('bold'),bg='#26ff00',fg='black', height = 1, width = 8) 
Export_btn.place(x=300,y=55)

#Copy (Button)
Search_btn = tk.Button(root, text ='Copy', command = lambda:CopyFilesByExtension(), font=('bold'),bg='blue',fg='white', height = 1, width = 6) 
Search_btn.place(x=390,y=55)

#Move (Button)
Search_btn = tk.Button(root, text ='Move', command = lambda:MoveFilesByExtension(), font=('bold'),bg='blue',fg='white', height = 1, width = 6) 
Search_btn.place(x=460,y=55)

#Delete (Button)
Search_btn = tk.Button(root, text ='Delete', command = lambda:DeleteFilesByExtension(), font=('bold'),bg='red',fg='white', height = 1, width = 6) 
Search_btn.place(x=530,y=55)

#Status Text (Text)
Status_txt = tk.Text(root, wrap=tk.WORD,height=13, width=39,bg='black',borderwidth=1, highlightthickness=0,font=('bold',14), fg='#26ff00')

Status_txt.insert(tk.END ,'                     ------:: Files Finder v1.0::------'+
                        '\n'+
                        '\n'+'Instruction : '+
                        '\n'+'1- Browse folder '+
                        '\n'+'2- Select extension from the list'+
                        '\n'+'3-'+
                        '\n'+'- To export file list to text file press Export'+
                        '\n'+'- To copy the files press Copy'+
                        '\n'+'- To move the files press Move'+
                        '\n'+'- To delete the files press Delete'+
                        '\n')

Status_txt.config(state=tk.DISABLED)
Status_txt.place(x=160,y=100)

#Founded Extension (Lable)
Ext_flbl = tk.Label(root, font=('bold',14),width=12 ,bg='#fff7d8',fg='red')
Ext_flbl.place(x=9,y=360)

#Extension List (ListBox)
Ext_lbox = tk.Listbox(root, height=11, width=13, border=1,font=('bold',14),fg='#8a0b0b')
Ext_lbox.place(x=7,y=100)

#Main Function
def FindFilesByExtension():
    global TargetFolderName
    global CountFiles
    global FundedFilesList
    FundedFilesList = []
    CountFiles = 0
    TargetExtension = ' '
    index = Ext_lbox.curselection()  
            
    if not index:
        Status_txt.config(state=tk.NORMAL)
        Status_txt.delete(1.0,tk.END)
        Status_txt.insert(tk.END ,'Select Extension Form the list or Browse Folder')
        Status_txt.config(state=tk.DISABLED)

    else:
        #Show Status Message
        Status_txt.config(state=tk.NORMAL)
        Status_txt.delete(1.0,tk.END)
        Status_txt.insert(tk.END ,'Finding files, Please wait...')
        Status_txt.config(state=tk.DISABLED)

        TargetExtension = str(Ext_lbox.get(Ext_lbox.curselection()))
        if Path_ == ' ':
            Status_txt.config(state=tk.NORMAL)
            Status_txt.delete(1.0,tk.END)
            Status_txt.insert(tk.END ,'Select folder first')
            Status_txt.config(state=tk.DISABLED)
        else:
            MsgBox = tk.messagebox.askquestion ('Find Files','Are you sure ?',icon = 'warning')
            if MsgBox == 'yes':
                TargetFolderName = '_'+TargetExtension.upper() + ' ' + 'Files'
                TargetPath = Path_+'\\'+TargetFolderName
                try:                
                    for folderNames,subFolders,fileNames in os.walk (Path_):
                        for filename in fileNames:
                            if folderNames != str(TargetPath):  
                                if filename.endswith(TargetExtension):
                                    CountFiles = CountFiles + 1
                                    FundedFilesList.append(folderNames+'\\'+filename)
                            else:
                                break
                        
                    if CountFiles == 0:
                        Status_txt.config(state=tk.NORMAL)
                        Status_txt.delete(1.0,tk.END)
                        Status_txt.insert(tk.END ,'No files founded or alredy done')
                        Status_txt.config(state=tk.DISABLED)
                    else:
                        Status_txt.config(state=tk.NORMAL)
                        Status_txt.delete(1.0,tk.END)
                        Status_txt.insert(tk.END ,'['+str(CountFiles)+']'+
                                                 ' ('+TargetExtension+') Files founded'+
                                                 '\n\n')
                        for item in FundedFilesList:
                            Status_txt.insert(tk.END,item+'\n\n')

                        Status_txt.config(state=tk.DISABLED)
                        Ext_slbl.config(text=TargetExtension)

                except IOError:
                    Status_txt.config(state=tk.NORMAL)
                    Status_txt.delete(1.0,tk.END)
                    Status_txt.insert(tk.END ,'Access Denied :'+'\n'+folderNames+'\\'+filename)
                    Status_txt.config(state=tk.DISABLED)
            else:
                Status_txt.config(state=tk.NORMAL)
                Status_txt.delete(1.0,tk.END)
                Status_txt.insert(tk.END ,'Operation canceled')
                Status_txt.config(state=tk.DISABLED)
               
def ExportFilesListToText():
    global CountFiles
    TragetExtension = str(Ext_slbl.cget('text'))
    TargetFileName = '_'+TragetExtension.upper()+' Files List.txt'
    cwd = os.getcwd()

    #Show Status Message
    Status_txt.config(state=tk.NORMAL)
    Status_txt.delete(1.0,tk.END)
    Status_txt.insert(tk.END ,'Exporting list, Please wait...')
    Status_txt.config(state=tk.DISABLED)

    if CountFiles == 0:
        Status_txt.config(state=tk.NORMAL)
        Status_txt.delete(1.0,tk.END)
        Status_txt.insert(tk.END ,'Find the file or Select file extension from list')
        Status_txt.config(state=tk.DISABLED)
    
    else:
        try:
            file = open(TargetFileName, "w")
            for item in FundedFilesList:
                file.write(item+'\n\n')

            file.close()
            Status_txt.config(state=tk.NORMAL)
            Status_txt.delete(1.0,tk.END)
            Status_txt.insert(tk.END ,'Files list exported successfully to:'+
                                      '\n\n'+cwd+'\\'+TargetFileName)
            Status_txt.config(state=tk.DISABLED)
            
        
        except IOError:
            Status_txt.config(state=tk.NORMAL)
            Status_txt.delete(1.0,tk.END)
            Status_txt.insert(tk.END ,'Cannot creat file. Access Denied :'+'\n'+cwd)
            Status_txt.config(state=tk.DISABLED)
    
def MoveFilesByExtension():
    global CountFiles
    global TargetFolderName
    TragetExtension = str(Ext_slbl.cget('text'))
    TargetFolderName = '_'+TragetExtension.upper() + ' ' + 'Files'
    TargetPath = Path_+'\\'+TargetFolderName

    #Show Status Message
    Status_txt.config(state=tk.NORMAL)
    Status_txt.delete(1.0,tk.END)
    Status_txt.insert(tk.END ,'Moving files, Please wait...')
    Status_txt.config(state=tk.DISABLED) 


    if CountFiles == 0:
        Status_txt.config(state=tk.NORMAL)
        Status_txt.delete(1.0,tk.END)
        Status_txt.insert(tk.END ,'Find the file or Select file extension from list')
        Status_txt.config(state=tk.DISABLED)

    else:
        #MassgeBox (Massagebox)
        MsgBox = tk.messagebox.askquestion ('Move Files','Are you sure you want to MOVE files ?',icon = 'warning')
        if MsgBox == 'yes':
            try: 
                for item in FundedFilesList:
                    if CheckFolderIfExsit():
                        shutil.move(item, TargetPath)
                    else:
                        os.makedirs(TargetPath)
                        shutil.move(item, TargetPath)

                Status_txt.config(state=tk.NORMAL)
                Status_txt.delete(1.0,tk.END)
                Status_txt.insert(tk.END ,'Operation succeeded'
                                    +'\n'+'Files moved to :'+'\n\n'+TargetPath
                                  +'\n\n'+'Updating files list, Please wait...')    
                GetExtensionListInFolder()
                Status_txt.insert(tk.END ,'\n\n'+'Files extension list updated successfully')
                Status_txt.config(state=tk.DISABLED)

            except IOError:
                Status_txt.config(state=tk.NORMAL)
                Status_txt.delete(1.0,tk.END)
                Status_txt.insert(tk.END ,'Access Denied or file does not exist'+'\n\n'+item)
                Status_txt.config(state=tk.DISABLED)

        else:
            Status_txt.config(state=tk.NORMAL)
            Status_txt.delete(1.0,tk.END)
            Status_txt.insert(tk.END ,'Operation canceled')
            Status_txt.config(state=tk.DISABLED)

def CopyFilesByExtension():
    global CountFiles
    global TargetFolderName
    TragetExtension = str(Ext_slbl.cget('text'))
    TargetFolderName = '_'+TragetExtension.upper() + ' ' + 'Files'
    TargetPath = Path_+'\\'+TargetFolderName

    #Show Status Message
    Status_txt.config(state=tk.NORMAL)
    Status_txt.delete(1.0,tk.END)
    Status_txt.insert(tk.END ,'Copying files, Please wait...')
    Status_txt.config(state=tk.DISABLED)   

    if CountFiles == 0:
        Status_txt.config(state=tk.NORMAL)
        Status_txt.delete(1.0,tk.END)
        Status_txt.insert(tk.END ,'Find the file or Select file extension from list')
        Status_txt.config(state=tk.DISABLED)

    else:
        #MassgeBox (Massagebox)
        MsgBox = tk.messagebox.askquestion ('Copy Files','Are you sure you want to COPY files ?',icon = 'warning')
        if MsgBox == 'yes':
            try: 
                for item in FundedFilesList:
                    if CheckFolderIfExsit():
                        shutil.copy(item, TargetPath)
                    else:
                        os.makedirs(TargetPath)
                        shutil.copy(item, TargetPath)
                        
                Status_txt.config(state=tk.NORMAL)
                Status_txt.delete(1.0,tk.END)
                Status_txt.insert(tk.END ,'Operation succeeded'+'\n'+'Files copied to :'
                                    +'\n\n'+TargetPath)
                Status_txt.config(state=tk.DISABLED)

            except IOError:
                Status_txt.config(state=tk.NORMAL)
                Status_txt.delete(1.0,tk.END)
                Status_txt.insert(tk.END ,'Access Denied :'+'\n\n'+item)
                Status_txt.config(state=tk.DISABLED)

        else:
            Status_txt.config(state=tk.NORMAL)
            Status_txt.delete(1.0,tk.END)
            Status_txt.insert(tk.END ,'Operation canceled')
            Status_txt.config(state=tk.DISABLED)

def DeleteFilesByExtension():
    global CountFiles
    global TargetFolderName
    TragetExtension = str(Ext_slbl.cget('text'))
    TargetFolderName = '_'+TragetExtension.upper() + ' ' + 'Files'

    #Show Status Message
    Status_txt.config(state=tk.NORMAL)
    Status_txt.delete(1.0,tk.END)
    Status_txt.insert(tk.END ,'Deleting files, Please wait...')
    Status_txt.config(state=tk.DISABLED) 


    if CountFiles == 0:
        Status_txt.config(state=tk.NORMAL)
        Status_txt.delete(1.0,tk.END)
        Status_txt.insert(tk.END ,'Find the file or Select file extension from list')
        Status_txt.config(state=tk.DISABLED)

    else:
        #MassgeBox (Massagebox)
        MsgBox = tk.messagebox.askquestion ('Delete Files','Are you sure you want to DELETE files ?',icon = 'warning')
        if MsgBox == 'yes':
            DelMsgBox = tk.messagebox.askquestion ('Delete Files','All files with extension ('+TragetExtension+')'+' will be deleted.Are sure ?',icon = 'warning')
            if DelMsgBox == 'yes':  
                try:       
                    for item in FundedFilesList:
                        os.remove(item)

                    Status_txt.config(state=tk.NORMAL)
                    Status_txt.delete(1.0,tk.END)
                    Status_txt.insert(tk.END ,'Operation succeeded'
                                        +'\n'+'All files with extension ('+TragetExtension+')'+' Deleted'
                                      +'\n\n'+'Updating files list, Please wait...')
                    GetExtensionListInFolder()
                    Status_txt.insert(tk.END ,'\n\n'+'Files extension list updated successfully')
                    Status_txt.config(state=tk.DISABLED)

                except IOError:
                    Status_txt.config(state=tk.NORMAL)
                    Status_txt.delete(1.0,tk.END)
                    Status_txt.insert(tk.END ,'Access Denied or file does not exist'+'\n\n'+item)
                    Status_txt.config(state=tk.DISABLED)
            else:
                Status_txt.config(state=tk.NORMAL)
                Status_txt.delete(1.0,tk.END)
                Status_txt.insert(tk.END ,'Operation canceled')
                Status_txt.config(state=tk.DISABLED)
        else:
            Status_txt.config(state=tk.NORMAL)
            Status_txt.delete(1.0,tk.END)
            Status_txt.insert(tk.END ,'Operation canceled')
            Status_txt.config(state=tk.DISABLED)

def BrowesFolder():
    #Show Status Message
    Status_txt.config(state=tk.NORMAL)
    Status_txt.delete(1.0,tk.END)
    Status_txt.insert(tk.END ,'Getting files extension, Please wait...'+
                              '\n\n'+'This may take a while, Depending on selected folder size.')
    Status_txt.config(state=tk.DISABLED)

    FolderPath = filedialog.askdirectory()
    global Path_
    Path_ = FolderPath
    Path_ = Path_.replace('/','\\')
    Browes_ent.config(state=tk.NORMAL)
    Browes_ent.delete(0,tk.END)
    Browes_ent.insert(tk.END,str(Path_))
    GetExtensionListInFolder()
    Ext_flbl.config(text=str(CountExt))

    #Show Status Message
    Status_txt.config(state=tk.NORMAL)
    Status_txt.delete(1.0,tk.END)
    Status_txt.insert(tk.END ,'Files extension list updated successfully')
    Status_txt.config(state=tk.DISABLED)

def GetExtensionListInFolder():
    global CountExt
    CountExt = 0 
    FilesExtList = []
    i = 0
    Ext_lbox.delete(0,tk.END)
    #Get extension list in target folder 
    for folderNames,subFolders,fileNames in os.walk (Path_):
        for filename in fileNames:
            #if folderNames != str(forTest):
                #Ensure that you do not search previously sorted files
                fFolderName = folderNames[len(Path_):]
                if fFolderName.startswith('\\_'):
                    break                            
                else:
                    fFileName,fFileExt = os.path.splitext(filename)
                    if fFileExt not in FilesExtList:
                        if fFileExt != '':
                                FilesExtList.append(fFileExt)
                                CountExt = CountExt + 1
                        else:
                            continue
                    else:
                        continue 
            #else:
            #    break
    
    #Insert extension list  to the list box 
    for item in FilesExtList:
        Ext_lbox.insert(i,item)
        i = i + 1
    
def CheckFolderIfExsit():
    global TargetFolderName
    for folderNames in os.walk(Path_):
        if folderNames[0] == str(Path_+'\\'+TargetFolderName):
            return True
        else:
            continue

#Start Program
root.mainloop()
