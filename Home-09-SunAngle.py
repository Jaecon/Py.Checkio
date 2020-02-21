def sun_angle(time):
    t_minutes = int(time.split(":")[0])*60 + int(time.split(":")[1])

    if t_minutes < 360 or t_minutes > 1080:
        return "I don't see the sun!"
    else:  
        res = (t_minutes-360)/4
        return round(res,2)

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")