system.exec_command("xkbset m")
system.exec_command("xmodmap -e \"keycode 54 = Pointer_Button1\"")
system.exec_command("xmodmap -e \"keycode 39 = Pointer_Button2\"")
system.exec_command("xmodmap -e \"keycode 38 = Pointer_Button3\"")
dialog.info_dialog(message="stan_clicks on!")