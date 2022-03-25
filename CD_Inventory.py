#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# DRodriguez, 2021-Mar-24, modified code
#------------------------------------------#

# -- DATA -- #
file_name = 'cdInventory.txt'
table = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """ 
    # -- Fields -- #
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
        except ValueError:
            print('Please enter a valid CD ID.')
        except Exception as e:
            raise Exception('ERROR: Error defining CD inputs')
            
    # -- Properties -- #
    @property
    def cd_id (self):
        return self.__cd_id
    
    @cd_id.setter 
    def cd_id (self, value):
        try:
            self.__cd_id == int(value)
        except ValueError:
            print('Please enter a valid CD ID.')
    
    @property
    def cd_title (self):
        return self.__cd_title
    
    @cd_title.setter 
    def cd_title(self, value):
        try:
            self.__cd_title == str(value)
        except Exception as e:
            raise Exception('ERROR: Please enter a CD title as a string.')
    
    @property
    def cd_artist (self):
        return self.__cd_artist
    
    @cd_artist.setter 
    def cd_artist(self, value):
        try:
            self.__cd_artist == str(value)
        except Exception as e:
            raise Exception('ERROR: Please enter a Artist as a string.')
    
    # -- Methods -- #
    
    def print_to_screen(self):
        """prints data to screen"""
        return '{:>2}\t{} (by {})'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
    
    def print_to_file(self):
        """prints data to file"""
        return '{},{},{}\n'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
    
    # TODO Add Code to the CD class
    pass

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    # TODO Add code to process data to a file
    pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for objCD in table:
            print(objCD.print_to_screen())
        
        print('======================================')
    
    @staticmethod
    def add_CD():
        """Ask user for new ID, CD Title and Artist

          Args:
              strID: name of ID input
              strTitle: name of title input
              strArtist: name of artist input
              intID: Converts strID to integer

          Returns:
              values defined in arguments if no errors occur
              
          """
        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID = int(strID)
                break
            except ValueError:
                print('Please enter a number for CD ID.')
            except Exception as e:
                print('Request could not be completed. There was an error.')
                print(type(e), e, e.__doc__, sep='\n')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        intID = int(strID)
        return intID, strTitle, strArtist



    
    # TODO add docstring
    # TODOne add code to show menu to user
    # TODOne add code to captures user's choice
    # TODOne add code to display the current data on screen
    # TODOne add code to get CD data from user
    pass

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            Table if no errors occur
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    cd_id, cd_title, cd_artist = line.strip(',').split()
                    objCD = CD(cd_id, cd_title, cd_artist)
                    table.append(objCD)
        except FileNotFoundError:
            print('File not found.')
        except Exception as e:
            print('Request could not be completed. There was an error.')
            print(type(e), e, e.__doc__, sep='\n')
        else:
            return table

class DataProcessor:
    @staticmethod
    def add_CD(new_CD, lstTbl):
        """Function to add a new item to table
        
        Args:
            dicRow: creates dictionary
            lstTbl: adds new values to dictionary
            show_inventory: displays data
            
        Returns:
            Table showing inventory in lstTbl
        
        """
        intID, strTitle, strArtist = new_CD
        new_CD = CD(intID, strTitle, strArtist)
        table.append(new_CD)
        return table
    
    @staticmethod
    def write_file(file_name, table):
        """Function to save data
        
        Args:
            objFile: calls the text file containing CD inventory
            lstValues: row of values in 2D table
            objFile.write: writes inputted data to file
            stTbl (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
            
        Returns:
            Table showing inventory in lstTbl if no errors occur
        
        """
    try:
        with open(file_name, 'w') as readfileObj:
            for objCD in table:
                file_name.write(objCD.print_to_file())
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print('Request could not be completed. There was an error.')
        print(type(e), e, e.__doc__, sep='\n')
        
# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # Process menu selection
    # Process exit first
    if strChoice == 'x':
        break
    # Load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(file_name, table)
            IO.show_inventory(table)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(table)
        continue  # start loop back at top.
    # Add a CD
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist and add item to table
        new_cd = IO.add_CD()
        lstTbl =  DataProcessor.add_CD(new_cd, table)
        continue  # start loop back at top.
    # Display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # Save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            # Save data
            DataProcessor.write_file(file_name, table)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    #Catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
