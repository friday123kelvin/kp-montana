from mirabank.index import MiraBank
from Transactions.gethelp import Kp_montana

class ServiceManager:
    def __init__(self):
        self.mira_bank = MiraBank()
        self.kpmontana = Kp_montana()  

    def run(self):
        while True:
            print('Hello welcome to mi-global network. What service would you like to use?')
            print('1. Mirabank\n7. kp_montana\n8. Exit')
            choice = input("Choose 1/7/8: ")
            
            if choice == "1":
                self.mira_bank.run()
            elif choice == "7":
                self.kpmontana.run()
            elif choice == "8":
                print("Thank you for choosing our services")
                break
            else:
                print("Invalid choice. Please try again.")

main = ServiceManager()
main.run()
