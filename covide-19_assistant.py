import pyttsx3
import speech_recognition as sr
import datetime
import covid_19_data as cd
import matplotlib.pyplot as plt
import pandas as pd

engin=pyttsx3.init('sapi5')
voice=engin.getProperty('voices')
engin.setProperty('voice',voice[2].id)

def say(audio):
    engin.say(audio)
    engin.runAndWait()

def wish():
    hours=datetime.datetime.now().hour
    if hours>0 and hours<12:
        say('Good morning sir!')
    elif hours>12 and hours<18:
        say('good evening sir !')
    else:
        say('Good night sir!')

    print('Im you assistant FRIDAY, what can i do for you !')
    say('im you assistant friday, what can i do for you !')


def take_command():

    r = sr.Recognizer()
    print('fgdfcsdc')
    with sr.Microphone() as source:
        print('sddfv')
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en_in')
            print(f'User said :- {query}')
        except Exception as e:
            print(e)
            return 'None'
    return query


def corona():
    while 1:
        print('Tell me what you want to ask !!')
        say('tell me what you want to ask')

        query=take_command().lower()

        if 'total' and 'active' in query.lower():

            covid_check('Total-Active-Cases')

        elif 'total' and 'death' or 'died' in query.lower():
            covid_check('Total-Death')

        elif 'how many' and 'cases' or 'case' in query.lower():
            state=query.split('in')[1]
            state=state[0].replace(' ','')+state[1:]
            covid_check(state)

        elif 'prevention' or 'avoid' in query:
            print('1.Stay at Home')
            print('.Keep a safe distance')
            print('3.Wash your hands often')
            print('4.Cover your mouth wile cough')
            print('5.If feeling sick ! Call Helpline := 1075 or 011-23978046')


            say('1.Stay at Home')
            say('.Keep a safe distance')
            say('3.Wash your hands often')
            say('4.Cover your mouth wile cough')
            say('5.If feeling sick ! Call Helpline := 1075 or 011-23978046')

        elif 'total' and 'recover' or 'recovery' in query.lower():
            covid_check('Total-Recover')

        elif 'graph' in query.lower():
            a = pd.DataFrame(cd.covid_database)
            a = a.T
            a.drop(['Total-Active-Cases', 'Total-Recover', 'Total-Death'], axis=0, inplace=True)
            a['State'] = a.index
            a.plot(figsize=(15, 10), kind='barh')
            plt.show()

        print('Want to ask anthing else about Covid-19 ?')
        say('want to ask anything else about covid-19')




        query=take_command().lower()
        if 'no' or 'nothing' in query:
            break
        else:
            continue
    return
def covid_check(query):

    print(query)
    print('dfvsrvdfvdfv')
    for i in cd.covid_database:
        if i.lower() == query.lower():

            print(cd.covid_database[i])

            say(cd.covid_database[i])



if __name__=='__main__':

    wish()
    take_command()
    while 1:

        try:

            query=take_command().lower()
            print('kash')
            if query == 'None':
                print('PLz say something !')
                say('please say something ')
                continue

        except:
            continue

        if 'no' in query:
            print('Bye !!')
            say('bye')
            exit()

        if 'corona' or 'covid' or 'covid-19' in query:
            corona()

        print('Anything else.....')
        say('anything else...')