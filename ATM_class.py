import sys
import time
import random
import datetime as date
import mysql.connector as sql



class Atm:
        def __init__(self):
                self.my_db = sql.connect(host = "localhost", user = "root", password = "", database = "atm_db")
                self.my_cursor = self.my_db.cursor()
                self.cardreader = "INSERT YOUR CARD "
                
                
                # self.my_cursor.execute("CREATE TABLE Transaction_History (COLUMN_ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100), Account_Number VARCHAR(10), PIN VARCHAR(4), Beneficiary_Name VARCHAR(100), Beneficiary_AccountNumber VARCHAR(10), Transaction_Type VARCHAR(100), Amount INT(12), DATE VARCHAR(50))")
                # self.my_cursor.execute("ALTER TABLE Transaction_History ADD COLUMN (PIN VARCHAR(4))")
                # self.my_cursor.execute("ALTER TABLE Transaction_History MODIFY COLUMN DATE VARCHAR(50) AFTER COLUMN_ID")
                # self.my_cursor.execute("DROP TABLE transfer_History, withdraw_History")
                # self.my_cursor.execute("SHOW DATABASES")

                # for x in self.my_cursor:
                #     print(x)
                
                
                self.displayscreen = ["WELCOME TO JAIZ BANK", "KINDLY TAKE YOUR CASH", "THANK YOU FOR BANKING WITH US", "WHAT OPERATION DO YOU WANT TO PERFORM? ", "Please wait while your transaction is processing"]
                self.receipt = "Take your receipt"
                self.cardDetails = {}
                user_card = self.cardDetails
                self.main_page()
        def main_page(self):
                print(self.displayscreen[0])
                print("""
                1. SIGNUP           2. SIGNIN           3. QUIT
                """)
                option = input(self.displayscreen[3])
                if option== "1": 
                        self.SIGNUP()
                elif option == "2":
                        self.SIGNIN()
                elif option== "3":
                        sys.exit()
                else:
                        print("Invalid input!!  Enter the suitable operation ")
                        self.main_page()
        def SIGNUP(self):
                user_name = input("Input your full name ")
                user_password = input("Input password ")
                confirmPassword = input("confirm password  ")
                
                if user_password != confirmPassword:
                        print("Password do not tally")
                        self.SIGNUP()
                else:
                        user_pin = input("Input a four digit pin\n")
                        user_phoneNumber = input("Input your phone number ")
                        Email = input("Email Address > ")
                        user_AccountNumber = random.randint(1000000000, 9999999999)
                        AccountBalance = 0
                        my_query = "INSERT INTO  customerDetails (FullName, Password, Pin, AccountNumber, AccountBalance, PhoneNumber, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        my_val = (user_name.upper(), user_password.lower(), user_pin, user_AccountNumber, AccountBalance, user_phoneNumber, Email.lower())
                        self.my_cursor.execute(my_query, my_val)
                        self.my_db.commit()
                        time.sleep(3)
                        print("Account created succesfully ")
                        print("YOUR ACCOUNT NUMBER > " + str(user_AccountNumber))
                        time.sleep(3)
                        self.main_page()


        def SIGNIN(self):
                
                try: 
                        global userDetails  
                        global userPin
                        userPin = input("Enter your PIN ")

                        myquery2 = "SELECT * FROM customerDetails WHERE PIN = %s"
                        val2 = (userPin,)
                        self.my_cursor.execute(myquery2, val2)
                        details = self.my_cursor.fetchall()
                        userDetails = {"FullName" : details[0][1], "Password" : details[0][2], "Pin" : details[0][3], "AccountNumber" : details[0][4], "AccountBalance" : details[0][5], "PhoneNumber" : details[0][6], "Email" : details[0][7]}
                        self.transaction()

        
                except IndexError:
                        print("INVALID PIN")
                        self.SIGNIN()
                
        def transaction(self):
                print("What transaction do you want to perform? ")
                print("""

                1. DEPOSIT            2. WITHDRAW                    3. TRANSFER 
                
                4. CHECK BALANCE      5. TRANSACTION HISTORY          6. LOG OUT
                """)
                user_response_trsn = int(input("INPUT THE TRANSACTION NUMBER "))
                if user_response_trsn == 1:
                        self.deposit()
                elif user_response_trsn == 2:
                        self.withdraw()
                elif user_response_trsn == 3:
                        self.transfer()
                elif user_response_trsn == 4:
                        self.check_balance()
                elif user_response_trsn == 5:
                        self.transactionHistory()
                elif user_response_trsn == 6:
                        self.main_page()
                else:
                        print("Invalid input " + "Enter correct transaction number ")
                        self.transaction()
        

        def deposit(self):
                
                global newBalance_Deposit
                print("Your Current Account Balance is " + str(userDetails.get("AccountBalance")))
                AmountDeposit = int(input("Amount to deposit in digit\n"))
                newBalance_Deposit = userDetails.get("AccountBalance") + AmountDeposit
                queryBalanceUpdate = "UPDATE customerDetails SET AccountBalance = %s WHERE PIN = %s"
                valBalanceUpdate = (newBalance_Deposit, userDetails.get("Pin"))
                self.my_cursor.execute(queryBalanceUpdate, valBalanceUpdate)
                self.my_db.commit()
                DepositDate = date.datetime.now()
                time.sleep(2)
                print("Transaction Successful")
                
                # DEPOSIT HISTORY
                my_query = "INSERT INTO  Transaction_History (Name, Account_Number, Beneficiary_Name, Beneficiary_AccountNumber, Transaction_Type, Amount, DATE, PIN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                my_val = (userDetails.get("FullName"), userDetails.get("AccountNumber"), "NULL", "NULL", "DEPOSIT",  AmountDeposit, DepositDate, userDetails.get("Pin")) 
                self.my_cursor.execute(my_query, my_val)
                self.my_db.commit()     

                    


                global deposit_receipt
                deposit_receipt = f'''
                Date: {DepositDate.date()}, {DepositDate.time()}
                Name: { userDetails.get("FullName")}
                Acccount_Number: {userDetails.get("AccountNumber")}
                Amount_Deposit: {AmountDeposit}
                Account_Balance: {newBalance_Deposit}
                '''
                        
                print("Do you want receipt? ")
                receipt_response = input("YES OR NO \n")
                if receipt_response.capitalize() == "Yes": 
                        print(deposit_receipt)
                        self.main_page()

                else:
                        print("Your new balance is " + str(newBalance_Deposit))
                        time.sleep(2)
                        print("Do you want to perform another transaction? ")
                        UserInput = input("YES OR NO? \n")
                        if UserInput.lower() == "yes":
                 
                                self.SIGNIN()
                        else:
                                self.main_page()
                
        

        def withdraw(self):
                 
                Amount_withdraw_List = [1000, 2000, 5000, 10000, 20000, 50000]
                print("""
                1. 1000             2. 2000            3. 5000
                        
                4. 10000            5. 20000            6. 50000
                        
                7. others           8. CANCEL
                """)
                print("Your Current Account Balance is " + str(userDetails.get("AccountBalance")))
                user_input = input("Amount to withdraw ? \n")
                numbers = ["1", "2", "3", "4", "5", "6","7", "8"]
                if user_input not in numbers:
                        print("INVALID INPUT")
                        self.withdraw()
                        
                if user_input == "7":
                        global newBalance
                        global Amount_withdraw_others
                        Amount_withdraw_others = int(input("Enter amount in digit\n"))

                        if Amount_withdraw_others <= userDetails.get("AccountBalance"):
                                newBalance = userDetails.get("AccountBalance") - Amount_withdraw_others
                                time.sleep(2)
                                print(self.displayscreen[4])

                                

                                WithdrawDate = date.datetime.now()
                                queryUpdate = "UPDATE customerDetails SET AccountBalance = %s WHERE PIN = %s"
                                valUpdate = (newBalance, userDetails.get("Pin")) 
                                self.my_cursor.execute(queryUpdate, valUpdate)
                                self.my_db.commit()


                                
                                time.sleep(2)
                                print("Transaction Succesfull")

                                # WITHDRAW HISTORY
                                my_query = "INSERT INTO  Transaction_History (Name, Account_Number, Beneficiary_Name, Beneficiary_AccountNumber, Transaction_Type, Amount, DATE, PIN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                                my_val = (userDetails.get("FullName"), userDetails.get("AccountNumber"), "NULL", "NULL", "WITHDRAW",  Amount_withdraw_others, WithdrawDate, userDetails.get("Pin")) 
                                self.my_cursor.execute(my_query, my_val)
                                self.my_db.commit()  
                                 

                                
                                print(self.displayscreen[1])
                                time.sleep(2)
                                print(self.displayscreen[2])

                                withdraw_receipt = f'''
                                Date: {WithdrawDate.date()}, {WithdrawDate.time()}
                                Name: { userDetails.get("FullName")}
                                Acccount_Number: {userDetails.get("AccountNumber")}
                                Amount_Withdraw: {Amount_withdraw_others}
                                Account_Balance: {newBalance}
                                '''
                                print("Do you want receipt? ")
                                receipt_response = input("YES OR NO \n")
                                if receipt_response.capitalize() == "Yes": 
                                        print(withdraw_receipt)
                                        print("Do you want to make another transaction? ")
                                else:
                                        print("Do you want to make another transaction? ")
                        
                                
                                User_Response = input("YES OR NO\n")
                                if User_Response.capitalize() == "Yes":
                                        self.SIGNIN()
                                else:
                                        print(self.displayscreen[2])
                                        print("logging out")
                                        self.main_page()
                                        
                        else:
                                print("INSUFFICIENT BALANCE")
                                self.withdraw()
                else:
                        Amount_withdraw = Amount_withdraw_List[int(user_input) - 1]
                        if Amount_withdraw <= userDetails.get("AccountBalance"):
                                newBalance = userDetails.get("AccountBalance") - Amount_withdraw
                                time.sleep(2)
                                print(self.displayscreen[4])
                                
                                queryUpdate = "UPDATE customerDetails SET AccountBalance = %s WHERE PIN = %s"
                                valUpdate = (newBalance, userDetails.get("Pin")) 
                                self.my_cursor.execute(queryUpdate, valUpdate)
                                self.my_db.commit()


                                
                                time.sleep(2)
                                print("Transaction Succesfull")
                                WithdrawDate_b = date.datetime.now()

                                # WITHDRAW HISTORY

                                my_query = "INSERT INTO  Transaction_History (Name, Account_Number, Beneficiary_Name, Beneficiary_AccountNumber, Transaction_Type, Amount, DATE, PIN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                                my_val = (userDetails.get("FullName"), userDetails.get("AccountNumber"), "NULL", "NULL", "WITHDRAW",  Amount_withdraw, WithdrawDate_b, userDetails.get("Pin")) 
                                self.my_cursor.execute(my_query, my_val)
                                self.my_db.commit()     

                                

                                print(self.displayscreen[1])
                                time.sleep(2)
                                print(self.displayscreen[2])

                                # global deposit_receipt

                                withdraw_receipt = f'''
                                Date: {WithdrawDate_b.date()}, {WithdrawDate_b.time()}
                                Name: { userDetails.get("FullName")}
                                Acccount_Number: {userDetails.get("AccountNumber")}
                                Amount_Withdraw: {Amount_withdraw}
                                Account_Balance: {newBalance}
                                '''
                                
                                print("Do you want receipt? ")
                                receipt_response = input("YES OR NO \n")
                                if receipt_response.capitalize() == "Yes": 
                                        print(withdraw_receipt)
                                        print("Do you want to make another transaction? ")
                                else:
                                        print("Do you want to make another transaction? ")
                        
                                
                                User_Response = input("YES OR NO\n")
                                if User_Response.capitalize() == "Yes":
                                        self.SIGNIN()
                                else:
                                        print(self.displayscreen[2])
                                        print("logging out")
                                        self.main_page()
                                
                        else:
                                print("INSUFFICIENT BALANCE")
                                self.withdraw()


                if user_input == "8":
                        self.transaction()


        def transfer(self):
                global userNewBalance
                recipientAccountNumber = input("Recipient Account Number >  ")
                AmountTransfer = int(input("Enter amount in digit "))
                time.sleep(2)
                print("Are you sure you want to send " + str(AmountTransfer) + "  to  " + str(recipientAccountNumber))
                print("""
                1. Send
                2. Make changes
                """)
                print(userDetails.get("AccountBalance"))
                user_response_transfer = input("Enter suitable operation >\n")
                if user_response_transfer == "1":
                        if AmountTransfer <= userDetails.get("AccountBalance"):
                                userNewBalance = userDetails.get("AccountBalance") - AmountTransfer
                                print(userNewBalance)
                                queryRecipientAccountBalance = "SELECT AccountBalance, FullName FROM customerDetails WHERE AccountNumber = %s"
                                valRecipientAccountBalance = (recipientAccountNumber, )
                                self.my_cursor.execute(queryRecipientAccountBalance, valRecipientAccountBalance)
                                recipientDetails = self.my_cursor.fetchall()
                                recipientNewAccountBalance = recipientDetails[0][0] + AmountTransfer

                                queryRecipientAccountBalanceUpdate = "UPDATE customerDetails SET AccountBalance = %s WHERE AccountNumber = %s"
                                valRecipientAccountBalanceUpdate = (recipientNewAccountBalance,  recipientAccountNumber )
                                self.my_cursor.execute(queryRecipientAccountBalanceUpdate, valRecipientAccountBalanceUpdate)
                                self.my_db.commit()

                                print(self.displayscreen[4])
                                time.sleep(2)
                                print("Transaction Successful")

                                transfer_date = date.datetime.now()

                                queryUserAccountBalanceUpdate = "UPDATE customerDetails SET AccountBalance = %s WHERE PIN = %s"
                                valUserAccountBalanceUpdate = (userNewBalance, userDetails.get("Pin"))
                                self.my_cursor.execute(queryUserAccountBalanceUpdate, valUserAccountBalanceUpdate)
                                self.my_db.commit()

                                # TRANSFER HISTORY

                                my_query = "INSERT INTO  Transaction_History (Name, Account_Number, Beneficiary_Name, Beneficiary_AccountNumber, Transaction_Type, Amount, DATE, PIN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                                my_val = (userDetails.get("FullName"), userDetails.get("AccountNumber"), recipientDetails[0][1], recipientAccountNumber, "TRANSFER",  AmountTransfer, transfer_date, userDetails.get("Pin")) 
                                self.my_cursor.execute(my_query, my_val)
                                self.my_db.commit()  
                                
                                

                                Transfer_receipt = f'''
                                Date: {transfer_date.date()}, {transfer_date.time()}
                                Name: { userDetails.get("FullName")}
                                Acccount_Number: {userDetails.get("AccountNumber")}
                                Recipient_Name: {recipientDetails[0][1]}
                                Recipient_Account_Number: {recipientAccountNumber}
                                Amount_Transfer: {AmountTransfer}
                                Account_Balance: {userNewBalance}
                                '''
                                
                                
                                print("Do you want receipt? ")
                                receipt_response = input("YES OR NO \n")
                                if receipt_response.capitalize() == "Yes": 
                                        print(Transfer_receipt)
                                        print("Do you want to make another transaction? ")
                                else:
                                        print("Your New Balance is " + str(userNewBalance))

                                        print("Do you want to make another transaction? ")

                                
                                User_Response = input("YES OR NO\n")
                                if User_Response.capitalize() == "Yes":
                                        self.SIGNIN()
                                else:
                                        print(self.displayscreen[2])
                                        print("logging out")
                                        self.main_page()
                        
                        else:
                                print("INSUFFICIENT BALANCE")
                                print("Your Account Balance is " + str(userDetails.get("AccountBalance")))

                                print("""
                                    1. BACK         2. Deposit          3. LOG OUT 
                                """)
                                User_response = input("Enter suitable operation\n")
                                if User_response == "1":
                                        self.transfer()
                                elif User_response == "2":
                                        self.deposit()
                                else:
                                        self.main_page()

                else:
                        self.transfer()


        def check_balance(self):
                print("Your Current Account Balance is " + str(userDetails.get("AccountBalance")))
                print("Do you want to make transaction? ")
                                
                User_Response = input("YES OR NO\n")
                if User_Response.capitalize() == "Yes":
                        self.transaction()
                else:
                        print(self.displayscreen[2])
                        print("logging out")
                        self.main_page()

                   
        def transactionHistory(self):
                print("""
                1. DEPOSIT HISTORY       2. WITHDRAW HISTORY     3. TRANSFER HISTORY
                
                """)

                User_input = input("Enter Suitable Transaction\n")
                if User_input == "1":
                        query = "SELECT Name, Account_Number, Amount, DATE FROM Transaction_History WHERE PIN = %s AND Transaction_Type = %s"
                        val = (userDetails.get("Pin"), "DEPOSIT")
                        self.my_cursor.execute(query, val)
                        myHistory_Deposit = self.my_cursor.fetchall()
                        print(myHistory_Deposit)
                        self.transaction()
                elif User_input == "2":
                        query = "SELECT Name, Account_Number, Amount, DATE FROM Transaction_History WHERE PIN = %s AND Transaction_Type = %s"
                        val = (userDetails.get("Pin"), "WITHDRAW")
                        self.my_cursor.execute(query, val)
                        myHistory_withdtraw = self.my_cursor.fetchall()
                        print(myHistory_withdtraw)
                        self.transaction()
                elif User_input == "3":
                        query = "SELECT Name, Account_Number, Amount, DATE FROM Transaction_History WHERE PIN = %s AND Transaction_Type = %s"
                        val = (userDetails.get("Pin"),"TRANSFER")
                        self.my_cursor.execute(query, val)
                        myHistory_transfer = self.my_cursor.fetchall()
                        print(myHistory_transfer)
                        self.transaction()


start = Atm()
