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