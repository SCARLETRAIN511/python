def solution1(baktun,katun,tun,uinal,kin):
        # initial from 13,20,7,16,3  2000.1.1
        diffKin = kin - 3
        diffUinal = uinal - 16
        diffTun = tun - 7
        diffKatun = katun - 20
        diffBaktun = baktun - 13
        
        #calculate the difference in days.
        diffDays = diffKin + diffUinal*18 + diffTun*360 + diffKatun*7200 + diffBaktun*144000
        
        #year from 2000, leap year has 366 days
        year = 2000
        yearDays = 366
        while  diffDays >= yearDays:
            
            if year % 4 == 0:
                diffDays -= 366
                year += 1
                yearDays = 365
            else:
                diffDays -= 365
                year += 1
                if year % 4 == 3:
                    yearDays = 366
                else:
                    yearDays = 365
            
            
        if year % 4 == 0:
            FebDays = 29
            monthDays= [31,FebDays,31,30,31,30,31,31,30,31,30,31]
        else:
            FebDays =28
            monthDays= [31,FebDays,31,30,31,30,31,31,30,31,30,31]
            
        month=1
        for i in monthDays:
            if diffDays <= i:
                break
            else:
                diffDays -= i
                month += 1

        return [diffDays,month,year]

if __name__ == "__main__":
    print(solution1(13,20,9,2,9))
        