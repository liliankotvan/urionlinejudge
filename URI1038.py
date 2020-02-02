x, y = map(int, raw_input().split(" "))

dictionary = {1: 4.0,
              2: 4.5,
              3: 5.0,
              4: 2.0,
              5: 1.5
              }

if x in dictionary.keys():

    resultado = dictionary.get(x) * y

    print ("Total: R$ {:.2f}".format(resultado))