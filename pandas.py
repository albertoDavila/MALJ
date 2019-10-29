#ejercicio 1

mylist=list("abcdefghijklmnopqrstuvwxyz")
import pandas as pd 
ser = pd.Series(mylist)
ser

#ejercicio 2

mylist= [x for x in "abcdefg"]
myarr= list(range(0,len(mylist)))
ser=pd.DataFrame({"numeros":myarr, "letras":mylist})
ser


#ejercicio 3 

ser1= pd.Series([1,2,3,4,5])
ser2=pd.Series([4,5,6,7,8])
result = ser1.isin(ser2)
type(result)
ser1[~result]


#ejercicio 4

ser = np.random.randint(1,10,35)
ser.resize(7,5)
ser


#ejercicio 5 

line = pd.DataFrame(['how', 'to', 'kick', 'ass?'])
def capital(st):
    st = st.capitalize()
    return st
line.apply(lambda x: capital(x[0]),axis=1)

#ejercicio 6



