
# coding: utf-8

# # Managing Files in Folders using Python

# ##Current working Directory

# In[14]:

import os
cwd=os.getcwd()
print (cwd)


# ##Change current directory to the one you want to manage and look at the immediate subdirectories

# In[15]:

mywd=os.chdir('C:\\Users\\Pritanshi.Khurana\\Desktop\\MF')
os.listdir(mywd)


# ##Select a folder you want to manage, say NHM_GO

# In[16]:

managewd=os.chdir('C:\\Users\\Pritanshi.Khurana\\Desktop\\MF\\NHM_GO')


# ##Make new folders in which you want your files to get sorted

# In[ ]:

codes=""
data=""
deliverables=""
def makeFolders(x,y,z):
    if not os.path.exists(x):
        os.makedirs(x)
        codes=os.path.abspath(x)
    if not os.path.exists(y):
        os.makedirs(y)
        data=os.path.abspath(y)
    if not os.path.exists(z):
        os.makedirs(z)
        deliverables=os.path.abspath(z)
        
makeFolders('C:\\Users\\Pritanshi.Khurana\\Desktop\\MF\\NHM_GO\\codes',
            'C:\\Users\\Pritanshi.Khurana\\Desktop\\MF\\NHM_GO\\data',
            'C:\\Users\\Pritanshi.Khurana\\Desktop\\MF\\NHM_GO\\deliverables' );


# ##Send R files to code folder, Excels to data and html and pptx files to deliverables

# In[21]:

import shutil
newPath=""

def folderStructure(file_ext1, file_ext2,newfolder):
    for (dirname, dirs, files) in os.walk('.'):
        for filename in files:
            targetFile = os.path.abspath(filename)
            newPath=newfolder +str("\\")+str(filename)
            if filename.endswith(file_ext1) or filename.endswith(file_ext2) :
                try:
                    shutil.move(targetFile,newPath)
                except(FileNotFoundError):
                    pass
folderStructure('.xlsx', '.csv', data);
folderStructure('.pptx', '.html', deliverables);
folderStructure('.R', '.Rmd', codes);

