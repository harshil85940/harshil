from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import time
import datetime
import pyttsx3
import os
import random
import pywhatkit

driver = webdriver.Chrome('D:\\PG\\assistant\\web\\chromedriver.exe')
driver.get('file:///D:/PG/assistant/index.html')
driver.maximize_window()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#engine.say('नमस्कार')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak('नमस्कार')

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("गुड मॉर्निंग मेरे प्यारे दोस्त")
    elif hour>=12 and hour<18:
        speak("शुभ दोपहर मेरे प्यारे दोस्त")
    else:
        speak("शुभ संध्या मेरे दोस्त")
def sendEmail(to,query2):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshilrashmishah@gmail.com','')
    server.sendmail('harshilrashmishah@gmail.com',to,query2)
    server.close()
#speak('नमस्कार')

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit = 5)
    response = ""
    speak('भाषण की पहचान करना')
    try:
        response = recognizer.recognize_google(audio, language='hi-in')
    except:
        response = "Error"
    return response
time.sleep(3)
WishMe()
speak('अब मैं ऑनलाइन हूँ')
while True:
    speak('मैं आपका अपना क्या मदद कर सकता हूँ')
    voice = recognize_speech()
    if 'गूगल खोलो' in voice:
        speak('रुको यार मैं गूगल खोल रहा हूँ')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://google.com')
    elif 'गूगल खोज' in voice:
        while True:
            speak('मैं सुन रहा हूं')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('q')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'यूट्यूब खोलो' in voice:
        speak('यूट्यूब खोलना')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://www.youtube.com')
    elif 'यूट्यूब सर्च' in voice:
        while True:
            speak('मैं सुन रहा हूं')
            query = recognize_speech()
            if query != 'Error':
                break
        element = driver.find_element_by_name('search_query')
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
    elif 'गाना चालू करो' in voice:
        speak('अब ..आएगा..असली..मजा')
        music_dir = 'C:\\Users\\LENOVO\\Music\\songs'
        songs = os.listdir(music_dir)
        num = random.randint(0,7)
        os.startfile(os.path.join(music_dir,songs[num]))
        time.sleep(15)
    elif 'समय क्या हुआ है' in voice:
        strtime = datetime.datetime.now().strftime("%H:%M")
        speak(f"मेरे दोस्त ....अभी समय {strtime}...हुआ है")
    elif 'वातावरण बताओ' in voice:
        codepath = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        anpath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        speak("कोन्सा वातावरण खोलू ......सब लाइम .....या..... दृश्य कोड")
        speak('1 ..बोल ने पर...सब लाइम.... 2 ..बोल ने पर....दृश्य कोड')
        query1 = recognize_speech()
        if 'एक' in query1:
            os.startfile(anpath)
        elif 'दो' in query1:
            os.startfile(codepath)
            time.sleep(10)
        else:
            break
    elif 'नोटपैड खोलो' in voice:
        codepad = 'C:\\WINDOWS\\system32\\notepad.exe'
        os.startfile(codepad)
    elif 'मैसेज करो' in voice:
        speak('क्या ..भेज ..ना है ..संदेश..तुजे..वो बोल')
        q1 = recognize_speech()
        pywhatkit.sendwhatmsg("+919619690066",q1,11,43)
        speak("व्हाट्स ..एप ..मेसेज ..हो ..रहा है")
    elif 'तुम्हारा नाम क्या है मेरे दोस्त' in voice:
        speak("मेरा नाम ..चुगल है और ..तुम्हारा")
        q2 = recognize_speech()
        speak(f"{q2}.. बहुत अच्छा ..नाम है")
    elif 'वापस जाओ' in voice:
        driver.back()
    elif 'आगे जाओ' in voice:
        driver.forward()
    elif 'चेंज करो' in voice:
        speak('स्विच बंध हो रहा है')
        driver.close()
    elif 'जाओ' in voice:
        speak('मे जा रहा हु मेरे दोस्त अगर आपको मेरी मदद की जरूरत हो तो मुझसे कभी भी कहना')
        driver.quit()
        break
    elif 'थोड़ा समय जोड़ें' in voice:
        speak('दो मिनट के लिए मे जा रहा हूं')
        time.sleep(120)
    elif 'ज़यादा समय जोड़ें' in voice:
        speak('पाच मिनट के बाद मैं वापस आता हु इसे याद रखना')
        time.sleep(300)
    elif 'बदलो' in voice:
        num_tabs = len(driver.window_handles)
        cur_tab = 0
        for i in range(num_tabs):
            if driver.window_handles[i] == driver.current_window_handle:
                if i != num_tabs - 1:
                    cur_tab = i + 1
                    break
        driver.switch_to_window(driver.window_handles[cur_tab])
    elif 'शॉपिंग की वेबसाइट खोलो' in voice:
        speak('रुको यार मैं..खोल रहा हूँ')
        driver.get('https://www.flipkart.com/')
        driver.execute_script("window.open('');")
        window_list = driver.window_handles
        driver.switch_to_window(window_list[-1])
        driver.get('https://www.amazon.in/')

    else:
        speak('मुजे समज नही आ रहा है फिर से कोशिश करे')
    time.sleep(3)

