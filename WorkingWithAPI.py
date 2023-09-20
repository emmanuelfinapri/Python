import requests
try:
  # Function that runs a specific API link when the user's input is Y
  def Y_Input():
    while True:

      #API URL
      request_url = "https://api.adviceslip.com/advice/search/"
      
      keyword= input("what is the keyword you’re looking for? ")
      #Add the keyword to the API URL
      request_url = request_url + keyword
      # Get data from the web API
      response = requests.get(request_url)
      # Convert the JSON data object into a python-friendly format.
      data = response.json()

      #Checking if the "total_results" key is in the array
      if "total_results" in data:
        print("Awesome, so we found " + data["total_results"] + " keywords containing '"+  data["query"] + "' Which are:\n")
        num = 1
        for slip in data["slips"]:
          print(num, "."+ slip['advice'])
          num  = num + 1
        break
      else:
        print("\nSorry this keyword doesn’t exist in our pool. Try again")

  # Function that runs a specific API link when the user's input is N
  def N_Input():
    while True:
      request_url = "https://api.adviceslip.com/advice"
      # Get data from the web API
      response = requests.get(request_url)
      # Convert the JSON data object into a python-friendly format.
      data = response.json()
      print("\n",data['slip']['advice'])
      break

  # Quits the program when the user inputs "Q"
  def Q_Input():
    while True:
      print("Bye, see you next time")
      break

  #Welcome messge when the code is run
  print("Welcome here we have a bunch of advices for you but is there any keyword you’ll like to search from our pool or do you want any random advice?")

  print("\nType “Y or y” to input your keyword")
  print("Type “N or n” to get a random advice") 
  print("Type “Q or q” to end quit")
  
  user_input = input("\n")

  if user_input == "Y" or user_input == "y":
    Y_Input()
    
  elif user_input  == "N" or user_input == "n":
    N_Input()
    
  elif user_input == "Q" or user_input == "q":
    Q_Input()
    
  else:
    print("Invalid Input")

  
except Exception as error:
  print("\nOops there's an error")
  print("Error:", error)
