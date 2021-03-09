# for loop that runs a certain # times
#     ask question
#         check answer
#         +=1 variable
#     ask another question
#         check answer
#         +=1 variable
#     ask third question
RATQ1 = """
    QUESTION ONE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I'm consistent and reliable, but not flexible enough.\n   b. I'm flexible and changebable,  but lack consistency.
    """
RATQ2 = """
    QUESTION TWO\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. A bad mood has little impact on my productivity.\n   b. I'm strongly dependant on my internal biorhythms.
    """
RATQ3 = """
    QUESTION THREE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I do not start something new until I've finished the previous task.\n   b. Usually, I start several projects at once.
    """
EXTQ1 = """
    QUESTION FOUR\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I am an open person.\n   b. I am a reserved person.
    """
EXTQ2 = """
    QUESTION FIVE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. Contacts with strangers do not bother me.\n   b. Contacts with strangers require effort.
    """
EXTQ3 = """
    QUESTION SIX\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. It is easier for me to understand others than myself.\n   b. It is easier for me to understand myself than others.
    """
SENQ1 = """
    QUESTION SEVEN\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. If nothing is clear, I actively collect information\n   b. If nothing is clear, I rely on my intuition.
    """
SENQ2 = """
    QUESTION EIGHT\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I see everything that happens around me.\n   b. I see only what I attach importance to.
    """
SENQ3 = """
    QUESTION NINE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I see better ways of achieving a goal.\n   b. I see a goal better than the ways to achieve it.
    """
LOGQ1 = """
    QUESTION TEN\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I live more by reason than by heart.\n   b. I live more with my heart than with my mind.
    """
LOGQ2 = """
    QUESTION ELEVEN\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. I react more to the content of the conversation.\n   b. I am very responsive to the intonation of the speaker.
    """
LOGQ3 = """
    QUESTION TWELVE\nPlease enter 'a' if the first statement is mostly true, or 'b' if the second statement is mostly true.\n   a. It is better to prove than to persuade.\n   b. It is better to persuade than to prove.
    """
RATEX = """
    The following questions will aim to sort you into one of the 4 Jungian dichotomies, rationality and irrationality.\nThe former bases judgement on actions and truths while the latter is governed by perceptions of the mind and body.
    """
EXTEX = """
    These next questions will see where on the extroversion and introversion spectrum you lean more towards.
    """
SENEX = """
    The sensing vs intuition dichotomy are understood as mental processes where sensing types focus on experience with the concrete and\ntangible, whereas intuitive types are receptive of the intangible details of reality, say for instance time/trend.
    """
LOGEX = """
    The next questions will sort based on the final Jungian dichotomy, logic vs ethics, rational judgement involving inanimate objects\nand systems ("right or wrong") and rational judgement involving interpersonal relations ("good or evil").
    """
ESE = """
                                    YOU ARE...

                                                E S E
                                            4D Fe | 3D Si
                                            1D Ni | 2D Te
                                            2D Ne | 1D Ti
                                            3D Fi | 4D Se
    ESEs, with strong extraverted ethics (Fe), are lively, animated, and are skilled at creating emotional ambience and energizing others wherever they go. They are highly intuned with their inner homeostasis and love creating comfort for themselves and those around them due to favoring introverted sensing (Si). They tend to have a good eye for aesthetics and enjoy organizing events for loved ones.
    """
LII = """
                                    YOU ARE...

                                                LII
                                            4D Ti | 3D Ne
                                            1D Se | 2D Fi
                                            2D Si | 1D Fe
                                            3D Te | 4D Ni
    LIIs are known to be the strong analytical types due to their 4 dimensional introverted thinking (Ti). They are usually able to understand abstract systems and conceptualize, compartmentalize them. If they could be left to think and research for a living, they would reach self-actualization. With extroverted intuition (Ne), they are able to see the big picture and ways of realizing their ideas.
    """
ILE = """
                                    YOU ARE...

                                                ILE
                                            4D Ne | 3D Ti
                                            1D Fi | 2D Se
                                            2D Fe | 1D Si
                                            3D Ni | 4D Te
    ILEs are creative thinkers who love ideas purely for their unlimited 
    """
SEI = """
                                    YOU ARE...

                                                SEI
                                            4D Si | 3D Fe
                                            1D Te | 2D Ni
                                            2D Ti | 1D Ne
                                            3D Se | 4D Fi
    """
EIE = """
                                    YOU ARE...

                                                EIE
                                            4D Fe | 3D Ni
                                            1D Si | 2D Te
                                            2D Se | 1D Ti
                                            3D Fi | 4D Ne
    """
LSI = """
                                    YOU ARE...

                                                LSI
                                            4D Ti | 3D Se
                                            1D Ne | 2D Fi
                                            2D Ni | 1D Fe
                                            3D Te | 4D Si
    """
SLE = """
                                    YOU ARE...

                                                SLE
                                            4D Se | 3D Ti
                                            1D Fi | 2D Ne
                                            2D Fe | 1D Ni
                                            3D Si | 4D Te
    """
IEI = """
                                    YOU ARE...

                                                IEI
                                            4D Ni | 3D Fe
                                            1D Te | 2D Si
                                            2D Ti | 1D Se
                                            3D Ne | 4D Fi
    """
LIE = """
                                    YOU ARE...

                                                LIE
                                            4D Te | 3D Ni
                                            1D Si | 2D Fe
                                            2D Se | 1D Fi
                                            3D Ti | 4D Ne
    """
ESI = """
                                    YOU ARE...

                                                ESI
                                            4D Fi | 3D Se
                                            1D Ne | 2D Ti
                                            2D Ni | 1D Te
                                            3D Fe | 4D Si
    """
SEE = """
                                    YOU ARE...

                                                SEE
                                            4D Se | 3D Fi
                                            1D Ti | 2D Ne
                                            2D Te | 1D Ni
                                            3D Si | 4D Fe
    """
ILI = """
                                    YOU ARE...

                                                ILI
                                            4D Ni | 3D Te
                                            1D Fe | 2D Si
                                            2D Fi | 1D Se
                                            3D Ne | 4D Ti
    """
IEE = """
                                    YOU ARE...

                                                IEE
                                            4D Ne | 3D Fi
                                            1D Ti | 2D Se
                                            2D Te | 1D Si
                                            3D Ni | 4D Fe
    """
SLI = """
                                    YOU ARE...

                                                SLI
                                            4D Si | 3D Te
                                            1D Fe | 2D Ni
                                            2D Fi | 1D Ne
                                            3D Se | 4D Ti
    """
LSE = """
                                    YOU ARE...

                                                LSE
                                            4D Te | 3D Si
                                            1D Ni | 2D Fe
                                            2D Ne | 1D Fi
                                            3D Ti | 4D Se
    """
EII = """
                                    YOU ARE...

                                                EII
                                            4D Fi | 3D Ne
                                            1D Se | 2D Ti
                                            2D Si | 1D Te
                                            3D Fe | 4D Ni
    """

def print_intro():
    """Prints the title & gives brief intro of quiz"""
    print("                                                   SOCIONICS TYPE QUIZ\n")
    
    print("     Socionics is a personality system and theory based closely on Carl Jung's Psychological Types. In contrast to other personality\n  theories, Socionics has the concept of intertype relations that makes it worth studying. Today you will be taking a quiz that will\n  pick a sociotype among 16 that you are most likely to have affinity for. If the sociotype you recieve after the quiz does not\n  resonate with you, do not worry as you can read more about the theory online and find out which type you truly are.\n\n                                                   Thank you and enjoy!\n")

def ratvs_irrat(socio):
    """ Loops through series of questions on rationality vs irrationality
    based on answers, socio at index 0 is updated """

    rat_count = 0
    irrat_count = 0
    rat_irrat = (RATQ1, RATQ2, RATQ3)
    print(RATEX)
    for q in rat_irrat:
        print(q)
        answer = input("> ").lower()
        if answer == "a":
            rat_count+=1
        else:
            irrat_count+=1
    if irrat_count > rat_count:
        socio[0] = 1
    return socio

def extvs_int(socio):
    """ Loops through eries of questions on extroversion vs introversion
    based on answers, socio at index 1 is updated """

    extro_count = 0
    intro_count = 0
    extro_intro = (EXTQ1,EXTQ2, EXTQ3)
    print(EXTEX)
    for q in extro_intro:
        print(q)
        answer = input("> ").lower()
        if answer == "a":
            extro_count+=1
        else:
            intro_count+=1
    if intro_count > extro_count:
        socio[1] = 1
    return socio

def senvs_int(socio):
    """ Loops through series of questions on sensing vs intuition
    based on answers, socio at index 2 is updated """

    sen_count = 0
    intui_count = 0
    sen_intui = (SENQ1,SENQ2, SENQ3)
    print(SENEX)
    for q in sen_intui:
        print(q)
        answer = input("> ").lower()
        if answer == "a":
            sen_count+=1
        else:
            intui_count+=1
    if intui_count > sen_count:
        socio[2] = 1
    return socio

def logvs_eth(socio):
    """ Loops through series of questions on logical vs ethical
    based on answers, socio at index 3 is updated """
    
    log_count = 0
    eth_count = 0
    log_eth = (LOGQ1,LOGQ2, LOGQ3)
    print(LOGEX)
    for q in log_eth:
        print(q)
        answer = input("> ").lower()
        if answer == "a":
            log_count+=1
        else:
            eth_count+=1
    if eth_count > log_count:
        socio[3] = 1
    return socio

def get_sociotype(socio):
    """ Loops through sociotype dictionary to find user match """

    sociotype = {
        "ESE": [0,0,0,1],
        "LII": [0,1,1,0],
        "ILE": [1,0,1,0],
        "SEI": [1,1,0,1],
        "EIE": [0,0,1,1],
        "LSI": [0,1,0,0],
        "SLE": [1,0,0,0],
        "IEI": [1,1,1,1],
        "LIE": [0,0,1,0],
        "ESI": [0,1,0,1],
        "SEE": [1,0,0,1],
        "ILI": [1,1,1,0],
        "IEE": [1,0,1,1],
        "SLI": [1,1,0,0],
        "LSE": [0,0,0,0],
        "EII": [0,1,1,1]
    }
    
    for personality in sociotype:
        if sociotype[personality] == socio:
            return personality
            

def type_blurb(personality):
    """ Parses through dictionary of type and prints user a blurb about their type """
    
    type_and_blurb = {
        "ESE": (ESE),
        "LII": (LII),
        "ILE": (ILE),
        "SEI": (SEI),
        "EIE": (EIE),
        "LSI": (LSI),
        "SLE": (SLE),
        "IEI": (IEI),
        "LIE": (LIE),
        "ESI": (ESI),
        "SEE": (SEE),
        "ILI": (ILI),
        "IEE": (IEE),
        "SLI": (SLI),
        "LSE": (LSE),
        "EII": (EII)
    }
    
    for key in type_and_blurb:
        if key == personality:
            print(type_and_blurb[key])

def play_game():
    """ Function calls all functions above to run the terminal quiz """

    print_intro()

    user_sociotype = [0,0,0,0]
    user_sociotype = ratvs_irrat(user_sociotype)
    user_sociotype = extvs_int(user_sociotype)
    user_sociotype = senvs_int(user_sociotype)
    user_sociotype = logvs_eth(user_sociotype)
    result = get_sociotype(user_sociotype)
    blurb = type_blurb(result)
    return blurb

print(play_game())