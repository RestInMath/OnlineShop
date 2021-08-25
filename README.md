# Online Shop
> Online shop microservice    

Technology stack:   
-Python   
-Flask    
-MongoDB    

# Installation
Microservice requires Flask, PyMongo, Flask-Pymongo modules   

Install the dependencies
```
pip install -r requirements.txt
```   
    
# Run   
``` 
python __init__.py
```
    
# Supported operations using curl
### *Get all product names*    
curl -X GET http://localhost:5000/    
    
### *Get product names by name or description*      
*Linux*       
curl -X GET http://localhost:5000/ -d "{"name":*product_name*}"   
curl -X GET http://localhost:5000/ -d "{"description":*some_words*}"   
*Windows*     
curl -X GET http://localhost:5000/ -d "{\\"name\\":*product_name*}"     
curl -X GET http://localhost:5000/ -d "{\\"description\\":*some_words*}"   

### *Get product names by parameter*      
*Linux*       
curl -X GET http://localhost:5000/ -d "{"parameters":{*parameter_name*:*parameter_value*}}"      
*Windows*     
curl -X GET http://localhost:5000/ -d "{\\"parameters\\":{*parameter_name*:*parameter_value*}}"   


### *Create new product*   
Linux       
curl -X POST http://localhost:5000/add -d "{"name":*product_name*,"description":*product_description*, "parameters":{*parameter_name*:*parameter_value*}}"   
Windows     
curl -X POST http://localhost:5000/add -d "{\\"name\\":*product_name*,\\"description\\":*product_description*, \\"parameters\\":{*parameter_name*:*parameter_value*}}"     

### *Get product details by id*    
*Linux*     
curl -X GET http://localhost:5000/details -d "{"id":*number*}"      
*Windows*       
curl -X GET http://localhost:5000/details -d "{\\"id\\":*number*}"