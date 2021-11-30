from kivy.app import App
from kivy.uix.widget import Widget
from kivy import Config
Config.set('graphics', 'multisamples', '0')
import cgi
import mysql.connector
 
#form=cgi.FieldStorage()


class LoginWindow(Widget):
    def login(self, *args):
        firstname = self.ids.firstname_input
        firstname_text = firstname.text

        lastname = self.ids.lastname_input
        lastname_text = lastname.text

        email = self.ids.email_input
        email_text = email.text

        passwde = self.ids.password_input
        password_text = passwde.text

        cpassword = self.ids.cpassword_input
        cpassword_text =cpassword.text
        
        print(firstname_text)
        print(password_text)
                            
        mydb = mysql.connector.connect(host = "localhost", user = "root",password = "",db = "adf_practical_10")
        c = mydb.cursor()
        print('database connected')
        
        sql_command = "INSERT INTO user ( firstname,lastname,email,password,confirmpassword) VALUES (%s,%s,%s,%s,%s)"
        values = (firstname_text,lastname_text,email_text,password_text,cpassword_text)
            
        c.execute(sql_command, values)	   

        mydb.commit()
        mydb.close()

class Practical_10(App):
    def build(self):
        return LoginWindow()


if __name__ == '__main__':
    Practical_10().run()
