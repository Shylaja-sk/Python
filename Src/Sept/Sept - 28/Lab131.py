''''### **JSON Basics**
- Full Form  - Javascript Object Notation.
- JSON is a **text format **for storing and transporting data
- A key and Value Pair. -
- JSON Object  - {}
- JSON Arrays -  []
- Rule Value
    - Data Types
        - String
        - Number
        - Boolean
        - Null
        - Arrays
        - Object
- Rule - Keys
    - " " - IN JSON
    - String
    - can't be other data type
    - unique
- Simple -
{

"name" : "Pramod"

}




```
{
 "name" : "Pramod",
 "age" : 12.45,
 "isMale" : true,
 "audi" : null,
 "address" : {
   "home" : "delhi",
   "office" : "KA"
 },
 "phone" : ["976543210","987654321","976567898"]
}
```
https://jsoncrack.com/editor --- to write code
----------------------------------------------------------------------------------------------------------------------------

PUT

1. Update with complete replace.
2. It required ID or endpint where we need to update.
```
{
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : true,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
```
Patch

1. Partial Update
2.
```
{
    "firstname" : "Pramod",
    "lastname" : "Brown"
}
```
POST- universal method - cant be use as GET, POST, PATHC, PUT, DELETE.

option - check which http method this url supports.



- HTTP Methods - Rules which are given to you for best practice.
- Gun AK 47
    - Save
    - Kill other



'''