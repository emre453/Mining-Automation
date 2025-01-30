import time
import keyboard
import pyautogui
import pydirectinput
import win32api,win32con
import ctypes
time.sleep(2)
def click(x, y, right=False):
    win32api.SetCursorPos((x, y))
    if right:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
def find_object_with_drag(image_path, confidence=0.8, step=75, max_attempts=25, start_x=586, start_y=190):
    pyautogui.moveTo(start_x, start_y)   
    
    attempts = 0
    start_time = time.time()
    while attempts < max_attempts and (time.time() - start_time) < 25:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                print("Nesne bulundu!", location)
                return location
        except Exception as e:
            print("aramaya devam ediliyor...")
        
        try:
            pyautogui.mouseDown(button='right')
            pyautogui.moveRel(step, 0, duration=0.1)
            pyautogui.mouseUp(button='right')
        except Exception as e:
            print("Fare hareketinde hata oluştu, devam ediliyor...")
        
        attempts += 1
        time.sleep(0.2) 
    
    print("Nesne bulunamadı!")
    return None


def right_click(x, y):
    try:
        ctypes.windll.user32.SetCursorPos(x, y) 
        time.sleep(0.1)
        ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0, 0)
        time.sleep(0.5)
        ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0, 0) 
    except Exception as e:
        print(f"right_click fonksiyonunda hata: {e}")
while True:
    pydirectinput.press('h')
    time.sleep(1)
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\town.png', confidence=0.8)
    if image_location is not None:
            center_x, center_y = pyautogui.center(image_location)
            pyautogui.moveTo(center_x, center_y ,   duration=0.5)
            x, y = win32api.GetCursorPos()
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.078)
            keyboard.press("ESC")
            time.sleep(0.1)
            keyboard.release("ESC")
            time.sleep(3)

    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(1)
    image_path = 'C:\\python\\maden\\pitmanjaro1.png'
    find_object_with_drag(image_path)
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\pitmanjaro1.png', confidence=0.7)
    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)

        pyautogui.moveTo(center_x -5, center_y +40 ,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        time.sleep(10)    

    image_path = 'C:\\python\\maden\\sadi.png'
    find_object_with_drag(image_path)

    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\sadi.png', confidence=0.65)

    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x , center_y +25 ,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        keyboard.press("r")
        time.sleep(0.5)
        keyboard.release("r")
        time.sleep(0.2)
        keyboard.press("d")
        time.sleep(1.2)
        keyboard.release("d")
        time.sleep(0.1)
        keyboard.press("e")
        time.sleep(0.1)
        keyboard.release("e")
        time.sleep(12)
        print("Karakter maden alanına gidiyor...")
        keyboard.press('a')
        time.sleep(1.3)
        keyboard.release("a")
        time.sleep(25)
        keyboard.press("s")
        time.sleep(0.1)
        keyboard.release("s")
        time.sleep(1)
        pydirectinput.press("space")
        time.sleep(1)
          

    confidence = 0.7 
    start_time = time.time()
    confidence = 0.85   
    start_time = time.time()   
    while True:
        try:
            image_location = pyautogui.locateOnScreen(r'C:\python\maden\stopmining1.png', confidence=confidence)
            
            if image_location is not None:  # Resim bulunduğunda
                keyboard.press('ı')  # "ı" tuşuna bas
                time.sleep(0.5)
                keyboard.release('ı')
                time.sleep(0.5)
                print("envanter doldu. kırdırma işlemine geçiliyor...")
                break 
            if time.time() - start_time > 1800:
                print("zaman aşımı.")
                break

            time.sleep(1)  # 1 saniye bekle ve tekrar dene

        except Exception as e:
            print(f"kazmaya devam ediliyor.... {e}")   
            time.sleep(15)



    time.sleep(2)

    sling_pos = None
    junk_pos = None

    def find_sling():
        global sling_pos
        sling_image = pyautogui.locateOnScreen('C:\python\maden\sling.png', confidence=0.85)
        if sling_image is not None:
            sling_pos = pyautogui.center(sling_image)

    def find_junk():
        global junk_pos
        junk_image = pyautogui.locateOnScreen('C:\python\maden\junk.png', confidence=0.8)
        if junk_image is not None:
            junk_pos = pyautogui.center(junk_image)

    def drag_and_drop():
        find_sling()
        find_junk()
        if sling_pos is not None and junk_pos is not None:
            win32api.SetCursorPos(sling_pos)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(1)
            win32api.SetCursorPos(junk_pos)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(1)
            print("Sürükle ve bırak işlemi gerçekleştirildi.")
        else:
            print("Dosyalar bulunamadı.")

    while sling_pos is None:
        find_sling()

    drag_and_drop()

    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\onayla.png', confidence=0.7)

    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        x = center_x
        y = center_y
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.5)
        time.sleep(1)

    pydirectinput.press('h')
    time.sleep(1)
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\town.png', confidence=0.8)
    if image_location is not None:
            center_x, center_y = pyautogui.center(image_location)
            pyautogui.moveTo(center_x, center_y ,   duration=0.5)
            x, y = win32api.GetCursorPos()
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.078)
            keyboard.press("ESC")
            time.sleep(0.1)
            keyboard.release("ESC")
            time.sleep(3)

    time.sleep(2)
    pyautogui.scroll(-1000)
    time.sleep(2)
    

    image_path = 'C:\\python\\maden\\pitmanjaro1.png'
    find_object_with_drag(image_path)
    time.sleep(1)   
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\pitmanjaro1.png', confidence=0.6)
    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x -5, center_y +35 ,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        time.sleep(13)
    print("Fps kamera modu değiştiriliyor...")
    keyboard.press("F9")
    time.sleep(1)
    keyboard.release("F9")
    time.sleep(1)
    keyboard.press("F9")
    time.sleep(1)
    keyboard.release("F9")
    time.sleep(1)
    pydirectinput.press("b")
    time.sleep(1)



    def find_and_click(image_path, confidence=0.7):
        try:
            image_location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if image_location:
                center_x, center_y = pyautogui.center(image_location)
                click(center_x, center_y)
                return True
        except:
            pass
        return False

    for _ in range(5):   
        try:
            pydirectinput.press("b")
            time.sleep(0.1)
            click(512, 483, right=True) 
            time.sleep(1)
            for i in range(5):
                find_and_click('C:\\python\\maden\\exchange.png')
                find_and_click('C:\\python\\maden\\goldore.png')
                find_and_click('C:\\python\\maden\\confirm1.png')
        except:
            pass

    print("Kırdırma işlemi tamamlandı.")
    print("Fps kamera modu değiştiriliyor...")
    time.sleep(1)
    keyboard.press("F9")
    time.sleep(1)
    keyboard.release("F9")
    time.sleep(1)
    keyboard.press("F9")
    time.sleep(1)
    keyboard.release("F9")
    time.sleep(1)
    time.sleep(1)
    pyautogui.scroll(-1000)
    time.sleep(1)
    pydirectinput.press('h')
    time.sleep(1)
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\town.png', confidence=0.8)
    if image_location is not None:
            center_x, center_y = pyautogui.center(image_location)
            pyautogui.moveTo(center_x, center_y ,   duration=0.5)
            x, y = win32api.GetCursorPos()
            time.sleep(1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.078)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.078)
            keyboard.press("ESC")
            time.sleep(0.1)
            keyboard.release("ESC")
    time.sleep(8)

    image_path = 'C:\\python\\maden\\armornpc.png'
    find_object_with_drag(image_path)
    pydirectinput.press("b")
    time.sleep(1)
    time.sleep(1)  # Son bekleme süresi
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\armornpc.png', confidence=0.8)
    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x -5, center_y +35 ,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
        time.sleep(8)
        right_click(527, 455) 
        time.sleep(1)
        print("Tedarik yapılıyor...")
        image_location = pyautogui.locateOnScreen('C:\\python\\maden\\iwantrpr.png', confidence=0.8)
        if image_location is not None:
            center_x, center_y = pyautogui.center(image_location)
            x = center_x
            y = center_y
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.5)
        else:
            print("iwantrpr bulunamadı")
        time.sleep(2)
        image_location = pyautogui.locateOnScreen('C:\\python\\maden\\matock.png', confidence=0.7)
        if image_location is not None:
            center_x, center_y = pyautogui.center(image_location)
            x = center_x
            y = center_y
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            time.sleep(0.5)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            time.sleep(0.5)
        else:
            print("iwantrpr bulunamadı")
        time.sleep(1)
        pydirectinput.press("ESC")
        time.sleep(2)


    image_path = 'C:\\python\\maden\\wpn.png'
    find_object_with_drag(image_path)

    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\wpn.png', confidence=0.8)

    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x, center_y +35 ,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
    time.sleep(2)
    keys_and_times = [('r', 0.08998298645019531, 0.12998414039611816),
                    ('e', 0.09000372886657715, 0.19899892807006836),
                    ('d', 0.23102521896362305, 3.070429563522339),
                    ('d', 0.18030619621276855, 3.219986438751221),
                    ('a', 0.4103555679321289, 5.459778308868408),
                    ('a', 0.4104940891265869, 3.59203028678894),
                    ('w', 0.047998905181884766, 0)]

    for index, (key, press_duration, time_between_keys) in enumerate(keys_and_times):
        keyboard.press(key)
        time.sleep(press_duration)
        keyboard.release(key)
        if index < len(keys_and_times) - 1 and time_between_keys > 0:
            time.sleep(time_between_keys)
        if key == 'r':
            time.sleep(1)

    pydirectinput.press("b")
    time.sleep(0.5)
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\inn.png', confidence=0.7)

    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x, center_y +65,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)
        time.sleep(0.078)
    time.sleep(4)
    image_location = pyautogui.locateOnScreen('C:\\python\\maden\\inn2.png', confidence=0.85)

    if image_location is not None:
        center_x, center_y = pyautogui.center(image_location)
        pyautogui.moveTo(center_x, center_y  ,   duration=0.5)
        x, y = win32api.GetCursorPos()
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.078)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.078)
    time.sleep(5)
    def rightclick(x,y):
        win32api.SetCursorPos((x,y))
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)


    def slot1(x,y):

        time.sleep(0.25)
        rightclick(x, y)
        time.sleep(0.5)
        keyboard.press("enter")   
        time.sleep(0.35)
        keyboard.release("enter")




    slot1X = 676
    slot1Y = 465

    for x in range(7):

        slot1(slot1X, slot1Y)
        slot1X = slot1X + 50

    slot1X = 676
    slot1Y = 510
    for x in range(7):

        slot1(slot1X, slot1Y)
        slot1X = slot1X + 50
    slot1X = 676
    slot1Y = 545
    for x in range(7):

        slot1(slot1X, slot1Y)
        slot1X = slot1X + 50
    slot1X = 676
    slot1Y = 590
    for x in range(7):

        slot1(slot1X, slot1Y)
        slot1X = slot1X + 50    
    time.sleep(1)
    pydirectinput.press("ESC")
    time.sleep(1)
    print("mining islemi bitti döngü devam ediyor...")


     