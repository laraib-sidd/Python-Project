#-*- coding: UTF-8 -*-
# Copyright 2017 Davin Yu. All rights reserved.
# Distributed under the GNU General Public License v3.0 (GPLv3).

from datetime import datetime, timedelta
from time import sleep
from Tkinter import *
import os
import sys
import tty, termios
import subprocess

# return the date format of the day which is <n> days from <startdate>
def date_formatter(n, startdate):
    nowdate =  startdate + timedelta(days=n)
    return nowdate.strftime("%c")

# push <num> of time to remote server in specific <date>
def push_to(date, num):
    for i in range (0, num):
        with open('temp.txt', 'a') as f:
            f.write(" ");
        subprocess.call('git add temp.txt', shell=True)
        os.environ["GIT_AUTHOR_DATE"] = date
        os.environ["GIT_COMMITTER_DATE"] = date
        subprocess.call('git commit -m "renew"', shell=True)
        subprocess.call('git push origin master', shell=True)
        sleep(.5)

# clear the shell
def screen_clear():
    subprocess.call('clear', shell=True)

# print the pattern
def screen_print(list):
    print("Use w,s,a,d to control the pointer 'p', use j to select current location")
    print("Press q to finish your input")
    for i in range (-1,8):
        print('')
        for j in range (-1,53):
            if (i==-1 or i==7):
                sys.stdout.write('—')
            elif (j==-1 or j==52):
                sys.stdout.write('|')
            else:
                sys.stdout.write(list[i][j])

# main method
def main():
    screen_clear();
    list = []
    for i in range (0,7):
        list.append([])
        for j in range (0,52):
            list[i].append(' ')
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = ' '
    px = 0
    py = 0
    list[px][py] = 'p'
    stack = ' '
    print('Find the target area for your new Github Contribution Pattern')
    print('Input the date of the top left corner of your target area')
    iyear = input("Input year: ")
    imonth = input("Input month: ")
    iday = input("Input day: ")
    pushtime = input("How many times you want to commit for a day? ")
    while (ch != 'q'):
        screen_clear();
        screen_print(list);
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        # Operation
        if (ch=='j'):
            if (stack != '▇'):
                list[px][py] = '▇'
                stack = '▇'
            else:
                list[px][py] = 'p'
                stack = ' '
        elif (ch=='a' and py>0):
            list[px][py] = stack
            stack = list[px][py-1]
            py = py - 1
            list[px][py] = 'p'
        elif (ch=='d' and py<51):
            list[px][py] = stack
            stack = list[px][py+1]
            py = py + 1
            list[px][py] = 'p'
        elif (ch=='w' and px>0):
            list[px][py] = stack
            stack = list[px-1][py]
            px = px - 1
            list[px][py] = 'p'
        elif (ch=='s' and px<6):
            list[px][py] = stack
            stack = list[px+1][py]
            px = px + 1
            list[px][py] = 'p'

    list[px][py] = stack

    print('')
    print('Are you sure from %d-%d-%d push %d times? (Y/N)' % (iyear, imonth, iday, pushtime))
    sure = input()
    incre = 0
    if (sure.upper() == 'Y'):
        for i in range(0,52):
            for j in range(0,7):
                if (list[j][i] == '▇'):
                    now = date_formatter(incre, datetime(iyear,imonth,iday,8,26,0))
                    push_to(now, pushtime)
                incre = incre + 1
    else:
        print ('Bye!')

if __name__ == "__main__":
    main()
