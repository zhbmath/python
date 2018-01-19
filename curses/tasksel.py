#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import logging
import curses
from curses import wrapper
#import yaml

logger = logging.getLogger()


def init_screen():
    '''初始化屏幕'''
    return curses.initscr()

def init_color():
    '''初始化颜色'''
    try:
        curses.start_color()  #首先需要调用这个方法
    except:
        pass
    #文字和背景色设置，设置了两个color pair，分别为1和2
    curses.init_pair(1,  curses.COLOR_RED,     curses.COLOR_WHITE)
    curses.init_pair(2,  curses.COLOR_GREEN,   curses.COLOR_WHITE)
    curses.init_pair(3,  curses.COLOR_BLUE,    curses.COLOR_WHITE)
    curses.init_pair(4,  curses.COLOR_RED,     curses.COLOR_BLACK)
    curses.init_pair(5,  curses.COLOR_GREEN,   curses.COLOR_BLACK)
    curses.init_pair(6,  curses.COLOR_BLUE,    curses.COLOR_BLACK)
    curses.init_pair(7,  curses.COLOR_WHITE,   curses.COLOR_RED  )
    curses.init_pair(8,  curses.COLOR_WHITE,   curses.COLOR_GREEN)
    curses.init_pair(9,  curses.COLOR_WHITE,   curses.COLOR_BLUE )
    curses.init_pair(10, curses.COLOR_BLACK,   curses.COLOR_RED  )
    curses.init_pair(11, curses.COLOR_BLACK,   curses.COLOR_GREEN)
    curses.init_pair(12, curses.COLOR_BLACK,   curses.COLOR_BLUE )
    curses.init_pair(13, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(14, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    return True

def set_screen_bkgd(stdscr, color_pair=4):
    '''设置屏幕背景'''
    stdscr.nodelay(1) #以非阻塞的方式接受输入，超时1秒
    stdscr.bkgd(curses.color_pair(color_pair))
    stdscr.refresh()

def create_subwin(stdscr, y, x, height, width, color_pair=9):
    '''创建子窗口'''
    subscr = stdscr.subwin(height, width, y, x)
    subscr.box()
    subscr.bkgd(curses.color_pair(color_pair))
    subscr.refresh()
    return subscr

def show_msg(stdscr, y, x, msg, color_pair=13):
    '''''显示文字'''
    stdscr.addstr(y, x, msg, curses.color_pair(color_pair))
    stdscr.refresh()

    

def end_screen(stdscr):
    '''重置控制台'''
    #恢复控制台默认设置（若不恢复，控制台仍然是没有回显的）
    stdscr.keypad(0)
    curses.nocbreak() #打开回车确认
    curses.echo(1)    #打开回显
    curses.endwin()   #结束窗口

def get_yaml():
    '''读取配置文件'''
    try:
        with open('conf.yaml','r') as loadfile:
            y = yaml.load(loadfile)
        return y
    except yaml.YAMLError as ex:
        print(ex)

def set_yaml():
    '''修改配置文件'''
    try:
        with open('conf01.yaml','w') as dumpfile:
             dumpfile.write(yaml.dump(open('conf01.yaml', 'w')))
        #print yaml.dump(y)
    except yaml.YAMLError as ex:
        print(ex)

def move_cursor(win, new_y, new_x):
    win.nodelay(0)
    win.move(new_y, new_x)
    win.refresh()
    win.nodelay(1)

def get_ch(win):
    '''''Get char'''
    curses.noecho()   #关闭屏幕回显
    curses.cbreak()   #输入不需要回车确认
    win.nodelay(0)    #设置阻塞式
    ch=win.getch()
    win.nodelay(1)    #重置控制台以非阻塞式接受输入
    return ch

def run_win(stdscr):
    try:
        #H0, W0 = stdscr.getmaxyx()
	H0 = curses.LINES 
	W0 = curses.COLS
        show_msg(stdscr,  1, 1, "H0=%d, W0=%d" % (H0, W0), 4)

        subwin1 = create_subwin(stdscr, 1, W0/10, H0-2, W0*8/10 )
        H1, W1 = subwin1.getmaxyx()
        show_msg(subwin1, 1, 1, "H1=%d, W1=%d" % (H1, W1), 4)

        subwin2 = create_subwin(stdscr, 2, W0/10+W1*2/10, H1-2, W1*6/10, 4)
        H2, W2 = subwin1.getmaxyx()
        show_msg(subwin2, 1, 1, "H2=%d, W2=%d" % (H2, W2), 4)
        #y=get_yaml()
        #show_msg(stdscr, height, width/20+2, "[ X ]  %s" % zip(y[0].iterkeys()), 13)
        i=0
        stdscr.nodelay(1)
        subwin2.nodelay(1)
	subwin2.keypad(1)  # open special keyboard
        while True:
            ch=get_ch(subwin2)
            if ( ch == ord('q')  ):
                break
            else:
                if ( ch==ord('c') or ch==10 or ch==curses.KEY_DOWN ):
                   show_msg(subwin2, H2/3-8+i, W2/16-7, "[ %-02d ]" % i  , 4)
                   move_cursor(subwin2, H2/3-8+i, W2/16-5 )
                   if ( ch==32 ):
                       show_msg(subwin2, H2/3-8+i, W2/16-7, "[ X ]" , 4)
            if i>=20:
               i=0
            i=i+1
    except Exception,e:
        raise e
    finally:
        end_screen(stdscr)

def main():
    stdscr = init_screen()
    init_color()
    #set_screen_bkgd(stdscr)
    end_screen(stdscr)
    run_win(stdscr)

if __name__=='__main__':
    main()

