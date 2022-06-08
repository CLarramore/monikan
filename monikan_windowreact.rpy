

# If and when I return to WoW... 
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_wow",
            category=["World of Warcraft"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_wow:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "You still pay for a WoW sub or is this a private server, [mas_get_player_nickname()]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_wow')
    return


# YFM
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yfm",
            category=["Your Favorite Martian"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yfm:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Is this that band everyone was talking about?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_yfm')
    return