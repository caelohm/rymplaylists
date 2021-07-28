import pyautogui as pg
import time
import os
import re
import pyperclip

'''
only works with 4k resolution main display, 
80% zoom rym page snapped the left 1st tab in chrome,
txt document snapped to the right (ONLY ONE DOC)
spotify snapped to the left
view in spotify is reset and zoomed out twice
vscode is snapped to right side with terminal open
taskbar order:
    task view, app, app, app, spotify, chrome,
        app, app, app, app, app, app, vscode, txt doc

Look at the TODO below in nextpage() to set 
number of seconds to wait before scanning the next page
to prevent being blocked for loading pages too fast
'''

class Album:
    def __init__(self, position, title, artist, avgrating, numratings):
        self.position = position
        self.title = title
        self.artist = artist
        self.avgrating = avgrating
        self.numratings = numratings

    def get(self, str):
        switcher = {
            't': self.title,
            'art': self.artist,
            'avgr': self.avgrating,
            'numr': self.numratings,
        }
        return switcher.get(str, 'Invalid Album String')

    def __eq__(self, other):
        if (self.title != other.title):
            return False
        if (self.artist != other.artist):
            return False
        if (self.avgrating != other.avgrating):
            return False
        if (self.numratings != other.numratings):
            return False
        
        return True

    def alPrint(self):
        print('\nPosition: ' + self.position +
            '\nTitle: ' + self.title + 
            '\nArtist: ' + self.artist +
            '\nAverage Rating: ' + self.avgrating +
            '\nNumber of Ratings: ' + self.numratings)


def drag():
    # drag to bottom of page
    pg.mouseDown()
    pg.moveTo(1825, 2025, 1)
    time.sleep(2)

    # overkill scroll value screws it up,
    # done in increments
    i = 0
    for i in range(0, 10):
        pg.scroll(-5000)
        time.sleep(0.2)
    pg.mouseUp()


def cptxt():
    # play catch up
    time.sleep(1)

    # copy and paste to txt doc
    pg.hotkey('ctrl', 'c')
    pg.moveTo(3750, 1900, 0)
    pg.click()
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    time.sleep(0.5)
    pg.hotkey('ctrl', 's')


def nextpage():
    # prevent blocked ip
    # TODO:
    time.sleep(10)

    # at bottom of page
    pg.moveTo(1690, 1260)
    pg.click()


def rymchartcp():
    # Note: must have RYM chart open on left, txt on right
    val = input('\nEnter number of pages to scan:\n')
    val = int(val) + 1

    # goes to correct chrome tab
    pg.moveTo(1500, 2120)
    pg.click()
    pg.moveTo(130, 80)
    pg.click()

    # clicks on txt doc
    pg.moveTo(2380, 2120)
    pg.click()

    # 1, 51 means 1 to 50 (copy to end of page 50)
    for x in range(1, val):
        if (x > 1):
            nextpage()
            # wait for page to load
            time.sleep(5)

        # scroll page up
        pg.moveTo(960, 1080)
        pg.scroll(50000)

        pg.moveTo(50, 600)
        drag()
        cptxt()
        #wait for cptxt()
        time.sleep(1)

    backtoterm()


def snap():
    print('\nPLEASE SNAP TEXT FILE TO RIGHT SIDE.')
    pg.hotkey('win', 'right')
    backtoterm()


def searchalbum(aye):
    # URL's are hard to use when searching album,
    # which is why we search in google

    # searches for album on rateyourmusic
    pyperclip.copy(aye.artist + ' ' + aye.title + ' rateyourmusic')

    # goes to correct chrome tab
    pg.moveTo(1500, 2120)
    pg.click()
    pg.moveTo(760, 70)
    pg.click()

    #pastes and searches
    pg.moveTo(600, 180)
    pg.click()
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'v')
    pg.press('enter')
    time.sleep(2) 

    # click on first link
    pg.moveTo(660, 720)
    pg.click()
    backtoterm()

def backtoterm():
    # back to terminal
    pg.moveTo(2270, 2120)
    pg.click()
    pg.moveTo(3200, 1960)
    pg.click() 




def main():

    # desigend to have directories for each major genre,
    # for example:
    #   gen = 'Ambient'
    #   sub = 'Ambient Dub'
    #   in folder named Ambient lies Ambient Dub.txt 
    #       and Ambient Dub Missing.txt,
    # at very least, create main genre folder in current directory

    # create temp.txt
    if (not os.path.exists('temp.txt')):
        open('temp.txt', 'w').close()

    # Try not to tamper with temp.txt
    # Unless you know what it means
    if (os.stat('temp.txt').st_size == 0):
        print('\nMust start a session, temp.txt is empty')
        load = 'n'
    else:
        load = input('\nLoad previous session? y or n\n')

    if (None != re.search('n', load)):
        filet = open('temp.txt', 'w', encoding='utf8')
        # clear temp.txt
        open('temp.txt', 'w').close()

        gen = input('\nEnter main genre directory:\n')
        sub = input('\nEnter sub-genre:\n')

        rcap = input('\nEnter rating quota:\n')
        ncap = input('\nEnter number of ratings quota:\n')
        start_point = input('\nEnter album position number to start from:\n')

        filet.write(gen + '\n' + sub + '\n' + rcap + '\n' + 
            ncap + '\n' + start_point + '\n')
        
        print('\nSession saved to temp.txt\n')

    else:
        filet = open('temp.txt', 'r', encoding='utf8')
        # load information from last session
        gen = filet.readline()
        sub = filet.readline()
        rcap = filet.readline()
        ncap = filet.readline()
        start_point = filet.readline()
        # newline fucks with program, must remove
        gen = gen.rstrip('\n')
        sub = sub.rstrip('\n')
        rcap = rcap.rstrip('\n')
        ncap = ncap.rstrip('\n')
        start_point = start_point.rstrip('\n')


    filet.close()

    parse = gen + '\\' + sub + '.txt'
    missing = gen + '\\' + sub + ' Missing.txt'

    # create gen\sub.txt 
    # create gen\sub Missing.txt
    if (not os.path.exists(parse)):
        open(parse, 'w').close()
    if (not os.path.exists(missing)):
        open(missing, 'w').close()

    # Yes, the chart will only be copied if the
    # file being written to is empty
    if (os.stat(parse).st_size == 0):
        skip = 'n'
    else:
        skip = 'y'

    if (None != re.search('n', skip)):
    # file opened must be pasted into
    # opens gen\sub.txt
        os.startfile(parse)
        time.sleep(0.5)
        snap()
        rymchartcp()
    filec = open(parse, 'r', encoding='utf8')

    absolute = []
    nravg = 0.0
    ravg = 0.0
    totalb = 0.0

    # parse text file into absolute
    for line in filec:
        if (line.find('.') < 5):
            if (None != re.search('\d\.', line) and None == re.search('\d\...', line)):
                tit = filec.readline()
                art = filec.readline()
                temp = filec.readline()
                if (None == re.search('\d\.\d\d', temp)):
                    avgr = filec.readline()
                    numr = filec.readline()
                else:
                    avgr = temp
                    numr = filec.readline()
                
                art = art.replace('&', '')
                art = art.replace('/', '')

                temp = numr
                if (len(temp) > 3):
                    temp = temp.replace(',', '')

                '''
                print(tit)
                print(art)
                print(avgr)
                print(temp)
                '''
                ravg = ravg + float(avgr)
                nravg = nravg + float(temp)
                totalb = totalb + 1.0

                if (int(temp) >= int(ncap) and float(avgr) >= float(rcap)):        
                    alb = Album(line, tit, art, avgr, numr)
                    absolute.append(alb)


    #average number of ratings for selected range
    print('\nNumber of Albums:\n' + str(totalb))
    print('\nAverage rating:\n' + str(round(ravg / totalb, 2)))
    print('\nAverage number of ratings:\n' + str(nravg / totalb))
    filec.close()

    # txt document to paste albums that cannot be found
    filep = open(missing, 'a', encoding='utf8')

    fin = 'n'

    while(fin == 'n'):
        if (int(start_point) <= 1):
            ran = 0
            fin = 'y'
        else:
            for i in range(0, len(absolute)):
                if (int(start_point) == int(absolute[i].position.replace('.', ''))):
                    absolute[i-1].alPrint()
                    absolute[i].alPrint()
                    print('^^Use this album^^\n')
                    absolute[i+1].alPrint()
                    break
            if (i+1 == len(absolute)):
                print('\n' + start_point + '. is A) either out of search range or\n' +
                    'B) has been taken out by rating/number of ratings\n' + 
                    'quota')
            else:
                fin = input('Is this correct? y or n\n')
                if (fin == 'y'):
                    ran = i

    # Move into clipboard and take user input
    for i in range(ran, len(absolute)):
        absolute[i].alPrint()
        pyperclip.copy(absolute[i].title + ' ' + absolute[i].artist)
        val = '+'
        while (not val.isspace() and val != 'r'):
            # search in spotify
            if (val == '+'):
                pg.moveTo(1380, 2120)
                pg.click()
                pg.moveTo(190, 260)
                pg.click()
                time.sleep(0.2)
                pg.moveTo(1350, 70)
                pg.click()
                pg.hotkey('ctrl', 'a')
                pg.hotkey('ctrl', 'v')
            
            if (val == '+'):
                val = input('Enter whitespace to search next album,\n' +
                    '\t-p to go to album page on rym,\n' +
                    '\t-g to report missing spotify album to \n\t\t' +
                    gen + '/' + sub + ' Missing.txt\n' +
                    '\t-r to restart,\n' +
                    '\t-t to terminate\n')
            else: 
                val = input('\nInput next command\n')

            if (None != re.search('p', val)):
                searchalbum(absolute[i])
                # wait for searchurl to finish
                time.sleep(3)
                pyperclip.copy(absolute[i].title + ' ' + absolute[i].artist)

            if (None != re.search('g', val)):
                filep.write('*****************************************************'
                    '\nPosition: ' + absolute[i].position +
                    '\nTitle: ' + absolute[i].title + 
                    '\nArtist: ' + absolute[i].artist +
                    '\nAverage Rating: ' + absolute[i].avgrating +
                    '\nNumber of Ratings: ' + absolute[i].numratings)
                print('Album written to ' + gen + '/' + sub + ' Missing.txt')

            if (None != re.search('r', val)):
                filep.close()
                return True

            if (None != re.search('t', val)):
                filep.close()
                return False
            
    filep.close()
    return False


if __name__ == "__main__":
    restart = True
    while (restart == True):
        restart = main()

    # pyautogui trial
    '''
    import pyautogui as pg
    pg.moveTo(600, 180)
    '''