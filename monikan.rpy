init -990 python in mas_submod_utils:
    monikan=Submod(
        author="CLoggermore",
        name="Monikan", # Title is WIP
        description="Based off my perspectives of Monika",
        version="0.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
    
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod=store.mas_submod_utils.monikan
            user_name="CLarramore",
            repository_name="monikan",
            update_dir=""
        )