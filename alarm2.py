import time

def countdown(m):
    try:
        m = int(m)
    except ValueError:
        print('Must be an integer!')
    else:
        while Ture:
            for minute in range(m, -1, -1):
                if minute == 0:
                    break
                    for second in range(59, -1, -1):
                        time.sleep(1)
                        print('{}:{}.format(minute-1,second), end=' \r')
            print('Hi,the timer is now end.')
            break

if __name__ == '__main__':
    countdown(2)