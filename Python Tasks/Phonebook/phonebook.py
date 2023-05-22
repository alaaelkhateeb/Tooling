import sys
import re 

phonebook= []
contact = {}
DataList={}
currentPhonebook= None
DataList = {currentPhonebook:contact}
mail_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_regex=r'^01[0125][0-9]{8}$'



def displayContact():
    # print("Name\t\tNumber\tEmail")
    # for key in contact:
        # print("{}\t\t{}".format(key,contact.get(key)))
    global currentPhonebook
    global DataList
    print ("Select phonebook first\n")
    selectPhonebook()
    Name =input("Enter the name: ")
    detect =searchContact(Name)
    if detect != 0:
       print("Name: "+Name) 
       print("Number: "+DataList[currentPhonebook][Name]["Number"])
       print("Email: "+DataList[currentPhonebook][Name]["Email"])
    else:
        print("not found!")
#################################################################################
def createPhonebook():
    global DataList
    list1=list(DataList.keys())
   # for i in list1:
       #print(i,end=' ')
    namephonebook=input('Enter name of new phonebook:')
    if namephonebook in phonebook:
      print('\n Name already exists')
    else:
      #phonebook.append(namephonebook)
      DataList[namephonebook]={}
      #contact.append({})
#################################################################################
def addContact():
      global currentPhonebook
      global DataList
      buffer_info={}
    # if not currentPhonebook:
      # print("No phonebook exists, create one to proceed")
    # else:
      print ("Select phonebook first\n")
      selectPhonebook()
      f_mail=True
      f_num=True
      name = input("Enter the contact name: ")
      while(f_num):
        phone = input("Enter the mobile number ")
        if re.fullmatch(phone_regex, phone):
            f_num=False
        else :
            print("INVALID format for phone number")
      while(f_mail):
        mail = input("Enter the Email : ")
        if re.fullmatch(mail_regex, mail):
            f_mail=False
        else :
            print("INVALID format for email")    

      #Contact[name] = [phone,mail]
      buffer_info={"Number":phone,"Email":mail}
      DataList[currentPhonebook][name]=buffer_info
#################################################################################
def searchContact():
     global currentPhonebook
     global DataList
     print ("Select phonebook first\n")
     selectPhonebook()
     search_name =str(input("Enter the contact name "))
     if DataList[currentPhonebook].get(search_name) is not None:
     #if search_name in contact:
        print(search_name,"'s contact number is ",contact[search_name])
     else:
        print("Name is not found in contact book")
#################################################################################        
def editContact():
    f=1
    edit_contact = input("Enter the contact to be edited ")
    #   check if input in contact
    while f:
      c=input('\n \n1.For Number edit \n2.For Email edit \n3.Finished edit\nEnter your choice: ')
      if edit_contact in contact:
        if c=='1':
          phone = input('Enter the new phone ')
          contact[edit_contact]=phone
        elif c=='2':
          mail = input('Enter the new Email ')
          contact[edit_contact]=mail        
          print('contact updated')
          display_contact()
        elif c=='3':
          f=0
      else:
        print("Name is not found in contact book")
      # name = input("input the name: ")
      # deleteContact(name)
      # addContact()
#################################################################################
def deleteContact():
      global currentPhonebook
      global DataList
      if not currentPhonebook:
        print("No phonebook exists, create one to proceed")
      else:
        print ("Select phonebook first\n")
        selectPhonebook()      
        del_contact = input("Enter the contact to be deleted ")
        if del_contact in contact:
          confirm = input("Do you want to delete this contact y/n? ")
          if confirm =='y' or confirm =='Y':
              contact.pop(del_contact)
        else:
              print("Name is not found in contact book")
 #################################################################################           
def selectPhonebook():
      global currentPhonebook
      global DataList
      list1 = list(DataList.keys())
      # for i in list1:
        # print(i,end=' ')
      new_phone =input("Enter phone book name: ")
      currentPhonebook = new_phone
#################################################################################
def exitPhonebook():
      sys.exit('')
#################################################################################
def deletePhonebook():
      global currentPhonebook
      global DataList
      print ("Select phonebook first\n")
      selectPhonebook()
      del DataList[currentPhonebook] 

#################################################################################       
def main():
    print('***************************************************Phonebook************************************************************')
    while True:
      
      print("1.Create phonebook")
      print("2.select phonebook")
      print("3.Add new contact")
      print("4.Edit contact")
      print("5.Display contact")
      print("6.Search contact")
      print("7.Delete contact")
      print("8.Delete phonebook")
      print("9.exit")
      choice=input('Enter Your Choice: ')
      if choice == '1':
          createPhonebook()
      elif choice == '2':
           selectPhonebook()
      elif choice == '3':
            addContact()
      elif choice == '4':
            editContact()
      elif choice == '5':
             displayContact()
           
      elif choice == '6':
            searchContact()
      elif choice == '7':
            deleteContact()
      elif choice == '8':
            deletePhonebook()
      elif choice == '9':
            exitPhonebook()
            
            
            
            
            
if __name__ == '__main__':
  main()



