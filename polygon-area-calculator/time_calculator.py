MINS_IN_DAY = 24 * 60
DAYS_OF_WEEK_BY_INDEX = {
    0: "Sunday",
    1: "Monday", 
    2: "Tuesday", 
    3: "Wednesday", 
    4: "Thursday", 
    5: "Friday", 
    6: "Saturday", 
}
DAY_OFFSET_MINS_DIC = {
    "sunday": 0,
    "monday": 1 * MINS_IN_DAY,
    "tuesday": 2 * MINS_IN_DAY,
    "wednesday": 3 * MINS_IN_DAY,
    "thursday": 4 * MINS_IN_DAY,
    "friday": 5 * MINS_IN_DAY,
    "saturday": 6 * MINS_IN_DAY,
    None: 0
}

def add_time(startTimeString, durationString, startDay = None):
    endTimeStrResult = 'EndTime'

    dayOffsetMins = DAY_OFFSET_MINS_DIC[startDay.lower()] if startDay != None else 0
    finalTimeInMins = extractTotalLapsMins(startTimeString, durationString, dayOffsetMins)

    finalStopObj = convertMinsToDayTime(finalTimeInMins)
    
    endTimeStrResult = formatPrintFromDateTime(finalStopObj, startDay)

    return endTimeStrResult

def formatPrintFromDateTime(finalStopObj, startDay):
    period = "AM" if finalStopObj["hours"] < 12 else "PM"
    formatedHrs = finalStopObj["hours"] if period == "AM" else (finalStopObj["hours"] - 12) // 1
    formatedHrs = formatedHrs if formatedHrs != 0 else 12 # fixes issue for 12:01 AM (ie: at the 0 hr)
    formatedMins = finalStopObj["mins"] if finalStopObj["mins"] > 9 else f'0{finalStopObj["mins"]}'
    
    endTimeStrResult = f'{int(formatedHrs)}:{formatedMins} {period}'

    # add day of week
    if startDay != None:
        dayOfWeekIndex = finalStopObj["days"] % 7
        dayOfWeek = DAYS_OF_WEEK_BY_INDEX[dayOfWeekIndex]
        endTimeStrResult += f', {dayOfWeek}'

    # add day change tag
    dayOffsetMins = DAY_OFFSET_MINS_DIC[startDay.lower()] if startDay != None else 0
    dayDrift = int(((finalStopObj["days"] * MINS_IN_DAY) - dayOffsetMins) / MINS_IN_DAY)
    if dayDrift > 0:
        if dayDrift == 1:
            endTimeStrResult += ' (next day)'
        else:
            endTimeStrResult += f' ({dayDrift} days later)'

    return endTimeStrResult


def convertMinsToDayTime(totalMins):
    dateTime = {
        "days": 0,
        "hours": 0,
        "mins": 0,
    }

    days = (totalMins / MINS_IN_DAY ) // 1
    hours = ((totalMins - (days * MINS_IN_DAY)) / 60 ) // 1
    mins = (totalMins - (days * MINS_IN_DAY) - (hours * 60)) // 1

    dateTime["days"] = int(days)
    dateTime["hours"] = int(hours)
    dateTime["mins"] = int(mins)

    return dateTime

def extractTotalLapsMins(startTimeString, durationString, dayOffsetMins):
        # normalize start time to mins
    startIndexOfTimeCol = startTimeString.find(':')
    startTimeHr = int(startTimeString[0:startIndexOfTimeCol])
    startTimeMin = int(startTimeString[startIndexOfTimeCol+1:startIndexOfTimeCol+3])
    startTimePeriod = startTimeString.split()[1]

    if startTimePeriod == "PM":
        startTimeHr += 12

    totalStartMins = (startTimeHr * 60) + startTimeMin

    # normalize duration to mins
    durationIndexOfTimeCol = durationString.find(':')
    startTimeHr = int(durationString[0:durationIndexOfTimeCol])
    startTimeMin = int(durationString[durationIndexOfTimeCol+1:durationIndexOfTimeCol+3])

    totalDurationMins = (startTimeHr * 60) + startTimeMin

    finalTimeInMins = totalStartMins + totalDurationMins + dayOffsetMins

    return finalTimeInMins


print("Result:", add_time("2:59 AM", "24:00", "saturDay"))


