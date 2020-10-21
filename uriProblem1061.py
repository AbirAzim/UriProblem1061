
sd,dia = input().split()
startDia = int(dia)
startHour,startMinute, startSecond = input().split(":")
startHour = int(startHour)
startMinute = int(startMinute)
startSecond = int(startSecond)


ed,eDia = input().split();
endDia = int(eDia)
endHour,endMinute,endSecond = input().split(":")
endHour = int(endHour)
endMinute = int(endMinute)
endSecond = int(endSecond)


startTimeInSeconds = ((startDia * 24 * 60 * 60)) + (startHour * 60 * 60) + (startMinute * 60) + startSecond
endTimeInSeconds = ((endDia * 24 * 60 * 60)) + (endHour * 60 * 60) + (endMinute *60) + endSecond

resultInSeconds = endTimeInSeconds - startTimeInSeconds

resultDia = int(resultInSeconds/(24*60*60))
resultHour = int((resultInSeconds -  ((resultDia * 24) * 60 * 60)) / (60 * 60))
resultMinute = int(((resultInSeconds - (((resultDia * 24) * 60 * 60) + (resultHour * 60 * 60))) / 60))
resultSecond = (resultInSeconds - (((resultDia * 24) * 60 * 60) + (resultHour * 60 * 60) + (resultMinute * 60)))

print(resultDia,"dia(s)")
print(resultHour,"hora(s)")
print(resultMinute,"minuto(s)")
print(resultSecond,"segundo(s)")
