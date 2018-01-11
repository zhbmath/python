#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import curses

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

if __name__=='__main__':
    try:
        stdscr=init_screen() 
        while True:
            ch=get_ch(stdscr)
            if ( ch==ord('q') ):
                break
    except Exception,e:
        raise e
    finally:
        end_screen()
