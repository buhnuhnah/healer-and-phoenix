label start:
    $ centerTextbox = False;
    scene bg wasteland with fade
    play music "<loop 1.30>general drama.ogg" fadein 1.0
    voice "voice/start_48423cac.ogg"
    "The Oracle" "Once again the world is destroyed, ravaged by evil magic."
    "The Oracle" "How many times do you have to try, Phoenix, before you understand you can't save the world alone?"
    show phoenix at center with dissolve
    "Phoenix" "..."
    "Phoenix" "The gods made me the protector of this world."
    "The Oracle" "And you thought you'd have to bear this burden alone."
    "Phoenix" "Yes, but it's no use. I'm too weak..."
    "The Oracle" "You are not weak. Still, now you've seen it's an impossible task for one creature, no matter how powerful it is."
    "Phoenix" "I can't heal the infected animals. I need the help of a healer!"
    "Phoenix" "Oracle-"
    "The Oracle" "Once again, I'll send you back in time to a location in which a Healer will find you."
    "The Oracle" "But I too, am tired. I grow weary as my life force dwindles, thus I cannot bear the burden of using this kind of powerful magic anymore."
    "The Oracle" "This will be the last time I can help you this way, I am afraid I will have to use your own life force to do so."
    "The Oracle" "You will arrive hurt and dying."
    "Phoenix" "I understand, thank you for your help."
    "The Oracle" "Pray to the gods she finds you in time."

    scene black with dissolve
    play sound "sfx/time_travel.ogg"
    show white with Dissolve(0.1)
    pause 0.1
    hide white with Dissolve(0.1)
    pause 5
    jump ch1_s2

label ch1_s2:
    play sound "sfx/sudden_opening_of_the_door.ogg"
    play music "happy at work.ogg" fadein 1.0 loop
    scene cg max with fade
    pause 0.75
    m "Healer! Graciella is sick! Please, help her!"
    "I look up from the test I was doing on the microscope."
    "I see my long-term customer, Maximiano with his pet purrbear, Graciella in his arms."
    v "Hey! You shouldn't barge in here without knocking!"
    "My best friend and assistant Valencia calls Maximiano out of his behavior."
    "Normally I call in the patients myself, or sometimes she does, when we're ready to take care of the next pet."
    m "But! Graciella is in pain!"
    "The pet's owner looks about to burst into tears. His purrbear really looks sick."
    c "I only need to look at one more sample. I will be with you shortly."
    m "But-"

    $ vmood = 'worried'
    $ cmood = 'neutral'
    $ mmood = 'sad'
    $ gmood = 'sad'
    $ maxwithG = True
    scene bg vet day
    show catalina at flipCenter
    show valencia at right
    show max at left
    with fade

    play sound "sfx/channeling_magic_into_crystal.ogg"
    "I put the last sample into the microscope and channel my magic into the crystal to power it."
    "This is how all our devices are powered."
    "Even the lights and kitchen appliances have crystal batteries that we have to switch out every two weeks."
    "We replace them with new ones given to us."
    "There are powerful mages who work to channel magic into those crystals."
    "But smaller devices like this microscope can be activated by the user's magic."
    "The person has to be a magic user, of course."
    "Both my assistant and I, Catalina, are mages. Our specialization is healing mythical animals."
    "However, we also know some combat magic and are capable of using many advanced weapons."
    "Well, me more than Valencia - she's weaker when it comes to magic. That's why she didn't qualify as an independent healer."
    "She's told me repeatedly she's happy with the assistant position though."
    c "And done! Now show me Graciella, Maximiano."
    "Maximiano shows me the purrbear lying limp in his arms. She looks green in the face."
    m "She hasn't been eating since yesterday."
    c "Hmm..."
    "I touch the pet's stomach gently, and she hisses in pain."
    c "I think I know what the problem is..."

    scene black with dissolve
    stop music fadeout 1.0
    play music "<loop 8>minigame.ogg" loop
    jump tutorial

label ch1_s2a:
    stop music fadeout 1.0
    play music "happy at work.ogg" loop
    scene bg vet day
    show catalina at flipCenter
    show max at left
    show valencia at right
    with fade

    $ vmood = 'neutral'
    v "I'll hold Graciella for you."
    $ maxwithG = False
    show max with dissolve
    "Valencia grabs Graciella so that she can't see me coming to her from behind with the syringe."
    "Before the pet notices anything, I inject it."
    $ cmood = 'happy'
    c "There, all done!"
    "Graciella makes purring sounds, trying to get Valencia to pet her."
    $ vmood = 'happy'
    $ mmood = 'happy'
    v "Good girl!"
    "Valencia hugs the purrbear to her. Graciella sounds like one happy purrbear. It makes me so pleased to see an animal be so joyful."
    stop music fadeout 5
    m "You really are a wonderful healer, Miss Catalina..."
    "I look at Maximiano and smile brightly."
    $ mmood = 'surprised'
    m "Oh!"
    "He yelps, surprised."
    $ mmood = 'shy'
    play music "goofy.ogg" fadein 1.0
    m "Wait...Did I... did I say that out loud...?!"
    "It makes me want to tease him."
    c "Yes. Yes, you did!"
    "All the hugs made me want to hug someone too!"

menu:
    "Hug Valencia and Graciella":
        $ hugMax = False
        jump ch1_s2_2
    "Hug Maximiano":
        $ hugMax = True
        jump ch1_s2_3
    "That's a bad idea":
        $ hugMax = False
        jump ch1_s2_4

label ch1_s2_2:
    show catalina at rightish with move
    "I approach Valencia, who has Graciella in her arms, and hug them both."
    "Graciella seems to be happy with being between the two of us."
    $ mmood = 'shy'
    m "...how sweet."
    show catalina at flipRightish with dissolve
    c "Come join us!"
    "I smile at Maximiano brightly, urging him to join us in the hug, but he shakes his head."
    m "Thank you, but I'm good."
    $ cmood = 'sad'
    c "Daw..."
    "I make a sound of disappointment."
    $ cmood = 'neutral'

    show valencia at leftish
    show catalina at flipRight
    with move
    $ maxwithG = True
    pause 0.5
    show valencia at center with move

    "Eventually, we stop hugging. Valencia approaches Maximiano with his pet in her arms and hands Graciella over."
    jump ch1_s2_5

label ch1_s2_3:
    $ mmood = 'surprised'
    show catalina at flipLeftish with move
    "I approach Maximiano and before he can stop me from hugging him, I embrace him tightly."
    $ mmood = 'shy'
    m "Whoa!"
    "He's beet red, all the way to his ears."
    c "Hugging is healthy!"
    "Though I'm not doing it because I'm a healer. I simply wanted to hug Maximiano. He's just so cute!"
    m "Ahhhh....!"
    "Like now, when he's having a meltdown, waving his arms in the air, not knowing where to put them."
    show catalina at flipCenter with move
    "I let him go before his brain explodes."
    m "Miss Catalina..."
    "He has such pretty green eyes."
    $ vmood = 'happy'
    v "E-hem."

    show valencia at leftish
    show catalina at flipRightish
    with move
    $ maxwithG = True
    pause 0.5
    show valencia at center
    show catalina at flipRight
    with move

    "Valencia approaches us with Graciella in her arms. She hands the pet over to Maximiano."
    jump ch1_s2_5

label ch1_s2_4:
    $ cmood = 'neutral'
    $ vmood = 'neutral'
    $ mmood = 'neutral'
    "Maybe I shouldn't do it. It might feel too invasive to others if I suddenly embrace them."
    "As much as I like hugging, I need consent to do it."

    show valencia at leftish
    show catalina at flipRight
    with move
    $ maxwithG = True
    pause 0.5
    show valencia at center with move

    "Eventually, Valencia approaches Maximiano with Graciella in her arms. She hands the pet over to her owner."
    jump ch1_s2_5

label ch1_s2_5:
    $ vmood = 'happy'
    v "The payment?"
    $ mmood = 'shy'
    m "Ah, right."
    play sound "sfx/paying.ogg"
    pause 1
    show max at offscreenleft with move
    "Maximiano pays for our service, then exits the room."
    if hugMax:
        v "He's pretty cute, isn't he?"
        $ cmood = 'happy'
        c "That he is."
        "We giggle happily like two schoolgirls."
        "What? There's nothing wrong with appreciating how handsome our clients are. After all, we're helping their pets, not them."
    play music "happy at work.ogg" fadein 1.0
    "It's time for us to take on the next patient."
    c "I really love this job."
    "I say randomly, feeling very happy about healing another pet.."
    "I've been a mythical animal healer for a year now."
    "I graduated from a top university, and ever since then I've been running my own clinic with the help of my best friend Valencia."
    v "I love this job too."
    jump ch1_s3

label ch1_s3:
    $ cmood = 'happy'
    $ vmood = 'neutral'
    scene bg waiting day
    show catalina at flipCenter
    show valencia at right
    with fade
    play sound 'audio/sfx/clinic_loop.ogg'
    c "Now, who's next?"
    "I step into the waiting room of the clinic with a bright smile on my face."
    "I notice several pets with their owners, a colorful bunch waiting for me to solve their problems."
    "Which one should I chose?"
    jump animal_choice


label ch1_s3_1:
    "The navy-colored wonsh with the green underbelly is truly a beautiful creature."
    "However, the red light in its head is dim, suggesting it must be in immense pain."
    c "Can the owner of the wonsh please come in?"
    "Wonsh's Owner" "Thank you, Healer!"
    show bg vet day with dissolve
    "The wonsh's owner enters the doctor's room, carrying his pet in his arms."
    "This is concerning as the species normally slithers on its own."
    "Wonsh are usually quite independent and don't want to be carried."
    "I share a worried look with Valencia."
    "The man sets his pet on the surgery table."
    c "Before I take a look, could you tell me what happened?"
    "Wonsh's Owner" "My Mateo and I were playing catch in the fields."
    "Wonsh's Owner" "Suddenly Mateo hissed in pain and now he doesn't want to move on his own."
    stop music fadeout 3.0
    c "Hmm..."
    "Time to put the wonsh under inspection then!"
    jump second_minigame

label ch1_s3_1a:
    play music "happy at work.ogg" loop fadein 1.0
    c "There, all done! Just don't let Mateo slither for a few days, so the wound can heal properly."
    "Wonsh's Owner" "Thank you, Miss Catalina!"
    "The wonsh's owner pays for our services and leaves the doctor's room with the happy pet in arms."
    $ vmood = 'happy'
    v "A job well done!"
    $ cmood = 'neutral'
    $ vmood = 'neutral'

    if wonsh.done_with_minigame and flocto.done_with_minigame and lemurin.done_with_minigame:
        jump ch1_s4
    show bg waiting day with dissolve
    "Now whom should I chose next?"
    call screen choose_animal

label ch1_s3_2:
    "The flockto is a wonderful animal with its white spotted skin and colorful tentacles."
    "Most flocktos are usually extremely colorful, so it's quite amazing to see an albino one."
    $ cmood = 'worried'
    "However, I cannot truly admire its beauty when it's so clearly hurt"
    c "Can the flockto's owner please come in?"
    "Flockto's Owner" "Finally!"
    "The flockto's owner looks impatient as she enters the room, her pet floating in the air behind."
    show bg vet day with dissolve
    c "Tell me what happened."
    "Flockto's Owner" "Leonardo refuses to eat. Please do something about it."
    $ vmood = 'worried'
    stop music fadeout 3.0
    "I hold back a sigh. She doesn't exactly give much information. I will have to work with it regardless."
    "The owner can be rude all she wants but what's important is to save the pet from suffering."
    jump third_minigame

label ch1_s3_2a:
    $ cmood = 'neutral'
    $ vmood = 'neutral'
    play music "mystery.ogg" fadein 1.0 loop
    "Flockto's Owner" "Are they healed?"
    c "I took care of the worst of it, but please apply this medicine to Leonardo every day for the next four days."
    "Flockto's Owner" "If I must."
    c "And please don't feed the pet chocolate."
    "Flockto's Owner" "..."
    "The flockto's owner pays us and leaves the room without a goodbye."
    $ vmood = 'sad'
    v "Some people are really irresponsible."
    $ cmood = 'sad'
    c "I have a feeling this isn't the last time we are going to see this flockto and its owner."
    show bg waiting day with dissolve
    "I sigh and walk out of the doctor's room."
    $ cmood = 'neutral'
    $ vmood = 'neutral'
    play music "happy at work.ogg" loop
    if wonsh.done_with_minigame and flocto.done_with_minigame and lemurin.done_with_minigame:
        jump ch1_s4
    show bg waiting day with dissolve
    "Now whom should I chose next?"
    call screen choose_animal

label ch1_s3_3:
    "The lemurin with bright orange fur quivers in pain."
    $ cmood = 'worried'
    $ vmood = 'worried'
    "Lemurin's Owner" "Please help us, Healer!"
    c "On it!"
    show bg vet day with dissolve
    "The lemurin walks slowly and reluctantly behind its owner to the doctor's room."
    "I can feel its pain just by looking at it."
    c "What happened?"
    "Lemurin's Owner" "Emilia was playing with another lemurin of mine in a tree, when she suddenly fell from the branch."
    stop music fadeout 3.0
    "Lemurin's Owner" "Ever since then, she's been in a lot of pain and won't let even me touch her."
    c "Alright. I'll see what I can do."
    jump fourth_minigame

label ch1_s3_3a:
    $ cmood = 'happy'
    $ vmood = 'neutral'
    play music "happy at work.ogg" fadein 1.0 loop
    c "All done!"
    "Lemurin's Owner" "Thank you, oh thank you, healer!"
    "The lemurin's owner pays for the services and leaves, thanking us multiple times."
    $ vmood = 'happy'
    v "Excellent job!"
    c "Well, thank you!"
    $ cmood = 'neutral'
    $ vmood = 'neutral'

    if wonsh.done_with_minigame and flocto.done_with_minigame and lemurin.done_with_minigame:
        jump ch1_s4
    show bg waiting day with dissolve
    "I leave for the waiting room to see who's up next."
    call screen choose_animal

label ch1_s4:
    $ cmood = 'neutral'
    $ valencia = 'neutral'
    "With no more pets to heal, Valencia and I take a break for lunch."

    show bg vet sunset with dissolve
    show catalina at left with move

    "Later that day, after we've already closed the clinic for the day, and started our clean-up routine, Valencia smiles at me brightly."
    $ vmood = 'happy'
    v "Another day of work successfully completed!"

    $ results = wonsh.incorrect + flocto.incorrect + lemurin.incorrect

    if results < 3:
        voice "audio/minigame/voice/Scene 4/Catalina_055_take2.ogg"
        $ cmood = 'happy'
        c "Today was a great day!"
        "I can’t help the bright smile that appears on my face. I love my job and it brings me a lot of satisfaction."
        voice "audio/minigame/voice/Scene 4/Valencia_012_take1.ogg"
        v "Yes, and no major surgeries-"
        play sound "sfx/knocking1.ogg"
        $ cmood = 'neutral'
        $ vmood = 'neutral'
        "Our happiness is interrupted by loud banging on the entrance door."
        "It’s past opening hours, but that’s not the first time we find ourselves in this situation."
        stop music fadeout 5.0
        "I can’t say I’m surprised. Everything has gone too smoothly today."
    else:
        voice "audio/minigame/voice/Scene 4/Catalina_056_take1.ogg"
        $ cmood = 'sad'
        c "Today could have been better, but at least we made no major mistakes."
        "I smile at her softly. It certainly hasn’t been the best day in the history of the clinic, but still, I love my job."
        voice "audio/minigame/voice/Scene 4/Valencia_013_take2.ogg"
        v "Yes, and no major surgeries-"
        play sound "sfx/knocking1.ogg"
        $ cmood = 'neutral'
        "Our conversation is interrupted by loud banging on the entrance door."
        "It’s past opening hours, but that’s not the first time we find ourselves in this situation."
        stop music fadeout 5.0
        "I can’t say I’m surprised."

    $ cmood = 'worried'
    c "You might have said that too soon."
    $ vmood = 'worried'
    v "Oh no..."

    scene bg waiting sunset
    show catalina at offscreenright
    show valencia at offscreenright
    with fade
    show valencia at right
    show catalina at flipCenter
    with move
    play sound "sfx/knocking2.ogg"
    "I make my way to the entrance door, Valencia following me closely behind."
    "???" "Healer! We need your help!"
    play sound "sfx/sudden_opening_of_the_door.ogg"
    "There is a panicked man wearing a hard hat and plaid shirt on the outside of the entrance."
    "A lumberjack? But I see no sick animal with him. Oh no, is this an emergency call?"
    $ cmood = 'neutral'
    c "I'm here. How can I help?"
    play music "<loop 1.30>general drama.ogg" fadein 1.0
    "Lumberjack" "There's a burning bird in the forest just outside of town!"
    "Lumberjack" "We were working -  cutting trees and we found it there, lying there in a clearing!"
    "Lumberjack" "I swear we've done nothing! But it's on fire!"
    "That can't be what I think it is. I exchange a worried glance with Valencia."
    $ cmood = 'worried'
    c "Hold on, please don't panic. I'm not blaming you for anything."
    c "Tell me the state of the patient. Does it have any wounds?"
    "Lumberjack" "I don't know..."
    $ cmood = 'surprised'
    c "Has no one looked closely at the creature?"
    "Lumberjack" "No one dared to approach it! It's an inferno!"
    $ cmood = 'neutral'
    "The man looks shocked at my suggestion. I sigh, too tired to hide my annoyance."
    "Well, sometimes indifference is better than messing something up while trying to help."
    $ cmood = 'worried'
    c "Val, get the flying stretcher, my toolbox and four fire resistance potions."
    $ vmood = 'neutral'
    v "On it!"
    show valencia at flip
    show valencia at offscreenright with move
    play sound "sfx/leaving_and_closing_the_door.ogg"
    "Valencia leaves to prepare what we need to help our new patient."
    $ cmood = 'neutral'
    "It's time to try to calm down the man and get as much information out of him as I can."
    $ menuset = set()

menu:
    set menuset
    "Where is the patient exactly?":
        jump ch1_s4_2
    "Is the forest really not on fire?":
        jump ch1_s4_3
    "How long ago did you find the burning bird?":
        jump ch1_s4_4


label ch1_s4_2:
    $ menuset.add("Where is the patient exactly?")
    c "Can you tell me where exactly you found the burning bird?"
    "Lumberjack" "Not far away from town, it took me ten minutes to run over here from there!"
    "The man gestures to the left. That's indeed the way to the forest that surrounds the town."
    "There are no magical forests this close to us."
    "Magical forests are unstable, so there could be an explosion from the contact of the creature with the vegetation of such a forest."
    "The man doesn't look wounded though, and I heard no explosions. So I don't think he's lying about the location."
menu:
    set menuset
    "Where is the patient exactly?":
        jump ch1_s4_2
    "Is the forest really not on fire?":
        jump ch1_s4_3
    "How long ago did you find the burning bird?":
        jump ch1_s4_4
jump ch1_s4_5

label ch1_s4_3:
    $ menuset.add("Is the forest really not on fire?")
    c "You said the forest is not burning from the fire of the patient..."
    "Lumberjack" "I don't know how that's possible! The creature is clearly on fire!"
    "Well, I have my suspicions."
    "If there is no forest fire - and I can't see one from here - it cannot be a fire elemental that took on the shape of a bird."
    "That's good because a fire elemental is not a mythical animal."
    "It's an apparition made of pure magic of its corresponding element. There's nothing I could do to heal the force of nature."
menu:
    set menuset
    "Where is the patient exactly?":
        jump ch1_s4_2
    "Is the forest really not on fire?":
        jump ch1_s4_3
    "How long ago did you find the burning bird?":
        jump ch1_s4_4
jump ch1_s4_5

label ch1_s4_4:
    $ menuset.add("How long ago did you find the burning bird?")
    c "How long ago did you find the burning bird?"
    "Lumberjack" "Fifteen minutes ago! As soon as we saw the creature, we decided to go to you for help!"
    $ cmood = 'happy'
    show catalina happy
    c "Thank you for your faith in me."
    "Lumberjack" "Of course, you're known as the best animal healer in town!"
    "I nod, happy that my fame is spreading. Though with great fame comes great responsibility, as I think I'm about to discover..."
    $ cmood = 'neutral'
    show catalina
menu:
    set menuset
    "Where is the patient exactly?":
        jump ch1_s4_2
    "Is the forest really not on fire?":
        jump ch1_s4_3
    "How long ago did you find the burning bird?":
        jump ch1_s4_4
jump ch1_s4_5

label ch1_s4_5:
    $ vmood = 'neutral'
    $ cmood = 'neutral'
    show valencia at right with move
    show catalina at center with dissolve
    play sound "sfx/door_open.ogg"
    "After a while, Valencia comes back, the stretcher flying behind her."
    v "I have everything you've requested."
    c "Then let's go! No time to waste!"
    jump ch1_s5

label ch1_s5:
    scene bg road sunset
    show catalina at left
    show valencia at right
    with fade

    $ vmood = 'worried'
    $ cmood = 'worried'
    show valencia
    show catalina

    play music "gently foreboding.ogg" loop volume 1.0
    play sound "sfx/forest_amb_afternoon_loop.ogg" loop

    "We follow the man on the road leading out of town and soon we enter the forest. The trees rustle and move in the wind gently."
    "Nothing seems to indicate something bad has happened here."
    v "So... what do you think it is?"
    show valencia at rightish
    show catalina at leftish
    with move
    "Valencia takes me by the arm and we walk some distance behind the lumberjack."
    "He looks over his shoulder, but shrugs and keeps walking when he sees we're still following."
    c "I asked him some questions while you were preparing."
    v "And?"
    c "Well, first things first he seems like an honest man."
    c "I don't think he's lying about what he saw in the forest... which can only mean one thing."
    c "The forest around here is not magical, so it could very well catch on fire if he were dealing with a fire elemental."
    v "But it didn't?"
    c "No, it didn't. We would see the smoke from a distance."
    c "That means the fire the creature is producing is magical itself, so we are dealing with a mythical animal."
    v "There is only one fiery bird I know that's not a fire elemental and that's..."
    c "A phoenix, yes?"
    "We exchange worried glances when I give voice to what we are both suspecting."
    $ vmood = 'surprised'
    v "But no one has seen a phoenix in decades!"
    c "That's one of the things that worries me. Will we be able to heal it?"
    $ vmood = 'worried'
    v "I've only learned phoenix anatomy in books..."
    $ cmood = 'sad'
    c "Same here. I have no practical experience with such advanced beings."
    c "I was present once when a dragon was cured, but the only thing used back then was a lot of magic."
    c "And I really mean it when I say a lot of magic."
    c "They had to use a huge magical crystal and ten people had to channel healing magic through it."
    c "Only then did the spell to have enough power to not burn out mid-way."
    $ vmood = 'sad'
    v "Oh no..."
    $ cmood = 'sad'
    c "I hope I can do something for the phoenix, anything before it's too late."
    $ vmood = 'neutral'
    v "Let's not lose hope just yet. You're an excellent healer!"
    $ cmood = 'neutral'
    c "Thank you, but sometimes skill itself isn't enough."
    $ cmood = 'worried'
    c "There's one more thing worrying me..."
    v "Yes?"
    c "Why is a phoenix on the brink of death in the first place? What was strong enough to cause such an injury?"
    $ vmood = 'neutral'
    "We stare at each other in grim silence. There's few animals I consider strong enough to cause harm to a phoenix..."
    "And the presence of any of them so close to human homes is worrying."
    v "I hope we'll be able to find out from the type of injuries it has."
    c "Indeed."
    "The lumberjack stops in front of us, and gestures to the left."
    "Lumberjack" "We need to get off this path here! Come on, ladies!"
    v "We're coming!"
    show valencia at right
    show catalina at rightish
    with move
    "We leave the road and enter the forest proper. After walking for a few minutes we hear the worried voices of multiple people."
    play sound "sfx/campfire_loop.ogg" loop
    "A few steps more and we see a clearing with lumberjacks gathered around a campfire."
    show catalina at flipRightish with dissolve
    "Lumberjack" "The healer is here!"
    $ cmood = 'neutral'
    $ vmood = 'neutral'
    "The people greet us with excitement."
    "After saying hello, we follow the man who took us here a bit further into the forest... until we reach another clearing."
    jump ch1_s6

label ch1_s6:
    play sound "sfx/magical_aura_loop.ogg" loop
    stop music fadeout 1.0
    scene cg phoenix with fade
    $ cmood = 'surprised'
    $ centerTextbox = True
    pause 0.5
    voice "voice/ch1_s6_cat1.ogg"
    c "By the gods!"
    play music "edmundo sad.ogg" fadein 1.0
    "Shock paralyses me when I see the phoenix lying in the middle of the foliage."
    "Power is radiating off the creature -  a magnificent, fearsomely beautiful being."
    "I force myself to approach, knowing that even when hurt it could so easily kill me."
    "I remind myself it's my job to help no matter what."
    "When I see the extent of the phoenix' injuries, I wonder how it's still alive. It must be in a lot of pain."
    "Numerous cuts all around its body, feathers plucked out. It lies there unconscious."
    "There is also some sort of magic attached to its body. It's floating around the wounds, a dark shadow."
    "Curiosity overwhelming me, I put my finger into the swirling mass."
    $ cmood = 'pain'
    show cg phoenix at shake_screen
    play sound "sfx/magic_bite.ogg"
    c "Ow!"
    "Rather than a burn, it feels like a bite. But when I examine my hand there is no sign of injury. Did it bite my magical aura directly?"
    "For a moment I worry it might damage me somehow, but soon it stops hurting altogether."
    $ cmood = 'worried'
    c "Valencia, please bring the stretcher."
    $ vmood = 'neutral'
    v "On it!"
    "We brought the fire resistance potions with us, but if it's a phoenix there is no point in using them."
    "The creature won't burn the stretcher. Even in this severely wounded condition it seems to have control over its own flames."
    "Phoenixes only burn things with their fire when they want to."
    "The will of this one must be strong, since it's still protecting the world from itself."
    $ cmood = 'neutral'
    c "Hey! Could you help us pack the creature onto the stretcher?"
    c "It won't burn you, but watch out for the swirling black magic! It's painful."
    scene bg road day
    show catalina at left
    show valencia at right
    with fade
    $ centerTextbox = False
    "The lumberjacks look scared, but the man who walked us here and another approach."
    "Lumberjack" "Understood. We'll help."
    "I direct the two men on how to grab the bird properly. In no time it's on our stretcher and we set it to floating again."
    "We say our goodbyes. The lumberjacks seem relieved that the problem is out of their hands now."
    stop music fadeout 5.0
    "The stretcher floats behind it as we make our way back to the clinic."
    stop sound fadeout 1.0
    jump ch1_s7

label ch1_s7:
    play music "general drama.ogg" fadein 1.0
    scene bg vet sunset
    show valencia at right
    show catalina at left
    with fade
    $ cmood = 'worried'
    $ vmood = 'neutral'

    c "Let's lay the phoenix on the table."
    v "Yes!"
    "We carefully move the patient from the stretcher to the surgery table."

    jump fifth_minigame

label ch1_s7a:
    $ cmood = 'sad'
    $ vmood = 'sad'
    show bg vet night with dissolve

    "We try everything we can. Hours pass by. Whenever we manage to heal a wound, it opens again."
    $ cmood = 'angry'
    c "It must be the dark magic that's attached to the phoenix's body."
    v "You're right. We need someone magically stronger than us to join us and help detach whatever that darkness is from the patient."
    "Someone magically stronger... but whom should I call? I'm stronger than all the other healers in town."
    $ vmood = 'neutral'
    v "How about Die-"
    c "No."
    "I answer quickly. I don't want to call on that person for any reason."
    $ cmood = 'neutral'
    c "He's in Gerla anyway. Do you think he would come to Girasol just because I need something?"
    $ vmood = 'happy'
    v "Yes, he will."
    $ cmood = 'surprised'
    "Valencia answers with a bright smile. I stare at her like she just grew a second head."
    c "Do you hear yourself? He lives in Gerla's capital now, that's a week's journey from here!"
    v "Not if he uses a portal!"
    c "But that's so expensive!"
    v "Diedriech isn't exactly poor, is he?"
    $ cmood = 'neutral'
    "Well no, he certainly isn't poor. Diedriech is about as rich as I am."
    "My parents gifted me this whole building when I graduated with flying colors."
    "Considering that, Diedriech definitely has the money for a portal."
    $ cmood = 'sad'
    c "I still don't think that's a good idea."
    $ vmood = 'neutral'
    v "If he can't come, no biggie. But trust me, he will be happy that you want to rely on him for something."
    $ cmood = 'neutral'
    "I can't understand why he would be."
    "Diedriech and I have been rivals throughout all of our university years. We were like fire and water, always bickering."
    "Somehow the Gerlan never left me alone, always coming to me to tease me about this and that."
    "When university ended, I moved back to my parents' hometown of Zalila."
    "Diedriech returned to Gerla to take over his parents' healing clinic for mythical creatures."
    "It's been a year since I last heard from him."
    "And now suddenly I'm supposed to contact him, because I'm in distress?"
    $ cmood = 'sad'
    "I look at the phoenix, lying there on my table, hurt and dying."
    "The thing that's stopping me from calling Diedriech is... pride. And that's stupid. I have to put those uncomfortable feelings aside."
    c "I'll call him."
    $ vmood = 'happy'
    v "Great! I'll stay here."
    "I nod at Valencia and step out of the room."
    jump ch1_s8
