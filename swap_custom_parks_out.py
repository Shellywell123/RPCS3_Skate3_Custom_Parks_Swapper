import os

#paths for python
parks_repo_path = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/ROM's/Playstation 3/DLC's and Extras/Skate 3/Skate 3 Custom Parks/"
os_parks_repo_path = "/mnt/c/Users/benja/Documents/Entertainment/Gaming/ROM\\'s/Playstation\\ 3/DLC\\'s\\ and\\ Extras/Skate\\ 3/Skate\\ 3\\ Custom\\ Parks/"

#paths for terminal
rpcs3_park_folder_path = '/mnt/c/Users/benja/Documents/Entertainment/Gaming/Launchers/PS3/dev_hdd0/home/00000001/savedata/BLES00760-SPARK_SKATER/'
os_rpcs3_park_folder_path = '/mnt/c/Users/benja/Documents/Entertainment/Gaming/Launchers/PS3/dev_hdd0/home/00000001/savedata/BLES00760-SPARK_SKATER/'

#########################################################################

def ascii():
    """ascii art for begining og program"""
    print("""--------------------------------------------------------------
   __|  |  /    \ __ __| __| __ /    _ \  \    _ \  |  /   __| 
 \__ \  . <    _ \   |   _|   _ \    __/ _ \     /  . <  \__ \ 
 ____/ _|\_\ _/  _\ _|  ___| ___/   _| _/  _\ _|_\ _|\_\ ____/ 
 --------------------------------------------------------------
""")


def set_current_save_parks(newname):
    """sets txt log to be the name of the current skate parks file in the RPCS3 folder"""
    file = parks_repo_path+'CPIRPCS(DoNotDelete).txt'

    with open(file, 'w') as f:
        f.write(newname)

def get_current_save_parks():
    """ retrieve the name of the current skateparks file in the RPCS3 file from the log txt"""
    file = parks_repo_path+'CPIRPCS(DoNotDelete).txt'

    with open(file, 'r') as f:
       cont = f.read()
    print('\nCurrent park save in game:')
    print(' - '+cont)
    return cont

def update_park_save_changes():
    """ performs a backup of any changes to a skate park file in the  RPCS3 folder before it is swapped out """
    current_park_save = get_current_save_parks()
    try:
        osstr = 'cp {}* {}'.format(os_rpcs3_park_folder_path,os_parks_repo_path+current_park_save+'/')
        os.system(osstr)
        print('Updated {} in Repo'.format(current_park_save))
    except:
        print('Updated of {} in Repo FAILED'.format(current_park_save))
        exit(0)

def empty_rpcs3():
    """empties the RPCS3 folder before a differrent save park file is swapped in"""
    os.system('rm {}*'.format(os_rpcs3_park_folder_path))
    print('Emptied RPCS3 folder')

def print_files_in_rpcs3_folder():
    """shows the user the contents of the RPCS3 folder"""
    for d in os.listdir(rpcs3_park_folder_path) :
        print(' - '+str(d))

def list_park_saves_in_repo():
    """shows the user the possible options of save park files he can swap between"""
    print('\nSave parks in repository:')

    repo_list = []
    for d in os.listdir(parks_repo_path) :
        if '.' not in d:
            print(' - '+str(d))
            repo_list.append(d)

    return repo_list

def swap_park_saves():
    """swaps out custom skate park saves in RPCS3 folder via a user input"""
    update_park_save_changes()
    
    choice_list = list_park_saves_in_repo()

    choice = input('\nInput which Park_Saves you want to play (can copy and paste from list above):\n')
    print('')

    if choice == 'exit':
        exit(0)

    if choice in choice_list:
        empty_rpcs3()
        ostr = "cp {}* {}".format(os_parks_repo_path+choice+'/',os_rpcs3_park_folder_path)
        os.system(ostr)
        print('{} files copied into RPCS3 folder'.format(choice))
        set_current_save_parks(choice)
        print('--------------------------------------------------------------')
    else:
        print('not a valid input')

#########################################################################

# run this
ascii()
swap_park_saves()