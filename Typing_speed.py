from time import time #for calculating time

def typerror(prompt):
  global u_words # we decleared in main function
  i_words=prompt.split()
  error=0
  for i in range(len(u_words)):
    if i in range(0,len(i_words)-1):
      if i_words[i]==u_words[i]:
        continue
      else:
        error+=1
    else:
       if i_words[i]==u_words[i]:
         if(i_words[i+1]==u_words[i+1] and i_words[i-1]==u_words[i-1]):
           continue
         else:
           error+=1
       else:
         error+=1
  return  error

def elapsed_time(stime,etime): #stime->start time , etime->end time
  time=etime-stime
  return time

def speed(u_words):
  global time

  twords=len(u_words)
  speed=twords/time
  return speed

if __name__=='__main__':
  #GIVING input
  prompt="Your Intelligence may fail, but your hard work never fails. If you do quick research on the keys to success, you will find a lot of resources. Some people will call them the only secrets to success you should know, while others will refer to this information as principles, elements, steps, factors, and so on. But the truth is there is only one thing you can’t go without if you want to succeed in any area of life, and that is hard work. Hard work never fails. There is more behind that, though."
  print("TYPE THIS FOLLOWING PARAGRAPH:\n ",prompt,'\n')
  input("PRESS ENTER TO START:")
  
  #GETTING input
  stime=time()
  u_words=input().split() #u_words->user_words
  etime=time()
  
  #CALLING functions
  time=round(elapsed_time(stime, etime),2)
  s=speed(u_words)
  t=typerror(prompt)
  
  print("* "*25)
  print("Total time taken: ",time," seconds")
  print("Your average speed:",s," words/minute")
  print("And, you made ",t," errors")
  print("* " * 25)



