Esa-Tracker
===========

This is a site to allow you to send requests to, as well as recieve and display the data sent in return from the satellite buoy, all from the same page, meaning you don't need to go to the rockblock website to send or recieve messages.

  I used flask python web framework to create the site, which allowed my to use python to generate a page and get and send data to the rockblock site.


HexToFloat(*class*)
-------------------

Converts hex data into floating point number

#### Parameters:
##### hex: str
  A section of the string of hex data recieved from the rockblock servers as specified by ParseFromHex()

#### Returns:
  A floating point number converted to decimal

crc8(*class*)
-------------

Generates a CRC value of the string being passed into it

#### Parameters:
##### msg: str
  A string of hex data, either generated locally, or on the module

#### Returns:
  Crc value as a hex integer

ParseFromHex(*class*)
---------------------

Parses the data recieved from the module and converts it into a readable form

#### Parameters:
##### data: str
  A string of hex data from the module

#### Returns:
  Readable form of the revieved data

ParseToHex(*class*)
-------------------

Generates data, containing unused filler data to get the string to be at least 31 bytes in length, to send  to send to the module, requesting to have data sent back in return

#### Parameter:
##### msgtype: int
  Integer dictating whether you are requesting data or sending an acknowledgement
##### Unstructured: str
  String to be sent to the module
  
#### Returns:
  Hex string to be sent to module
  
Index(*function*)
-----------------

  Generates the main page of the site, and displays the recieved data if there is any.  It also creates a new message to send to the module

GetData(*function*)
--------------------

  Checks where the post request is aimed towards, as indicated by the filler data, and either displays it, or sends it to the rockblock       servers to be sent to the module

___
Notes
---

  I couldn't figure out a way to send post data 3 times automatically, so I instead added:</br>
  ```
  return '''<h1>sending</h1><br><br>please refresh and resend twice then click <a href=http://esa-tracker.herokuapp.com/>here</a>'''
  ```
  on line 239, which brings you to another page and everytime you refresh it prompts you to re-send the post request
