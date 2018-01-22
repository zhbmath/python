#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import curses
import curses.ascii

def init_screen():
    return curses.initscr()

def end_screen():
    curses.endwin()

def get_ch(win):
    '''''Get char'''
    curses.echo(0) #关闭回显
    win.nodelay(0) #设置为阻塞式
    ch=win.getch()
    win.nodelay(1) #重置非阻塞式接受输入，超时1秒
    return ch

def main():
    stdscr=init_screen() 
    stdscr.keypad(1) # 打开扩展键盘
    while True:
        ch=get_ch(stdscr)
        if ( ch==ord('q') or ch==curses.ascii.ESC or ch==112 ):
            break
        if ( ch==curses.KEY_DOWN ):
            stdscr.addstr("Hello,")
    
if __name__=='__main__':
    try:
        main()
    except Exception,e:
        raise e
    finally:
        end_screen()
