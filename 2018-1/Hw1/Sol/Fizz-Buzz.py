

for i in range(1,101):
    
    # Condicion para Fizz
    fizz = i%3 == 0
    # Condicion para Buzz
    buzz = (i%7 == 0) or ('7' in str(i))
    
    # Si se cumplen ambas entonces es Fizz-Buzz
    if( fizz and buzz ):
        print "Fizz-Buzz"
    # A partir de ahora sabemos que AL MENOS UNA de las condiciones es falsa
    
    # Si se cumple fizz, entonces no se cumple buzz
    elif(fizz):
        print "Fizz"
    
    # A partir de ahora sabemos que NO se cumple fizz
    
    # Si se cumple buzz, es buzz
    elif(buzz):
        print "Buzz"
        
    # A partir de ahora sabemos que NO se cumple Fizz NI Buzz
    else:
        print i
