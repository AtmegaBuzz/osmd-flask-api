<p><img src="https://raw.githubusercontent.com/AtmegaBuzz/osmd/main/screenshots/logo.jpeg" alt="logo" width="20%" /></p>

# OSMD (One Source Multiple Destination) Flask-Apis

Note: Depricated project <br/>
project is migrated to Django https://github.com/AtmegaBuzz/osmd.git


- [About Project](#About-Project)

- [Working](#Working)
  - [Register](#Register)
  - [Login](#Login)
  - [Booking Cab](#Booking-Cab)
  - [Your Bookings](#Your-Bookings)

- [Getting Started](#Getting-Started)
  - [How to Add Google Maps Api](#oogle-api)
  - [Setup And Run the Application](#run)




<a id="About-Project"></a>

# OSMD Cab Infrastructure

One Source, Multiple Destination Cab App, is a cab app Website that focuses on optimizing the approach of booking shared from a single source.

We target organizations such as large MNC offices, Schools, or prominent gathering places, which are handled by an organization that has many individuals and wants to implement their own cab services.

This Idea focuses on providing the common Open-Source Infrastructure to the Organizations to implement their own software in delivering the cab services. 

<a id="Working"></a>

# How it Works
```This Algorithm for this app is created by NSIT Last year student colaborated with Swapnil Shinde for Implementation. Last year project NSIT```
1.It Is based on Bellman Ford algorith for shortest path | One source Multiple destination.
2.This app takes the Const Starting point which will be same for all users , it can be a organisation or a school.
3.then it optimises the path for one source to multiple destination

<a id="Register"></a>

# Resgiter 
```{{BASE_URL}}/register```

### example request
```
POST /login HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Content-Length: 78

{
    "username":"text",
    "email":"test@gmail.com",
    "password":"text"
}
```
### response 

```
{"message":"register successfully"}
```
<a id="Login"></a>

# Login
```{{BASE_URL}}/login```

### example request
```
POST /login HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Content-Length: 78

{
    "username":"text",
    "email":"test@gmail.com",
    "password":"text"
}
```
### response 

```
{"api_key":"Ax38fjdsa9ff72k2;"}
```





<a id="Booking-Cab"></a>

# Booking Cab
```{{BASE_URL}}/bookcab```


### example request
```
POST /login HTTP/1.1
Host: 127.0.0.1:5000
api_key: 23fasdf0sdf8asj
Content-Type: text/plain
Content-Length: 73

{
    "destination":"punjab",
    "datetime":2021-06-25 07:58:56.550604
}
```
### response 

```
{"booking":"booking added to the queue"}
```


<a id="Your-Bookings"></a>

# Your Bookings 
```{{BASE_URL}}/listbookings```

### example request
```
POST /login HTTP/1.1
Host: 127.0.0.1:5000
api_key: 23fasdf0sdf8asj
```

<a id="Getting-Started"></a>

## Getting Started

<a id="google-api"></a>

#### Add google maps API.

 - go to google developer console and enable and generate your own Google Maps Api
 - add the api to .env file. 


#### Setup and Run the Application
 - ```pip install requirements.txt``` 
 - ```export FLASK_APP=server.py```
 - ```flask db init``
 - ```flask db migrate -m "initial migration"```
 - ```python server.py"```

