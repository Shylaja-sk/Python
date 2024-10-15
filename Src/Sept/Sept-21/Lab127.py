'''


URL - https://www.dataaccess.com/webservicesserver/numberconversion.wso?op=NumberToWords

(https://www.dataaccess.com/webservicesserver/NumberConversion.wso)

Project #1 - Objective :

- **Returns the word** corresponding to the **positive number passed** as parameter. Limited to quadrillions.
if we pass 100 -> Hundred should display
 , 500 -> Five hundred ,
 1337 -> One thousand, three hundred and thirty seven.

API Testing - we requuired below items

**Request**

1. Base URL - www.dataaccess.com**](https://www.dataaccess.com/)** **
2. QP /PP :** /webservicesserver/NumberConversion.wso**
3. Header - **Content-Type - application soap/xml**
4. Cookie - **NA**
5. Auth -** NA**
6. Payload or Body - XML
    1. message is wrapped in a **SOAP envelope**
    2. <?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>unsignedLong</ubiNum>
    </NumberToWords>
  </soap12:Body>
</soap12:Envelope>`
7. HTTP method - **POST**


**Response**



1. Response Body verification
```
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Body>
        <m:NumberToWordsResponse xmlns:m="http://www.dataaccess.com/webservicesserver/">
            <m:NumberToWordsResult>one hundred </m:NumberToWordsResult>
        </m:NumberToWordsResponse>
    </soap:Body>
</soap:Envelope>
```




1. Status Code - 200 Ok
2. Response Body verification
3. Time validation | 1480 ms
4. Response Headers |  Same headers are coming verify



Testcases:
1. Verify that with the valid data send to the API request -
    1. Expected Result  - Status Code - 200 Ok
    2. Actual Result - 200 Ok
2. Verify that with the valid data send to the API request Body is coming with the correct Data. (Number to Conversion is performed)
3. Verify that with the **http** URL data send to the API request Body is coming with the correct Data.  -
    1. Expected Result -> 200 Ok, number (Number to Conversion is performed)
    2. Actual Result -> HTML page is coming, HTTP is not supported - Bug.
4. Verify that with the URL data - 1send to the API request Body is coming with the correct Data.  -
    1. Expected Result -> 200 Ok, number (Number to Conversion is performed)
    2. Actual Result -> 200 Ok but error message - number to large.


- -1
- pramod
- pramod123
- !@#$%^%$
- 123pramod
- 0
- blank
- null
- 98765432345678987654345678
- %%%pramod%%
- 12.34
- 0x0876567
- PRAMOD
- وتتحمّل والكوري ف
𡨸




SOAP UI -Install

'''