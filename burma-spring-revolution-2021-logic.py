ငါလုပ်တာ = True
ခရီးသွား = True
ပုံတင် = True
ခိုးသွား = False

# def ခိုးသွား():
#     if trip and not social_meida_post:
#         ခိုးသွား = True

def empathy_logic():
    print("empathy_logic")

def လောင်():
    print("လောင်")

if ငါလုပ်တာ:
    print("ALL OK")
else:
    if ခရီးသွား and ပုံတင်:
        လောင်()
    elif ခရီးသွား and not ပုံတင်:
        empathy_logic()
