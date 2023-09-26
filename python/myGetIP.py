def getHostnameByIP(h):
    try:

        hostname = str(h)
    
    except:
        ip = socket.gethostbyname(hostname)
        print (hostname +' has an ip of' + ip)

    print("Oops, something is wrong with that host")
