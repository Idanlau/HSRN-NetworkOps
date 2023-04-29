def pingit():                               # defining function for later use

    s = socket(AF_INET, SOCK_STREAM)         # Creates socket
    host = 'localhost' # Enter the IP of the workstation here 
    port = 80                # Select port which should be pinged

    try:
        s.connect((host, port))    # tries to connect to the host
    except ConnectionRefusedError: # if failed to connect
        print("Server offline")    # it prints that server is offline
        s.close()                  #closes socket, so it can be re-used
        pingit()                   # restarts whole process    

    while True:                    #If connected to host
        print("Connected!")        # prints message 
        s.close()                  # closes socket just in case
        exit()                     # exits program

pingit()               
