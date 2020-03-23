from time import time

a = time()
b = [i*2 for i in range(9999999)]
print("Temps d'execution du script : {} sec.".format((time() - a)))

