import random

cards = []
distCards = {
    "1": [],
    "2": [],
    "3": [],
    "4": []
}
def cardsDst(playersCnt):
    for i in range(13):
        cards.append(('Red' , i+1))
    for i in range(13):
        cards.append(('Yellow' , i+1))
    for i in range(13):
        cards.append(('Blue' , i+1))
    if(playersCnt == 4):
        for i in range(13):
            cards.append(('Green' , i+1))
    
    for i in range(13):
        x = random.randint(0 , len(cards)-1)
        distCards["1"].append(cards[x])
        cards.pop(x)
    distCards["1"].sort()
    for i in range(13):
        x = random.randint(0 , len(cards)-1)
        distCards["2"].append(cards[x])
        cards.pop(x)
    distCards["2"].sort()
    for i in range(13):
        x = random.randint(0 , len(cards)-1)
        distCards["3"].append(cards[x])
        cards.pop(x)
    distCards["3"].sort()
    
    if(playersCnt == 4):
        for i in range(13):
            x = random.randint(0 , len(cards)-1)
            distCards["4"].append(cards[x])
            cards.pop(x)
        distCards["4"].sort()
    keybordLayouts = distCards
    


