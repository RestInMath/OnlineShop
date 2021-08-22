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
-*Get all product names*    
curl -X GET http://localhost:5000/    
    
-*Get product names filtered by parameter*    
curl -X GET http://localhost:5000/ -d "{"name":*product_name*}"   
    
-*Create new product*   
curl -X POST http://localhost:5000/add -d "{"name":*product_name*,"description":*product_description*}"   
    
-*Get product details by id*    
curl -X GET http://localhost:5000/details -d "{"id":*number*}"    
