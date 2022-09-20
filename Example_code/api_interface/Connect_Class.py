#This is refactored code based on Stanley's Connect.py which demonstrates
#the advantages of class based programming. 

import requests


class SensApiInterface():
    
    #Macros
    #I can define constants which I call "Macros" in my class so
    #that I know I am working with a variable of that class. 
    #I can use these macros later on in my code. 
    apiAntPower = "/stapi/v0/ant/pwr"
    apiAntSequence = "/stapi/v0/ant/seq"
    apiEpicConfig = "/stapi/v0/epic"

    #----------------- constructors ----------------------
    #An advantage of classes is I can run constructor methods.
    #For example I know my header will always be the same format, 
    #So I can have a class based method to construct it for me with
    #The API key. I can also make a function that returns the endpoint
    #With a given key.
    def __init__(self,url,key,retries=3):
        self.apiKey = key
        self.baseUrl = url
        self.retries = retries
        self.header = self.constructHeader()

    def constructHeader(self):
        header = {
            'Authorization' : 'Bearer ' + self.apiKey, 
            'Content-Type'  : 'application/json;charset=utf-8'
        }
        return header

    def constructEndpoint(self,apiDestination):
        return self.baseUrl + apiDestination

    #----------------- constructors ----------------------

    #----------------- functions -------------------------
    #Another advantage of classes is I can create functions that 
    #I don't need to pass data into. I can have the class keep a track
    #of things like "headers" and Base API urls. Once I have set it up
    #It lowers the amount of work and complexity compared to function based
    #programming. In your other code you need to put in the base url and headers 
    #every time. check if __name__ == "__main__" for examples.
    def apiGetRequest(self,destination):

        #This will genereate an enpoint based on the given destination
        #I.E parsing Api antenna power will return "http://192.xxx.xxx.xxx/stapi/v0/ant/pwr"
        endpoint = SensApiInterface.constructEndpoint(destination)
        
        #try until max retries
        for i in range(self.retries): 
            r = requests.get(endpoint,header = self.header)
            if r.status_code == 200: 
                print("Connected")
                return r
        
        print("Failed to read RFID")
        return r
    
    #Here I can construct a class function that lets me use the same
    #methods for all get requests. This reduces workload and complexity.
    #Since these are all get requests, I can return the information raw, 
    #But i can also build decoders and data processing for each method in the
    #future if required. 
    def getPowerInfo(self):
        return self.apiGetRequest(SensApiInterface.apiAntPower)
    
    def getEpicInfo(self):
        return self.apiGetRequest(SensApiInterface.apiEpicConfig)

    def getAntSequence(self):
        return self.apiGetRequest(SensApiInterface.apiAntSequence)
        
    #----------------- functions -------------------------
    

if __name__ == "__main__":

    api_key = 21600019
    api_base_url = "http://192.168.0.41"

    #After setting this up, it will call the init method which will construct
    #My header. 
    reader = SensApiInterface(api_base_url,api_key)

    #Now to get the power diagnostics I can run the .getPowerInfo Function
    powerInfo = reader.getPowerInfo()
    epicInfo = reader.getEpicInfo()
    antennaSeq = reader.getAntSequence()

    #------------------------------------------------------

    #Advantage of class based programming is that I can create a new instance
    #Of the sensApiInterface easily with different parameters for example if
    #we connect 2 sensors to the network

    api_key_2 = 123456788
    api_base_url = "http://192.168.0.1"

    #Like with API reader 1, now that I have defined my constructor 
    #method, it will automatically generate the header, and my endpoints
    #I can call all the methods.
    reader2 = SensApiInterface(api_key_2,api_base_url)

    #I can also get the information very easily with the Same methods without
    #needing to change anything.
    powerInfo2 = reader2.getPowerInfo()
