#  RPCS3_Skate3_Custom_Parks_Swapper
(!THIS IS STILL IN DEVELOPMENT, IF YOU ARE GOING TO USE THIS PROGRAM, BACKUP ALL YOUR CUSTOM SKATEPARK FILES FIRST TO A SEPERATE FOLDER ON YOU PC!)\
\
This program manages the custom skatepark files ('SPARK_SKATER') for skate 3 in the RPCS3 emulator, I wrote this as I have many custom park files I enjoy swapping between and got tired of manually copying and pasting between directories on my PC.\

### Background
If like me you have recently moved from gaming on your PS3 console to to a PC and are now using RPCS3 to continue playing the best game in the world (Skate 3). You are likely to have multiple custom skatepark files, ones which you have made on your old PS3 console and ones which you have since made on your PC. 

This program is designed be used for quickly and easily swapping between custom skate 3 skate park files for playing in the RPCS3 emulator. My knowledge thus far is that you can only have one custom skateparks file occupying the RPCS3 emulator at a time, and am not yet sure wether there is a way to combine multiple file into once, hence the need to swap between files.\
\
(Note this program is for swapping between skatepark save files you already have on your PC or dumped from your console)\

### Code  
The program uses the basic linux commands  such as 'cp' and 'rm' to move files around on your machine via the python 3 package 'os'.

### How to setup:

#### 1) Set up your various park save files in the format the program expects

 - All parks files 'SPARK_SKATER' have been extracted into named folders containing B,H,DDATA,PDF,SFO files. It is preferable the the folder names do not contain spaces or non-ascii characters. Example = 'My_PC_Parks/' as a folder name.

 - The parent folder containing all your park save folders must also contain a txt file named 'CPIRPCS(DoNotDelete).txt' and in it must be the matching name to one of the folders in your repo/parent folder. If this is the first time swapping out custom park files on your pc, yoou will have your pc's made parks in the rpcs3 folder, therfore you will want to put the name 'My_PC_Parks' or your equivalent folder name written in the txt with no trailing spaces. The program reads this txt file to know which of the folders/ park files in currently in use in RPCS3.

#### 2) Set script paths to be for your machine.

 - In the python script you need to change the the paths to be relative to the folders on your PC (I will leave mine in script as an example):

```python
#paths for python
parks_repo_path = "path to where your multiple park files are stored"
os_parks_repo_path = "same as above with appropriate '\'s in path "

#paths for terminal
rpcs3_park_folder_path = 'path to RPCS3/dev_hdd0/home/00000001/savedata/BLES00760-SPARK_SKATER/'
    #may be BLUS is you have US ver of skate3
os_rpcs3_park_folder_path = "same as above with appropriate '\'s in path "
```
(Note this program expects the custom park files to extracted in to folders, alongside a txt containing the name of the current park in the RPCS3 folder)\

### How to run:
Once you have completed the set up instuctions above, execute the python script using python3:
```bash
foo@bar:~$ python3 swap_custom_parks_out.py
--------------------------------------------------------------
   __|  |  /    \ __ __| __| __ /    _ \  \    _ \  |  /   __|
 \__ \  . <    _ \   |   _|   _ \    __/ _ \     /  . <  \__ \
 ____/ _|\_\ _/  _\ _|  ___| ___/   _| _/  _\ _|_\ _|\_\ ____/
 --------------------------------------------------------------


Current Custom Park file in RPCS3:
 - My_PC_Parks
Saved any changes made to My_PC_Parks to your repository

Custom Park files in your repository:
 - My_PS3_Slim_Parks
 - My_PC_Parks
 - My_Friends_Parks
```
The program will then tell you which park is currently in your RPCS3 folder and save any changes you have made to it while playing before swapping it. The program will also list all the custom park folders you can swap from and ask you to chose one via a user input. In the example script below 'Bens_PS3_Slim_Parks' was chosen.
```bash
Input which Park_Saves you want to play (can copy and paste from list above):
>> My_PS3_Slim_Parks

Emptied RPCS3 folder
My_PS3_Slim_Parks files copied into RPCS3 folder
--------------------------------------------------------------
```
The program then empties your RPCS3 custom park folder and copies in the files from the chosen folder you inputted.\
Your skate 3 game should now have different custom parks when you play it in RPCS3 :)