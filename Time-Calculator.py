def add_time(start, duration, day=0):
    daysList = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    splitstart = start.split(" ")
    meridian = splitstart[1]
    starttime = splitstart[0]
    starthour = int(starttime.split(':')[0])
    startmin = int(starttime.split(':')[1])
    if meridian == "AM" :
        starthour = starthour
    else :
        starthour += 12;
    splitduration = duration.split(':')
    durationhour = int(splitduration[0])
    durationmin = int(splitduration[1])
    reshour = starthour + durationhour
    resmin = startmin + durationmin
    numberofdays = ''
    if resmin >= 60 :
        resmin -= 60
        reshour += 1
    else :
        resmin = resmin
    if len(str(resmin)) < 2 :
        resmin = "0" + str(resmin)
            
    if reshour >= 24 and reshour%24 == 0 :
        daysnext = reshour // 24
    else :
        daysnext = 0

    if reshour > 24 :
        daysnext = reshour // 24
        reshour = reshour % 24
        if daysnext == 1:
            numberofdays = "next day"
        else :        
            numberofdays = str(daysnext) + " days later"            
    else :
        reshour = reshour
        daysnext = 0

    print(daysnext, reshour, numberofdays, resmin)

    #if reshour == 12 :
        

    if reshour == 0 :
        reshour = 12
        resmeridian = "AM"
    elif reshour > 0 and reshour < 12 :
        resmeridian = "AM"
    elif reshour == 12 :
        if int(resmin) > 0 :
            resmeridian = "PM"
    else :
        reshour -= 12
        resmeridian = "PM"
    
    resday = ''
    if day != 0 :
        day = day[0].upper() + day[1:].lower()
        dayindex = daysList.index(day)
        #print(dayindex)
        resdayindex = dayindex + daysnext
        if resdayindex > 6 :
            resday = daysList[resdayindex%7]
        else :
            resday = daysList[resdayindex]

        if daysnext == 0 :
            print(str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian) + ', '  + str(resday))
            return str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian) + ', '  + str(resday)
        else :
            print(str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian) + ', ' + str(resday) + ' (' + str(numberofdays) + ')')
            return str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian) + ', ' + str(resday) + ' (' + str(numberofdays) + ')'
    elif daysnext == 0 :
        print(str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian))
        return str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian)
    else :
        print(str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian) + ' (' + str(numberofdays) + ')')
        return str(reshour) + ':' + str(resmin) + ' ' + str(resmeridian) + ' (' + str(numberofdays) + ')'

    
add_time("11:43 AM", "00:20")































