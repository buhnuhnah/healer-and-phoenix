# CHARACTER DESCRIPTORS FOR SPRITES
$ cmood, mmood, vmood, emood, dmood, gmood = 'neutral', 'neutral', 'neutral', 'neutral', 'neutral', 'neutral'
$ maxwithG = False


# CHARACTER DEFINITIONS

define character.c = Character("Catalina", voice_tag="catalina", side_image="avatar/avatar_catalina.png")
image catalina = ConditionSwitch(
    "_last_say_who == 'c'", "images/catalina/catalina [cmood] talk.png",
    "True", "images/catalina/catalina [cmood].png")

define character.m = Character("Max", voice_tag="max", side_image="avatar/avatar_max.png")
image max = ConditionSwitch(
    "_last_say_who == 'm' and not maxwithG", "images/max/max [mmood] talk.png",
    "_last_say_who == 'm' and maxwithG", "images/max/max [mmood] talk graciella [gmood].png",
    "maxwithG", "images/max/max [mmood] graciella [gmood].png",
    "True", "images/max/max [mmood].png")

define character.v = Character("Valencia", voice_tag="valencia", side_image="avatar/avatar_valencia.png")
image valencia = ConditionSwitch(
    "_last_say_who == 'v'", "images/valencia/valencia [vmood] talk.png",
    "True", "images/valencia/valencia [vmood].png")

define character.e = Character("Edmundo", voice_tag="edmundo", side_image="avatar/avatar_edmundo.png")
image edmundo = ConditionSwitch(
    "_last_say_who == 'e'", "images/edmundo/ed [emood] talk.png",
    "True", "images/edmundo/ed [emood].png")

define character.d = Character("Diedriech", voice_tag="diedriech", side_image="avatar/avatar_diedriech.png")
image diedriech = ConditionSwitch(
    "_last_say_who == 'd'", "images/diedriech/diedriech [dmood] talk.png",
    "True", "images/diedriech/diedriech [dmood].png")

image phoenix = "images/animals/phoenix.png"
