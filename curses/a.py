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
    stdscr.box()
    show_msg(stdscr, curses.COLS/4, curses.LINES/4+0, "Quit=<q>, Move=<Up>/<Down>, Select=<Space>, Switch=<Tab>" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+20, "<OK>"  )
    show_msg(stdscr, curses.COLS/2+10, curses.LINES/2+20, "<Cancel>"  )

    show_msg(stdscr, curses.COLS/2, curses.LINES/2+0, "[   ] netcat" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+1, "[   ] tree" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+2, "[   ] vim" )
    show_msg(stdscr, curses.COLS/2, curses.LINES/2+3, "[   ] pv" )
    move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2)

    stdscr.keypad(1) # 打开扩展键盘
    pos=0
    while True:
        ch=get_ch(stdscr)
        if ( ch==ord('q') or ch==curses.ascii.ESC ):
            break
        if ( ch==curses.KEY_UP ): # up key
	    pos=navigate(pos, 4, -1)
            move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2+pos )
        if ( ch==curses.KEY_DOWN ): # Down key
	    pos=navigate(pos, 4, 1)
            move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2+pos )
        if ( ch==32 ): # Space key
	    show_msg(stdscr, curses.COLS/2+2, curses.LINES/2+pos, "X")
            move_cursor(stdscr, curses.COLS/2+2, curses.LINES/2+pos )
        if ( ch==9 ): # Tab key
	    pos=navigate(pos, 11, 10)
            move_cursor(stdscr, curses.COLS/2+11-pos, curses.LINES/2+20 )
	if ( ch==curses.KEY_ENTER or ch==10 ): # Enter key
	    y, x = curses.getsyx() 
	    if (x==curses.COLS/2+11 and y==curses.LINES/2+20):
	        show_msg(stdscr, 10, 10, "x=%d, y=%d" % (x, y) )
	        break
	    elif (x==curses.COLS/2+11-pos and y==curses.LINES/2+20 ):
	        show_msg(stdscr, 11, 11, "x=%d, y=%d" % (x, y) )
	        #apt-get install -d netcat tree vim pv
	        pass


if __name__=='__main__':
    try:
        main()
    except Exception,e:
        raise e
    finally:
        end_screen()
