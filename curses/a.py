#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import curses
import curses.ascii

#import locale
#locale.setlocale(locale.LC_ALL, "")
#code = locale.getpreferredencoding()

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

def show_msg(win, x=10, y=10, msg="hello"):
    win.addstr(y, x, msg)
    win.refresh()

def move_cursor(win, x=10, y=10):
    win.move(y, x)
    win.refresh()

def loop(m,n):
    if n<m:  
        return n
    else:
        return n%m

def navigate(position, total, n):
    """A navigator."""
    position += n
    if position < 0:
        position = total-1 
    elif position > total-1:
        position = 0
    return position

def main():
    stdscr=init_screen() 
    show_msg(stdscr, curses.COLS/4, curses.LINES/4+0, "q=<quit>, Up=<Up>, Down=<Down>, Space=<select>"  )

    show_msg(stdscr, curses.COLS/2, curses.LINES/2+0, "[   ] netcat" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+1, "[   ] tree" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+2, "[   ] vim" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+3, "[   ] pv" )
    move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2)
    stdscr.keypad(1) # 打开扩展键盘
    pos=0
    while True:
        ch=get_ch(stdscr)
        if ( ch==ord('q') or ch==curses.ascii.ESC or ch==112 ):
            break
        if ( ch==curses.KEY_UP ):
	    pos=navigate(pos, 4, -1)
            move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2+pos )
        if ( ch==curses.KEY_DOWN ):
	    pos=navigate(pos, 4, 1)
            move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2+pos )
        if ( ch==32 ):
	    show_msg(stdscr, curses.COLS/2+2, curses.LINES/2+pos, "X")
            move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2+pos )

if __name__=='__main__':
    try:
        main()
    except Exception,e:
        raise e
    finally:
        end_screen()
