"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.


# --- Functions --- #
# Build out the required functions for your program.

class Email():
    
    def __init__(self, email_address, subject_line,  email_content, has_been_read = False):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = has_been_read
        

    def  mark_as_read(self):
        self.has_been_read = True



def populate_inbox():
    # Create 3 sample emails and add it to the inbox list.
    inbox.append(Email("admin@cogrammar.com", "Welcome to HyperionDev!", "we are thilled to have you on board"))  
    inbox.append(Email("admin@cogrammar.com", "Great work on the bootcamp!", "great progress keep going")) 
    inbox.append(Email("admin@cogrammar.com", "Your excellent marks!", "Congratualtions-you have scored 98%"))   
    

def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index, Email in enumerate(inbox):
        print(str(index) + " " + Email.subject_line)


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
        email = inbox[index] # inbox has connection to class name Email via the populate_inbox class function.
        try: 
            print(f'Email address from: {email.email_address}')
            print(f'Email subject is: {email.subject_line}')
            print(f'Email content is: {email.email_content}')
            email.mark_as_read() # call the mark_as_read() function to set email to it has been read now.

        except IndexError: # incase user enters an email index that doesn't exist
            print("\nInvalid option selected!")


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.

    # build a new tuple shaped list for not read yet emails.
    unread = [(i,email) 
              for i, email in enumerate(inbox) # inbox is a list so it has index and actual value fields
                if email.has_been_read == False # email not read yet, then add the email to unread list
                ]
    
    # Iterate through the inbox and check if an email has not been read
    if unread !=[]:
        for i, email in unread: # loop through the tuple list of unread emails
            print(f"{i}. {email.subject_line} <--this email is not read yet")  # Print email index and it's subject similar to list_emails function
        
    
    else:
        print("\n all email has already been read.")  # to show that all emails have been read already


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox=[]

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox()


# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
         # Add logic here to read an email
        list_emails()
        selection = int(input("Enter the corresponding email index number to read the email full details: "))
        read_email(selection)
        

    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()

    elif user_choice == 3:
        break

    else:
        print("Oops - incorrect input.")
