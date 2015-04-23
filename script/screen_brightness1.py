choices = [" -0.0", " -0.1", " -0.2", " -0.3", " -0.4", " -0.5", " -0.6", " -0.7", " -0.8", " -0.9", " -1.0"]
retCode, choice = dialog.list_menu(choices, height="370", title="Brightness")
if retCode == 0:
    system.exec_command("sh ~/Documents/bash/test" + choice)