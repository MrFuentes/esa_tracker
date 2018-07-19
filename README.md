# Esa-Tracker
Site used to monitor data from ,and send requests to, the sensor buoy

HexToFloat (*class*)
-------------------

Converts hex data into floating point number

#### Parameters:
##### hex : str
  A section of the string of hex data recieved from the rockblock servers as specified by ParseFromHex()

#### Returns:
  A floating point number converted to decimal

crc8(*class*)
-------------

Generates a CRC value of the string being passed into it

#### Parameters:
##### msg : str
  A string of hex data, either generated locally, or on the module

#### Returns:
  Crc value as a hex integer

ParseFromHex(*class*)
---------------------

#### Parameters:
##### data : str
  A string of hex data from the module

#### Returns:
  Readable form of the revieved data
