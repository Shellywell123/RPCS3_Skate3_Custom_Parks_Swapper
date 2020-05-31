#  RPCS3_Skate3_Custom_Parks_Swapper
(!THIS IS STILL IN DEVELOPMENT, IF YOU ARE GOING TO USE THIS PROGRAM, BACKUP ALL YOUR CUSTOM SKATEPARK FILES FIRST TO A SEPERATE FOLDER ON YOU PC!)\
If like me you have recently moved from gaming on your PS3 console to to a PC and are now using RPCS3 to continue playing the best game in the world (Skate3). You may also have multiple custom skatepark files, ones which you have made on your old PS3 and ones which you have since made on your PC. This program is to be used for easily swapping out the custom skate park files in the RPCS3 emulator to be played in the game. As my knowlege thus far is that you can only have one skateparks file at a time, and not sure there is a way to combine them.
(Note this program is for swapping between skatepark save files you already own, using the basic commands in a linux terminal i.e 'cp'.)

### How to setup:
In the python script you need to change the the paths to be relative to the folders on your PC (I will leave mine in script as an example):

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

Instructions still to be written

### How to run:
Once you have completed the set up instuctions above, execute the python script using python3:
```bash
foo@bar:~$ python3 swap_custom_parks_out.py
--------------------------------------------------------------
   __|  |  /    \ __ __| __| __ /    _ \  \    _ \  |  /   __|
 \__ \  . <    _ \   |   _|   _ \    __/ _ \     /  . <  \__ \
 ____/ _|\_\ _/  _\ _|  ___| ___/   _| _/  _\ _|_\ _|\_\ ____/
 --------------------------------------------------------------


Current park save in game:
 - Bens_Razer_Blade_Parks
Updated Bens_Razer_Blade_Parks in Repo

Save parks in repository:
 - Bens_PS3_Slim_Parks
 - Bens_Razer_Blade_Parks
 - Dizeeus_Skateparks
 - EU_Skateparks
 - EU_Top_Rated
 - GHFears_Server_Dump
 - Untreated_Park_files
```
The program will then tell you which park is currently in your RPCS3 folder and save any changes you have made to it while playing before swapping it. The program will also list all the custom park folders you can swap from and ask you to chose one via a user input. In the example script below 'Bens_PS3_Slim_Parks' was chosen.
```bash
Input Which Park_Saves you want to play:
>> Bens_PS3_Slim_Parks

Emptied RPCS3 folder
Bens_PS3_Slim_Parks files placed into RPCS3 folder
--------------------------------------------------------------
```
The program then empties your RPCS3 custom park folder and copies in the files from the chosen folder you inputted.\
Your skate 3 game should now have different custom parks when you play it in RPCS3 :)