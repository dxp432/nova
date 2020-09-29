from datetime import date
from auto import *

def ant_click():
    print('点击能量')
    for my_x in range(299, 899, 100):
        for my_y in range(450, 720, 100):
            # print(my_x, my_y)
            phone_click(my_x ,my_y)
            time.sleep(0.3)

    phone_click(202 ,742)
    time.sleep(0.3)
    phone_click(202 ,817)
    time.sleep(0.3)
    phone_click(202 ,950)
    time.sleep(0.3)
    phone_click(283 ,781)
    time.sleep(0.3)

    phone_click(775 ,689)
    time.sleep(0.3)
    phone_click(777 ,791)
    time.sleep(0.3)
    phone_click(845 ,934)
    time.sleep(0.3)
    phone_click(800 ,674)
    time.sleep(0.3)

while True:
    if datetime.datetime.now().hour >= 6 and datetime.datetime.now().hour <= 22:
        print(str(datetime.datetime.now().hour))
        phone_home()
        time.sleep(2)
        phone_home()
        time.sleep(2)

        phone_swipe(896, 1532, 136, 1532)
        time.sleep(2)
        print('打开支付宝')
        phone_click(122, 1557)  

        time.sleep(3)
        phone_prtsc()
        time.sleep(2)
        phone_matchImgClick('ant.png')
        time.sleep(3)
        ant_click()
        time.sleep(3)

        for my_swipe in range(1, 15, 1):
            print('------------------------------------' + str(my_swipe))

            if datetime.datetime.now().minute % 15 == 0:
                print('每个n分钟强制返回')
                for my_loop in range(10):
                    print('back')
                    phone_back()
                    time.sleep(1)
                break


            phone_swipe(566, 2059, 566, 718)
            time.sleep(2)

            phone_prtsc()
            time.sleep(2)
            if phone_if_matchImg('hand.png'):
                phone_matchImgClick('hand.png')
                time.sleep(2)
                ant_click()
                time.sleep(2)
                phone_back()
                time.sleep(2)     

            if phone_if_matchImg('help.png'):
                phone_matchImgClick('help.png')
                time.sleep(2)
                ant_click()
                time.sleep(2)
                phone_back()
                time.sleep(2)

            if phone_if_matchImg('more_fr.png'):
                phone_matchImgClick('more_fr.png')
                time.sleep(2)

            if phone_if_matchImg('no_more.png'):
                for my_back in range(1, 5, 1):
                    phone_back()
                    time.sleep(2)
                phone_home()
                time.sleep(2)
                break
        time.sleep(3)
    else:
        print('还没到时间')
        
        phone_click(746, 2201)  
        time.sleep(10)
        phone_home()
        time.sleep(10)
        # phone_prtsc()
        time.sleep(2)
    