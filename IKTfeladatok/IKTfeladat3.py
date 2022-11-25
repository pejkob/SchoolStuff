szoveg=input('Adjon meg egy szöveget! ')
maganhangzok=['a','á','e','é','i','í','o','ó','u','ú','ü','ű','ö','ő']
result=''
for letter in szoveg:
    result+=letter
    if letter  in maganhangzok:
        result+='v'+letter

print(result)