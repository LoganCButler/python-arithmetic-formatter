def add_time(startTimeString, durationString):
    endTimeStrResult = 'EndTime'
    MINS_IN_DAY = 24 * 60

    finalTimeInMins = extractTotalLapsMins(startTimeString, durationString)

    finalStopObj = convertMinsToDayTime(finalTimeInMins)

    period = "AM" if finalStopObj["hours"] < 12 else "PM"
    formatedHrs = finalStopObj["hours"] if period == "AM" else int((finalStopObj["hours"] - 12) // 1)
    endTimeStrResult = f'{formatedHrs}:{finalStopObj["mins"]} {period}'

    return endTimeStrResult

def convertMinsToDayTime(totalMins):
    dateTime = {
        "days": 0,
        "hours": 0,
        "mins": 0,
    }
    hours = (totalMins / 60 ) // 1
    mins = (totalMins - (hours * 60)) // 1

    dateTime["hours"] = hours
    dateTime["mins"] = mins

    print(dateTime)
    return dateTime

def extractTotalLapsMins(startTimeString, durationString):
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

    finalTimeInMins = totalStartMins + totalDurationMins

    return finalTimeInMins







print(add_time("3:30 PM", "2:12"))