init 5 python:
    # Player-initiated topic
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_guitar_listening",
            category=["music"],
            prompt="Can I play guitar for you?",
            pool=True,
            unlocked=True
        )
    )

    # Random topic - now less frequent
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_guitar_random",
            conditional="True",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.NORMAL, None),
            rules={"no repeat": None}  # Prevents immediate repeats
        )
    )

label monika_guitar_listening:
    if persistent._mas_guitar_playing:
        m 1ekbfa "Ready to keep playing, [player]? {w=0.5}Ehehe~"
    else:
        m 1eua "You want to play guitar for me? That's so sweet!"
        m 3hub "I'd love to listen!"
    
    m 1eua "I'm all ears~ Just play when you're ready."  # Changed to open-eyed listening
    $ persistent._mas_guitar_playing = True

    # Listening mode - now with open eyes
    m 1ekbfa "..."  # Changed from 1dsc (closed eyes) to 1eua (open eyes)

    # Player clicks to end
    m 1hua "Done already? {w=0.5}Or just taking a break?"
    menu:
        "I'm finished playing":
            $ persistent._mas_guitar_playing = False
            if mas_isMoniEnamored(higher=True):
                $ mas_gainAffection(5, bypass=True)
                m 1sub "That was absolutely breathtaking, [player]!"
                m 1ekbfa "Every note you play makes my heart flutter..."
            
            elif mas_isMoniHappy(higher=True):
                $ mas_gainAffection(3, bypass=True)
                m 1sua "That was wonderful, [player]!"
                m 1eka "It's so relaxing to hear you play..."
            
            else:
                $ mas_gainAffection(1, bypass=True)
                m 1eua "That was really nice, [player]."
        
        "Just taking a break":
            m 1ekbla "I'll wait right here, [player]~"
            jump monika_guitar_listening
    return

label monika_guitar_random:
    if mas_isMoniEnamored(higher=True):
        $ random_chance = renpy.random.randint(1, 3)
        if random_chance == 1:
            m 1ekbfa "[player]..."
            m 3ekbfa "I was just thinking about your guitar playing..."
            m 1hubfa "Would you play something for me when you have time?"
        elif random_chance == 2:
            m 1ekbfa "[player]..."
            m 3ekbfa "I keep thinking about your guitar playing..."
            m 1hubfa "Would you play for me again soon?"
        else:
            m 1ekbfa "Mmm, [player]..."
            m 3ekbfa "I can still hear your last guitar melody in my heart~"
            m 1hubfa "Play for me again sometime?"

    elif mas_isMoniHappy(higher=True):
        $ random_chance = renpy.random.randint(1, 2)
        if random_chance == 1:
            m 1ekbfa "[player]..."
            m 3eub "I've been craving some of your guitar playing lately!"
            m 1hua "It always makes me smile~"
        else:
            m 1ekbfa "[player]..."
            m 3eub "I'd love to hear you play guitar again!"
            m 1hua "You always play so beautifully~"

    else:
        $ random_chance = renpy.random.randint(1, 2)
        if random_chance == 1:
            m 1eua "Hey, [player]..."
            m 3eub "Feel like playing guitar sometime soon?"
            m 1hua "I always enjoy listening to you~"
        else:
            m 1eua "Hey, [player]..."
            m 3eub "Have you been practicing guitar lately?"
            m 1hua "I'd love to hear you play~"
    
    return