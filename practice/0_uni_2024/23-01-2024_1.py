import matplotlib.pyplot as pl
import numpy as np
over = np.arange(1.0,6.0,1.0)
Ind = [10,3,14,15,4]
nz = [4,9,3,8,10]
pl.title("Ind v/s Nz")
pl.bar(over,Ind,color='b',width=0.25,label='India')
pl.bar(over+0.25,nz,color='r',width=0.25,label='Newzeland')
pl.legend(loc='upper left')
pl.xlabel("Over")
pl.ylabel("Run")
pl.show()




# import matplotlib.pyplot as pl
# import numpy as np
# over = [1,2,3,4,5]
# run = [10,3,14,15,4]
# pl.xlim(0,10)
# pl.title("Cricket Analysis")
# pl.bar(over,run,width=1/2)
# pl.show()




# import matplotlib.pyplot as pl
# import numpy as np
# contri = [12.0,14.0,13.0,27.0]
# expl=[0,0,0.3,0]
# Houses = ["Shivaji","Tagore","Ashoka","Raman"]
# clr = ['r','g','b','Y']
# pl.pie(contri,labels=Houses,explode=expl,autopct="%1.1f%%")
# pl.show()





# import matplotlib.pyplot as pl
# import numpy as np
# contri = [12.0,14.0,13.0,27.0]
# Houses = ["Shivaji","Tagore","Ashoka","Raman"]
# clr = ['r','g','b','y']
# pl.pie(contri,labels=Houses,colors=clr,autopct="%1.1f%%")
# pl.show()





# import matplotlib.pyplot as pl
# import numpy as np
# contri = [12.0,14.0,13.0,27.0]
# Houses = ["Shivaji","Tagore","Ashoka","Raman"]
# pl.pie(contri,labels=Houses,autopct="%1.1f%%")
# pl.show()




# import matplotlib.pyplot as pl
# import numpy as np
# contri = [12.0,14.0,13.0,27.0]
# Houses = ["Shivaji","Tagore","Ashoka","Raman"]
# pl.pie(contri)
# pl.show()





# import matplotlib.pyplot as pl
# import numpy as np
# over=np.arange(1.0,6.0,1.0)
# Ind = [13,5,7,16,4]
# pl.xlabel("Overs")
# pl.ylabel("Runs")
# pl.barh(over,Ind,color = 'b')
# pl.show()




# import matplotlib.pyplot as pl
# import numpy as np
# over=np.arange(1.0,6.0,1.0)
# Ind = [13,5,7,16,4]
# Nz = [3,5,4,8,11]
# pl.xlabel("Overs")
# pl.ylabel("Runs")
# pl.bar(over,Ind,color = 'b',width=0.25)
# pl.bar(over+0.25,Nz,color = 'k',width=0.25)
# pl.show()




# import matplotlib.pyplot as pl
# over = [1,2,3,4,5]
# run = [13,5,7,16,4]
# pl.xlabel("Overs")
# pl.ylabel("Runs")
# pl.bar(over,run,color = ['r','g','b','k','c'])
# pl.show()




# import matplotlib.pyplot as pl
# over = [1,2,3,4,5]
# run = [13,5,7,16,4]
# pl.xlabel("Overs")
# pl.ylabel("Runs")
# pl.bar(over,run,color = 'red')
# pl.show()




# import matplotlib.pyplot as pl
# over = [1,2,3,4,5]
# run = [13,5,7,16,4]
# pl.xlabel("Overs")
# pl.ylabel("Runs")
# pl.bar(over,run)
# pl.show()





# import matplotlib.pyplot as pl
# import numpy as np
# x = np.arange(0,10,0.1)
# a = np.cos(x)
# b = np.sin(x)
# pl.plot(x,a,'r',linestyle = 'dashed')
# pl.plot(x,b,'b',linewidth = 2)
# pl.show()




# import matplotlib.pyplot as pl
# import numpy as np
# x = np.arange(0,10,0.1)
# a = np.cos(x)
# b = np.sin(x)
# pl.plot(x,a,'r',linewidth = 4)
# pl.plot(x,b,'b',linewidth = 2)
# pl.show()





# import matplotlib.pyplot as pl
# over = [1,2,3,4,5]
# run = [13,4,16,5,7]
# pl.xlabel("Overs")
# pl.ylabel("Runs")
# pl.plot(over,run)
# pl.show()




# import numpy as np
# lst = [1,2,3,4]
# a1 = np.array(lst)
# print(lst)
# print(a1)
# print(type(a1))