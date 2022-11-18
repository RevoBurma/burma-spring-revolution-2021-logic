ငါလုပ်တာ = True

မတရားသေနေပြီဆိုပုံတင်တဲ့ဟာတွေ = True
fb_storyတင် = True
igတင် = True
ခရီးသွား = True
ပုံတင် = True

ခိုးသွား = True

# def setter_ခိုးသွား():

def မတရားလောင်():
    print("မတရားလောင်")

def လောင်():
    print("လောင်")

def empathy_logic():
    print("empathy_logic")

def စဆရက_all_ok_logic():
    print("စဆရက_all_ok")

def main():
    if ငါလုပ်တာ:
        စဆရက_all_ok_logic()
    else:
        if မတရားသေနေပြီဆိုပုံတင်တဲ့ဟာတွေ:
            မတရားလောင်()
        elif ခရီးသွား and ပုံတင်:
            လောင်()
        elif fb_storyတင်:
            empathy_logic()
        elif igတင်:
            empathy_logic()
        elif ခိုးသွား:
            empathy_logic()

if __name__ == '__main__':
    main()
