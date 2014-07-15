'''
multiple of 3 'Fizz' and 5 'Buzz' and both 'FizzBuzz'
'''
import os,sys
class FizzBuzz:
    def numb(self):
        for i in range(1,101):
            if (i%3==0) and (i%5==0):
                print 'FizzBuzz'
            elif (i%5)==0:
                print 'Buzz'
            elif (i%3==0):
                print 'Fizz'
            else:
                print i


FizzBuzz().numb()


