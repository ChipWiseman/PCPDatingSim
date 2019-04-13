
#Characters
init python:
    def hippo_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("")#TODO: this
        elif event == "slow_done":
            renpy.sound.stop()
define player = Character("[player_name]")

define Jesse = Character("{color=#ffe300}???{/color}", what_color = "#ffe300")#, callback=hippo_voice)

define Hippo = Character("{color=#61ffe0}???{/color}", what_color = "#61ffe0", image = "hippo")#, callback=hippo_voice)
layeredimage hippo:
    group body auto:
        attribute campusstanding default

    group face auto:
        attribute campusneutral default

    attribute blushies if_any "blushies"


define Nate = Character("{color=#7bff00}???{/color}", what_color = "#7bff00", image = "nate")
layeredimage nate:
    group body auto:
        attribute campusstanding default

    group face auto:
        attribute campusneutral default

    attribute blushies if_any "blushies"
    attribute glasses if_any "glasses"

define Munchy = Character("{color=#ff80d4}???{/color}", what_color = "#ff80d4", image = "munchy")
layeredimage munchy:
    group body auto:
        attribute campusstanding default

    group face auto:
        attribute campusneutral default

    attribute blushies if_any "blushies"

define Digibro = Character("{color=#ff007d}???{/color}", what_color = "#ff007d", image = "digi")
layeredimage digi:
    group body auto:
        attribute campusstanding default

    group face auto:
        attribute campusneutral default

    attribute blushies if_any "blushies"

define Mage = Character("{color=#d052ff}???{/color}", what_color = "#d052ff", image = "mage")
layeredimage mage:
    group body if_not "silhouete" auto:
        attribute campus1 default

    group face if_not "silhouete" auto:
        attribute campusneutral default

    attribute blushies if_any "blushies"
    attribute silhouete if_any "silhouete"

define Tom = Character("{color=#ff0100}???{/color}", what_color = "#ff0100", image = "tom")
layeredimage tom:
    group body auto:
        attribute campus1 default

    group face auto:
        attribute campusneutral default

    attribute blushies if_any "blushies"

define n11 = Character("???", what_color = "#ffffff")
image 911 Boi = Movie(play="images/Characters/911/911_boi.webm",mask="images/Characters/911/911_boi_alpha.webm")
image 911 Concern = Movie(play="images/Characters/911/911_concern.webm",mask="images/Characters/911/911_concern_alpha.webm")
image 911 Pewpew = Movie(play="images/Characters/911/911_pewpew.webm",mask="images/Characters/911/911_pewpew_alpha.webm")
image 911 Standing = Movie(play="images/Characters/911/911_standin.webm",mask="images/Characters/911/911_standin_alpha.webm")
image 911 silhouete = "images/Characters/911/911_silhouete.png"

define Thoth = Character("Thoth", what_color = "#ffffff", image = "thoth")

define AG = Character("Action Giraffe", what_color = "#ffffff", image = "ag")
layeredimage ag:
    group body auto:
        attribute campusa default

    group face auto:
        attribute campusneutral default

define EW = Character("???", what_color = "#ffffff", image = "ew")
layeredimage ew:
    group body if_not "silhouete" auto:
        attribute campusstand default

    group face if_not "silhouete" auto:
        attribute standneutral default

    group blushies if_any ["campusblush1","campusblush2","campusblush3"] if_not "silhouete" auto:
        attribute stand1 default

    attribute silhouete if_any "silhouete"
