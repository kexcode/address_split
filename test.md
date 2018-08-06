# [001] : Testing an address line splitting function

## Description

The function **address_split(str)**, from the module **addsplit.py** is written on Python 2.7. It takes the string of an address and splits it on separate fields: street name and street number.
It is also provided an input file with typical address lines, including difficult cases, and the **main.py** script for a test.

**( street , house ) = address_split( address )**

   **Input:** string of address
   
   **Output:** string of street and string of street-number

### Precondition

* Python 2.7 compiler

### Assumptions

It is assumed that the address format is divided in 3 types: 
1. simple case 
    * `"Winterallee 3a"` -> `{"Winterallee", "3a"}`
2. long names / special characters / complex number
    * `"Auf der Vogelwiese 23 b"` -> `{"Auf der Vogelwiese", "23 b"}`
3. complex cases / other countries
    * `"4, rue de la revolution"` -> `{"rue de la revolution", "4"}`
    * `"200 Broadway Av"` -> `{"Broadway Av", "200"}`
    * `"Calle Aduana, 29"` -> `{"Calle Aduana", "29"}`
    * `"Calle 39 No 1540"` -> `{"Calle 39", "No 1540"}`

## Test Steps

1. Download all files into test directory
2. Run the *main.py* script in the python console
It will feed a number of cases from *input.txt* to the **address_split()** function
3. Visually compare results with the expected behaviour
4. Modify the *input.txt* file for testing other cases

## Expected Result

* `Address: Winterallee 3`               
    * `Str: Winterallee 	        House: 3`
* `Address: Musterstrasse 45`            
    * `Str: Musterstrasse 	        House: 45`
* `Address: Blaufeldweg 123/B`           
    * `Str: Blaufeldweg 	        House: 123/B`
* `Address: Am Bächle 23`                
    * `Str: Am Bächle 	            House: 23`
* `Address: Am Bächle 23-25`             
    * `Str: Am Bächle 	            House: 23-25`
* `Address: Auf der Vogelwiese 23 b`	    
    * `Str: Auf der Vogelwiese 	House: 23 b`
* `Address: Auf der Vogelwiese 23-b`    	
    * `Str: Auf der Vogelwiese 	House: 23-b`
* `Address: 4, rue de la revolution`    	
    * `Str: rue de la revolution 	House: 4`
* `Address: 200 Broadway Av`             
    * `Str: Broadway Av 	        House: 200`
* `Address: Calle Aduana, 29`          	
    * `Str: Calle Aduana 	        House: 29`
* `Address: Calle 39, 156`      	        
    * `Str: Calle 39 	            House: 156`
* `Address: Calle 39 No 1540` 	        
    * `Str: Calle 39 	            House: No 1540`
