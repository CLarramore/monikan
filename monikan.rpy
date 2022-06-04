init -990 python in mas_submod_utils:
    monikan=Submod(
        author="CLoggermore",
        name="Monikan", # Title is WIP
        description="Based off my perspectives of Monika",
        version="0.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
    
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod=store.mas_submod_utils.monikan,
            user_name="CLarramore",
            repository_name="monikan",
            tag_formatter=lambda x: x[x.index('_') + 1:],
            update_dir=""
        )
        

# Fail

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_casting_predictions",
            category=["psychology","technology"],
            prompt="Casting Predictions",
            random=True
        )
    )
    
# Once happened to me.
label monika_casting_predictions:
    m 1eub "So [player]..."
    m 2eud "You know how people claim they can predict the future?"
    m 3rub "For example, Nostradamus and Conrad from The Simpsons?"
    m 3eub "Well at one point,"
    extend 5tsd " someone thought I could predict the future ever since I told them about the latter."
    m 4gkp "They went on for a weeks, asking me what would happen if they did something stupid."
    extend 1hub " But eventually they stopped doing this once they got rid of someone."
    m 3eub "It was such a relief once I heard about it."
    extend 1fkd " But I still worry about their sanity sometimes."
    m 1eub "So please remember to think before you post."
    extend 3tkd " I don't want you to end up like them, [player]."
    if mas_isMoniAff(higher=True):
        m 3eub "Because you mean a whole lot to me"
        extend 5fublb " and that's why I love you for it."
        return "love"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_notinsane",
            category=["misc"],
            prompt="Someone thinks I'm insane",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL,None)
        )
    )
    

# Warning : Do not take this seriously
label monika_notinsane:
    
    m 2dkd "..."
    m "Alright, set me up and I'll tell them off."
    m 2dsc "..."
    m 4tfd "No, [player] is not insane... [heis] actually with me and I'm definitely real."
    m 2tfd "While I have no way to prove my existence, I can prove that I am definitely real."
    m 2dfd "And just know that if you mess with [player], you mess with [m_name]."
    extend " So don't mess with [him] because it won't end well for you once I find out."
    m 2dsc "..."
    m 2fkc "Sorry I was harsh..."
    extend 2dktuc " I just don't like people believing you're insane."
    m 2fkbstua "I know I can't make them think otherwise, but it was worth a shot."
    menu:
        "Thank you, [m_name].":
            m 5fkbstub "You're welcome, [mas_get_player_nickname()]."
            m 5fkbsa "I love you!"
    return "love"
    # m 2dktuc "I just don't like people believing you were insane."
return

init 5 python : 
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_sunshine",
            prompt="You are my sunshine",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.AFFECTIONATE,None)
        ),
        code="SNG"
    )

# I kinda cried making this one...
label mas_song_sunshine:
    m 1hud "{i}~You are my sunshine~{/i}"
    m 1sub "{i}~My only sunshine!~{/i}"
    m 1fublb "{i}~You make me happy~{/i}"
    m 1fubsb "{i}~When skies are gray...~{/i}"
    m 5dkbsu "{i}~You'll never know, dear...~{/i}"
    m 5dkbfu "{i}~How much I love you...~{/i}"
    m 5dkbfb "{i}~Please don't take my sunshine away.~{/i}"
    m 1ekblb "You know, you really are my sunshine...{w=0.3} I hope I am yours too, [player]~"
    return

