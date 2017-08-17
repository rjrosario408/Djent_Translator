# Djent_Translator
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx3Nq97IB_mCPko0rfpbJ_gjENdVLrHn-SkyHPL-japf_nZMKAjA)

Djent is a subgenre of metal music that's commonly joked about for having simple guitar tabs that consist of only 1's and 0's. Based on this joke, I decided to write a function that *translates* the tabs by treating it like binary and converting the binary to characters. 

The tabs aren't translated logically, so if you're looking for a deeper meaning to a Djent song then this isn't the right place. The process is done arbitrarily:
- Extract tabs 
- If a number is greater than 1, then convert it to binary without leading 0's. 
- Combine tabs into one string and then split into groups of 8.
- Convert each binary number into a character. 
