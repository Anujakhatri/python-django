while True:
   print("1. BMI calculator ")
   print("2. Taxation system ")
   print("3. Currency converter ")
   print("4. Remittance calculator ")
   print("5. Lagani Kosh")
   print("6. Invalid")

   choice = input("Enter your choice: ")
   
   if choice == "1":
       print("BMI calculator : https://github.com/bidhyabhattarai/BMI_calculator")
   elif choice == "2":
       print("Taxation system : https://github.com/Anujakhatri/Taxation-system-nepal")
   elif choice == "3":
       print("Currency converter: https://github.com/sneharitas/currency_converter")
   elif choice == "4":
       print("Remittance calculator: https://github.com/binisha77/nepal_remittance_calculator")
   elif choice == "5":
       print("Lagani Kosh: https://github.com/kopiladevkota/nepal_lagani_kosh")
   elif choice == "6":
       print("Invalid")
       break
   else:
       print("Invalid choice")