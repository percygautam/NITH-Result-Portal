# Import required packages
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.listview import ListItemButton
# import dbraw file 
from dbraw import *
# type of plot(SGPI OR CGPI)
global plot_type
plot_type=[]
# list of roll nos 
roll_nos=[]
second_roll_nos=[]

class ListButton(ListItemButton):
    pass
 
class Details(BoxLayout):
 
    # Connects the value in the TextInput widget to these fields
    
    second_roll_no_text_input = ObjectProperty()
    roll_no_text_input=ObjectProperty()
    group_list = ObjectProperty()
    
    # sgpi radio button's functionality
    sgpi_active = ObjectProperty(True)
    def sgpi_clicked(self,instance,value):
        if value is True:
            plot_type.append("SGPI")
            
        else:
            plot_type.remove("SGPI")
    
    # cgpi radio button's functionality        
    cgpi_active =  ObjectProperty(False)
    def cgpi_clicked(self,instance,value):
        if value is True:
            plot_type.append("CGPI")
            
        else:
            plot_type.remove("CGPI")
            
    #when compare button is hit
    def submit_member(self):
        roll_nos=[]
        second_roll_nos=[]

        # Get first roll no from the TextInputs
        roll_no = self.roll_no_text_input.text 
        
        # Get second roll no from the TextInputs
        second_roll_no = self.second_roll_no_text_input.text 
        
        # Add the first roll no to roll_nos
        roll_nos.append(roll_no)
        
        # check if second roll no text input is empty
        if(second_roll_no!=""):
            second_roll_nos.append(second_roll_no)
            
        # call main function of dbraw
        mainfunc(roll_nos,second_roll_nos,plot_type)
        

    # when compare to new button is hit       
    def delete_member(self, *args):
        second_roll_nos=[]
        # clear second roll no text input
        self.second_roll_no_text_input.text=""
    
    #when exit button is hit
    def Exit_app(self):
        
        #stop the app
        App.get_running_app().stop()
        Window.close()      # Closes the window


 
class DetailsApp(App):
    def build(self):
        
        return Details()

# Create the instance of the class DetailsApp
dbApp = DetailsApp()
dbApp.run()     # Running the app
exit()      # Exits the process
