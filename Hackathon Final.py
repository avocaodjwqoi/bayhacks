import random, HackathonSuicideLines, time


Motivational_statements = ['Almost there!', 'You got this!', 'Relax your mind.', 'Think of happy times.',
                           "Don't give up!", 'You are beautiful.', "All of your feelings are valid." ]




def bigCircle():
   print('       x  x ')
   print('    x        x  ')
   print('   x          x ')       
   print('   x          x   ')   
   print('    x        x   ')         
   print('       x  x  ')           




def smallCircle():
   print('       x  x')
   print('     x      x')
   print('     x      x')
   print('       x  x')


def Breathing(motivation):
   time.sleep(3)
   print("Breathe in.")
   bigCircle()
   time.sleep(2.5)
   print(motivation,'\n')
   time.sleep(4)
   print('Breathe out.')
   smallCircle()


def Meditation():
   print("Let's relax.")
   time.sleep(3)
   print("We will start with a simple breathing excercise.")
   for i in range(5):
       statement = Motivational_statements[random.randint(0,len(Motivational_statements))]
       Breathing(statement)
   print("You did amazing!\n")
   time.sleep(3)
   print('Now close your eyes for 15 seconds and imagine a warm light hugging you in a peaceful scene.\n')
   time.sleep(15)
   print('Feel, or follow, your breath go in and out of your body.\n')
   time.sleep(5)
   print('Close your eyes for 10 seconds and feel the sensations all over your body.\n')
   time.sleep(10)
   print('You did great! I hope you feel better.\n')
   print('Lastly, write anything you are feeling in the moment. This is a safe space.')
   input('Write your feelings here: \n')
   print('Thank you. Your feelings are valid.')




def vent_func():
    placer = ''
    while placer == '':
        vent = input('This is a safe space. You can say anything.') 
        length_vent = len(vent)  
        #---------------------------------------------------------
        if 'hurt' in vent:
            index_word = vent.index('hurt')
            slice_sentence = vent[index_word - 20 : index_word + 20]
            if 'myself' in slice_sentence or 'die' in slice_sentence:
                x = input('Would you like to call a suicide hotline in your country? 1 - yes // 2 - no')
                if x == '1':
                    HackathonSuicideLines.countries()
                elif x == '2':
                    pass
                x = input('Would you like to continue to talk? 1 - yes // 2 - no')
                if x == '1':
                    continue
                elif x == '2':
                    break
            else:
                print("It's okay. We are here for you.")
                x = input('Would you like to continue to talk?')
                if x == '1':
                    continue
                elif x == '2':
                    break
        #----------------------------------------------------------
        if 'kill' in vent: 
            index_word = vent.index('kill')
            slice_sentence = vent[index_word - 20 : index_word + 20]
            if 'kill myself' in slice_sentence:
                print("Take a deep breath. There are many things worth living for.")
                print("We recommend you call the suicide hotline in your country.")
                x = input('Would you like to call a suicide hotline in your country? 1 - yes // 2 - no')
                if x == '1':
                    HackathonSuicideLines.countries()
                elif x == '2':
                    break
                x = input('Would you like to continue to talk? 1 - yes // 2 - no')
                if x == '1':
                    continue
                elif x == '2':
                    pass
            else:
                print("It's okay. We are here for you.")
                x = input('Would you like to continue to talk?')
                if x == '1':
                    continue
                elif x == '2':
                    break
        #---------------------------------------------------------
        else:
            x = input('Are you done venting? 1 - yes // 2 - no')
            if x == '1':
                print("It'll be okay.")
                break
            elif x == '2':
                continue

def reasons_to_live():
    reasons_list = ["Your family", "You'll listen to your favorite song again", "Your friends", 
                    "Enjoying your favorite food", "See the sun again", "Reading your favorite book",
                    "Watching your favorite video", "Catching up with friends"]
    user_list = input("Think of some reasons to live:")
    x = input("Are you having trouble thinking of reasons? 1 - yes // 2 - no")
    placer = ''
    if x == '1':
        while placer == '':
            print('Here are some random reasons to live.')
            print(random.choice(reasons_list))
            x = input('Would you like to continue to generate reasons? 1 - yes // 2 - no')
            if x == '1':
                continue
            elif x == '2':
                break
    elif x == '2':
        pass

def anxiety_coping():
    anxiety_coping_list = ['Deep breathing', 'Regular exercise', 'Healthy eating', 'Adequate sleep',
                            'Less Caffiene and Alcohol', 'Hyrdration', 'Talk to someone', 'Meditation', 'Yoga']
    

def mental_health_bot():
    #teen pregancy, military trauma, postpartum depression, teengage mental health, anxiety, family abuse
    #able to contact nearby healthcare doctors, suicide hotlines, etc.
    #988 Suicide and Crisis Lifeline
    print('This program is designed to help military personel or their families.') 
    category = ''
    while category == '':    
        problem = input('What are you struggling with? Choose a certain catagory:'
                    '1 - Trauma // 2 - Depression // 3 - Anxiety // 4 - Suicide // 5 - Other')
        #--------------------------------------------------------------
        if problem == '1':
            category = input('1 - PTSD // 2 - Substance Use') 
            if category == '1':
                print("Remember that having an ongoing trauma response is normal.")
                print("Recovering is a slow process. You will heal, bit by bit.")
                list_recovery_methods = ['Muscle relaxation exercises', 'Breathing exercises', 'Meditation', 'Swimming', 
                                         'Stretching', 'yoga', 'Prayer', 'Listening to quiet music', 'spending time in nature']

                x = input('Would you like a random way of recovery? 1 - yes // 2 - no')
                if x == '1':
                    print(random.choice(list_recovery_methods))
                elif x == '2':
                    pass
            elif category == '2':
                x = input('Would you like some tips on substance use? 1 - yes // 2 - no')
                if x == '1':
                    print('Consult with a doctor or a addiction specialist to discuss treatment options.')
                    print('Avoid people or places that might trigger cravings and lead to substance use.')
                    print('Engage in hobbies and create a safe, supportive space.')
                    print('Finally, learn about addiction and coping methods.')
                elif x == '2':
                    pass
        #--------------------------------------------------------------
        elif problem == '2':
            category = 'depression'
            vent_func() #CALL VENT FUNC
            break
        #-------------------------------------------------------------
        elif problem == '3':
            category = input('1 - Anxiety Attacks // 2 - Panic Attacks // 3 - Seperation Anxiety')
            #CALL ANXIETY COPING 
            if category == '1':
                Meditation()
                break
                #Add meditation function here
            elif category == '2':
                Meditation()
                break
                #Add meditation function here
            elif category == '3':
                x = input('Would you like to hear some seperation anxiety coping methods? 1 - yes // 2 - no')
                if x == '1':
                    print("Gradually increase the time spent apart from the person or place you’re anxious about."
                          'Start with short periods and then slowly extend them.')
                    print("Stay connected with the person you have seperation anxiety with."
                           "Regular phone calls/ text messages would help.")
                    print("Focus in the positive face of seperation.")
                    x = input('Do you miss your family? 1 - yes // 2 - no')
                    if x == '1':
                        print('Think about good memories with them. You will see them soon.')
                        print('')
                break
        #--------------------------------------------------------------
        elif problem == '4': 
            category = 'suicide'
            print('Would you like to contact the suicide hotline?')
            a = input('1 - yes // 2 - no')
            if a == '1':
                HackathonSuicideLines.countries()
                pass
            elif a == '2':
                print('Would you like to talk?')
                a = input('1 - yes // 2 - no')
                if a == '1':
                    print('Enter venting mode:')
                    vent_func()
                    print('Entering reasons to live list:')
                    reasons_to_live()
                elif a == '2':
                    continue
            break
        #--------------------------------------------------------------
        elif problem == '5':
            x = input('We recommend that you find a therapist. Would you like to go back? 1 - yes // 2 - no')
            if x == '1':
                continue
            elif x == '2':
                break
            else:
                print('Invalid answer, returning to beginning...')
        #--------------------------------------------------------------
        else:
            print('Invalid answer, please use a number that is designated with an answer.')
            print('Returning to beginning...')
            continue

mental_health_bot()
print('If you would like more help, please rerun the program.')
#vent_func()
#reasons_to_live()



