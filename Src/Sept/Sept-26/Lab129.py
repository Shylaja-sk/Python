'''
## Project #2 - Restful Booker APIs
Objective -
Booking APIs
Create a booking
Update (Put, patch)
Get a Booking and
Delete Booking.

Makemytrip -> Create Booking

URL

restful-booker.herokuapp.com/apidoc/index.html](https://restful-booker.herokuapp.com/apidoc/index.html)

## How to Test the Rest APIs?
1. API Documentation -
    1.  restful-booker.herokuapp.com/apidoc/index.html](https://restful-booker.herokuapp.com/apidoc/index.html)
    2. Google DOC
    3. Confluence
    4  docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#update-a-repository](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#update-a-repository)
    5. Postman Documentation  - apidocs.imgur.com/#de179b6a-3eda-4406-a8d7-1fb06c17cb9c](https://apidocs.imgur.com/#de179b6a-3eda-4406-a8d7-1fb06c17cb9c)
    6. Swagger api  - httpbin.org/#/Auth  (https://httpbin.org/#/Auth)
2. **No API Documentation**.
    1. UI -> (Curl , UI, Asking) - Create your Own High Requirement)
    2. No UI -> docs.google.com/document/d/1y7WNwcdRfEo0q4jNBKy9U_z8i9mx7i6l/edit?usp=sharing&ouid=104755920778477387077&rtpof=true&sd=true](https://docs.google.com/document/d/1y7WNwcdRfEo0q4jNBKy9U_z8i9mx7i6l/edit?usp=sharing&ouid=104755920778477387077&rtpof=true&sd=true)


**Request - ** we need below basic things

1. Base URL -
2. QP /PP :** **
3. Header -
4. Cookie - **NA**
5. Auth -** NA**
6. Payload or Body - XML


**Response**

1. Response
2. Status Code
3. Headers, Cookie


### **Test Plan ( QA Lead)**
Template -

docs.google.com/document/d/1UO54JPp_kVC-dQVCzek6F1aD76bxEX_p/edit?usp=sharing&ouid=104755920778477387077&rtpof=true&sd=true](https://docs.google.com/document/d/1UO54JPp_kVC-dQVCzek6F1aD76bxEX_p/edit?usp=sharing&ouid=104755920778477387077&rtpof=true&sd=true)



### **Test cases ( Step by Step Instructions) **
docs.google.com/spreadsheets/d/1EH1UJ9Qezgx_aZ0xim3KcVJUCEeR7A-7/edit?usp=sharing&ouid=104755920778477387077&rtpof=true&sd=true](https://docs.google.com/spreadsheets/d/1EH1UJ9Qezgx_aZ0xim3KcVJUCEeR7A-7/edit?usp=sharing&ouid=104755920778477387077&rtpof=true&sd=true)

1. Positives
2. Negative


### LIVE Restful Booker
**Functionality** -

1. Create a Booking - POST
2. Fetch a Booking
    1. Fetch all the Booking - Get All
    2. Fetch Single boooking - Get
3. Update A Booking
    1. Update partially - Patch
    2. Update fully PUT
4. Delete a booking.


Create Token (Endpoint Authorization) -
Updation and Delete ->
Secure APIs endpoints - if you have token then you are allowed perform updation, deletion.


Curl - common line tool and library
without documentation
Go to - https://app.vwo.com/#/login
right click - inspect
Network
click on login
in network tab - right click on Login and copy as Curl
and paste it in the project by importing it
'''