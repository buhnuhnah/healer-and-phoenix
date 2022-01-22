label ch1_s8:
    $ cmood = 'sad'
    scene bg waiting night
    show catalina at flipCenter
    with fade

    "I look out of the window to see the moon shining brightly in the sky."
    "It's the middle of the night! Is it okay to wake up Diedriech now?"
    "But... My patient doesn't exactly have much time left and if Diedriech could portal to Zalila, it would only take a few hours."
    "I suspect we don't have enough time to wait until the more call-appropriate hours of morning."
    show catalina at left with move
    "I approach the large standing mirror with its complicated ornaments that hide the magical formulas for long-distance communication."
    c "Here goes nothing..."
    "I place my hand on the mirror's surface and think hard about Diedriech - his appearance when I last saw him, his location."
    "Then I channel my magic into the device."
    "I wait for a bit ... hoping he'll answer."

    scene cg diedriech with fade
    pause 0.5

    "When I finally see his face, those handsome features I haven't seen in so many months, I feel a wave of relief hit me."
    "I will be able to save the phoenix. I..."
    d "Catalina?...It's so late- why are you crying?!"
    "He's dressed in his everyday clothes and looks tired. I probably caught him after a long night of surgery."
    d "If anyone hurt you, I swear I will-"
    c "I'm okay..."
    "Only then do I realize I'm crying, and wipe the tears off of my face."
    c "I'm sorry, I just felt so relieved to see you..."
    d "I... see..."
    c "I have a problematic patient here and I can't save them alone. I-I need your help."
    "Diedriech looks at me with a solemn expression."
    d "I'll be there as soon as I can. If I use the portals, I should arrive in four hours."
    "Wait? He agreed so easily?"
    c "Ah! But I didn't even explain what the problem is!"
    "Diedriech smiles softly at me."
    voice "voice/ch1_s8_die1.ogg"
    d "I know you, Catalina. You wouldn't ask me for help if it wasn't important."
    d "Don't worry about anything. I'll help you. Get some rest while you wait for me to arrive."
    c "O-okay..."
    d "And please for the love of all the gods, don't cry. It breaks my heart to see you like this."
    c "S-sorry."
    d "See you in four hours."

    $ cmood = 'sad'
    $ vmood = 'happy'
    scene bg waiting night
    show catalina at left
    show valencia at offscreenright
    with fade

    "He takes his hand away from the mirror."
    "The familiar sight of Diedriech's face disappears and one again I'm alone in the waiting room."
    "He agreed to help me, without even knowing why I called."
    "I couldn't help but feel shocked."
    show valencia at flipCenter with dissolve
    v "Told you!"
    "I hear Valencia's voice and turn around to see her standing in the door to the doctor's room."
    c "Yeah..."
    "I answer softly and shrug, not being able to comprehend what happened."
    c "He said he'll be here in four hours."
    v "Great!"
    c "Get some rest, Val. Go home and sleep."
    $ vmood = 'worried'
    v "Only if you sleep too."
    c "I'll go upstairs as soon as you leave."
    "Val looks at me like she doesn't believe me. She sighs, but takes her things and leaves."
    v "Remember, we've got this Cat. I'll be back in four hours!"
    c "See you then!"

    scene bg vet night with fade
    $ cmood = 'sad'
    "As soon as Valencia leaves, I make my way back to the patient. I sit on the floor next to the phoenix, my back to the wall."
    "I can't leave a creature that's in pain completely alone. How can I sleep while it is suffering because I failed to help it?"
    "But I'm too tired from the day's work and exhausted from using my magic."
    "I can barely keep my eyes open and I begin to doze off."
    jump ch1_s9

label ch1_s9:
    scene bg wasteland dream with Fade(0.7, 0.5, 0.5)
    "I see a desolate landscape in front of me. The area is mountainous... or are they volcanoes?"
    $ cmood = 'surprised'
    $ emood = 'happy'
    show catalina at center with dissolve
    show edmundo at offscreenright
    "I'm standing in a pool of red hot lava. But I don't feel pain... shouldn't I die from something like this?"
    show catalina at left
    show edmundo at right
    with move
    e "It's okay. You're only dreaming."
    "There is a tall muscular man with dark skin in front of me, wearing elaborately embroidered clothes."
    "There is something regal about him, as if he owns the world wherever he goes."
    $ cmood = 'shy'
    "I can't help but feel fascinated by this mysterious stranger."
    c "Who... are you?"
    e "I'm the phoenix on your surgery table."
    $ cmood = 'surprised'
    "The phoenix... but he's a man... is he not?"
    c "Are you a shapeshifter?"
    $ emood = 'neutral'
    e "No... I can simply take whatever form I feel suits me."
    "But that would mean the creature has to have lived for thousands of years! Such power is not easily unlocked."
    $ emood = 'happy'
    e "Yes, I guess I'm an old man."
    $ emood = 'neutral'
    e "This body is a manifestation of my mental state though, so I suppose my spirit isn't that old yet, huh?"
    "I see... faced with such an old being talking to me, I feel..."

menu:
    "Insignificant":
        jump ch1_s9_2
    "Fascinated":
        jump ch1_s9_3

label ch1_s9_2:
    $ cmood = 'neutral'
    "I feel like a small insect in front of a large animal. I fear it could squash me at any moment."
    "I better act like I'm in front of a king."
    "I bow deeply out of respect for the creature that graced me with his dream."
    e "Nobody has bowed to me in ages, but..."
    $ emood = 'sad'
    e "It doesn't feel good, please stop."
    "I raise my head, then my body."
    $ cmood = 'worried'
    c "I only did it out of respect..."
    "The phoenix sighs, rubbing his temple."
    $ emood = 'neutral'
    e "I know. And I'd much rather you'd treat me as an equal."
    jump ch1_s9_4

label ch1_s9_3:
    "I feel fascinated with this mysterious being that must have seen so much in life."
    "Oh, the stories he could tell, the events he must have seen. Amazing."
    $ emood = 'sad'
    e "I may seem to you like a wonderful being, but you should know that living for thousands of years is not easy."
    $ emood = 'happy'
    e "Still, I'm happy you are not afraid of me."
    $ cmood = 'happy'
    c "No, somehow I feel at peace around you."
    e "Wonderful. Please treat me as an equal, as hard as it may be for you at first... but that's what I would prefer."
    $ cmood = 'neutral'
    "I nod. It will be hard, for sure, but out of respect for this being, I will try."
    jump ch1_s9_4

label ch1_s9_4:
    $ emood = 'happy'
    e "My name is Edmundo Valdez."
    $ cmood = 'neutral'
    c "Catalina Mendoza."
    e "Pleased to meet you, healer."
    $ cmood = 'sad'
    c "So far all I've done was fail to save you. Everything I tried... it didn't work."
    $ emood = 'neutral'
    e "You will get there, I believe in you. You see, it is very important that I'm healed. There is something I still need to do."
    $ emood = 'sad'
    e "Great evil is coming to this land and I-"
    scene white with Fade(0.25, 0.0, 0.25)
    v "Cat! Cat! Wake up!"
    d "Catalina..."
    jump ch1_s10

label ch1_s10:
    $ dmood = 'neutral'
    $ vmood = 'neutral'
    $ cmood = 'neutral'

    scene bg vet day
    show valencia at center
    show diedriech at flipLeft
    show catalina at flipRight
    with fade
    v "Diedriech is here. We need to get on with the healing."
    "I look at them, confused for a moment."
    "I felt like the phoenix was trying to tell me something important, but they woke me up from that dream...I remember it so vividly."
    "But... I have work to do. And Diedriech is here..."
    $ dmood = 'worried'
    d "Is that a phoenix I see on your surgery table?"
    "He nods to the patient as he stands there in all of his pretentious glory."
    "Oh, how the man annoys me by just being in the same room."
    $ cmood = 'angry'
    c "No, it's clearly a dragon."
    " I never did know why he gets on my nerves so much."
    $ vmood = 'worried'
    $ dmood = 'surprised'
    show valencia
    show diedriech
    "He looks at me exasperated. Valencia sighs."
    v "There they go again..."
    d "It's a phoenix?"
    "For the love of all the gods..."
    $ dmood = 'neutral'
    c "Yes, Mister Obvious. It's a phoenix."
    "If only he was half as smart as he was handsome."
    "Diedriech moves to the surgery table to examine our patient, mumbling under his breath."
    voice "voice/ch1_s10_die1.ogg"
    d "I never thought I would see a phoenix..."
    voice "voice/ch1_s10_die2.ogg"
    d "Look at his feather structure, what a wonderful specimen..."
    voice "voice/ch1_s10_die3.ogg"
    d "And the fact that it's on fire and not burning anything..."
    "Seeing him examine Edmundo with such curiosity, even though the phoenix is lying there dying, pisses me off even more."
    c "This is no time for looking at it as if you're in a zoo!"
    c "The patient is hurt! Can't you see the wounds?! And the dark energy swirling around?"
    $ dmood = 'neutral'
    "Diedriech sighs then looks at me seriously."
    d "You're right. Let's get to work. Tell me what you already know."
    $ cmood = 'neutral'
    "Now that's the part of my rival I always admired - his ability to shut off emotions in an instant and get into work-mode."
    "By comparison I'm definitely a lot more emotion-driven."
    c "Alright team, let's go."
    "I convey everything we've discovered and Diedriech listens and gives his own observations."
    $ dmood = 'neutral'
    voice "voice/ch1_s10_die4.ogg"
    d "It seems to me if we apply enough magical power at once..."
    voice "voice/ch1_s10_die5.ogg"
    d "We should be able to overwhelm the magic that's eating at its wounds."
    d "The alternative is of course unravelling the magic thread by thread."
    $ cmood = 'neutral'
    c "Tried that. It doesn't work. The pattern is too complicated and I can't find either the end nor the beginning."
    c "With time I could probably figure it out, but..."
    d "Time is what we don't have."
    $ vmood = 'worried'
    v "How much time do you think the patient has left?"
    "I think for a moment."
    $ cmood = 'worried'
    c "He seems much weaker than he was four hours ago..."
    "Was it because Edmundo used his powers to contact me through a dream?"
    $ dmood = 'surprised'
    $ vmood = 'surprised'
    d "He? You mean you can tell what gender it is?"
    v "Aren't phoenixes genderless?"
    $ cmood = 'neutral'
    c "This one seems to prefer being considered a male phoenix. His name is Edmundo Valdez. He contacted me in a dream."
    $ dmood = 'angry'
    d "You mean you dream-shared with the phoenix?!"
    "Why is Diedriech so angry all of a sudden?"
    c "I guess?"
    d "Did you or did you not?!"
    $ cmood = 'angry'
    $ vmood = 'worried'
    c "I did! But I don't get why you're shouting at me all of a sudden!"
    "Diedriech mumbles something under his breath. I recognize some of the words as Gerlan curses."
    d "...never gets anything..."
    c "I beg your pardon?!"
    v "Please calm down..."
    $ dmood = 'neutral'
    "He sighs, then rubs his temples. Soon after his calm self is back. How can he control his emotions so efficiently?"
    d "Nevermind. What did this Edmundo say to you in the dream?"
    $ cmood = 'neutral'
    c "You woke me up before he could say all he had to say, but he told me healing him was vital because... he has something important to do."
    d "So nothing useful."
    c "I would have healed him anyway, so I guess it wasn't anything that important."
    d "Alright, now that we've established we can only brute force the magic, let's focus on doing just that."
    d "Our combined power should be enough. I hope."
    "I share the sentiment."

    # MINIGAME
    scene black with dissolve
    " CH 1 SCENE 10 MINIGAME GOES HERE"

    jump ch1_s11

label ch1_s11:
    $ dmood = 'sad'
    $ vmood = 'sad'
    $ cmood = 'sad'

    scene bg vet sunset
    with fade

    "It takes us the whole day to heal the phoenix. Before I realize it, the sun is setting once again."
    "We used all of our magical power but the operation is a success. I feel like I could collapse at any moment."
    "I look around. Valencia is sitting on the floor, sleeping."
    "She couldn't keep up until the end so I told her to rest, but she didn't leave my side."
    show diedriech at flipLeft
    show catalina at flipCenter
    with dissolve
    "Diedriech looks exhausted."
    c "How many hours since last you slept?"
    d "Feels like the last time I slept was in the previous century."
    $ cmood = 'happy'
    show catalina happy
    c "Just like old times, right?"
    $ dmood = 'happy'
    d "Just like old times."
    "I remember all those sleepless nights trying to cram as much knowledge as we could into our brains for the exams."
    "Ah, university life. Sometimes I miss it."
    $ cmood = 'shy'
    c "Thank you for coming here, Diedriech."
    $ dmood = 'shy'
    d "...No, thank you for relying on me, Catalina. Thank you for thinking about me when you were in need."
    d "It really means a lot to me that you-"
    $ dmood = 'surprised'
    $ cmood = 'surprised'
    "Our awkward conversation is interrupted by a knock on the clinic's front door."
    c "Who in the world...?!"
    d "Don't go! The clinic is closed. We put up the sign. You don't need..."
    jump ch1_s12

label ch1_s12:
    $ cmood = 'neutral'
    $ dmood = 'neutral'
    scene bg waiting sunset with fade
    show catalina at flipCenter
    show diedriech at right
    with dissolve
    "But before Diedriech can stop me, I'm already at the entrance door."
    "The knock repeats. I unlock the door."
    $ mmood = 'surprised'
    $ gmood = 'happy'
    $ maxwithG = True
    show max at left with dissolve
    m "Ah...!"
    "I see Maximiano with Graciella in his arms. One of Maximiano's arms is raised as if he wants to knock again."
    "Graciella purrs in his arms happily, when she sees me."
    $ cmood = 'sad'
    "I sigh, feeling more exhausted than I did a moment ago."
    c "...I guess I told you to come here today..."
    $ mmood = 'shy'
    m "I'm sorry, Miss Catalina, I didn't realize you were busy... it's just that Graciella needs her treatment and..."
    $ cmood = 'happy'
    c "It's okay."
    $ dmood = 'angry'
    d "It's not okay."
    show diedriech at rightish with move
    $ cmood = 'surprised'
    show catalina
    "Diedriech steps in right behind me, putting a hand on my shoulder."
    "I stare at him, surprised to see that he is giving Maximiano a disapproving look."
    $ mmood = 'angry'
    $ gmood = 'neutral'
    show max
    "But when I look at Maximiano again... his expression mirrors Diedriech's. I thought he would be intimidated by my rival."
    "Many people were back in our school years. Yet, Maximiano doesn't seem shy at all."
    "How peculiar."
    $ cmood = 'neutral'
    d "Give me the pet, I will take care of it."
    $ gmood = 'angry'
    show max
    "Graciella hisses when she sees Diedriech's outstretched hands."
    m "No! Graciella doesn't like just anybody to touch her!"
    d "Did you just call me 'just anybody'?! For your information I am-"
    $ cmood = 'sad'
    "Okay, it's time to stop this before the whole situation blows up in my face. I'm too tired to deal with it."

menu:
    "Take care of Graciella's treatment":
        $ ch1s12_catCare = True
        jump ch1_s12_2
    "Trust that Diedriech knows what he is doing":
        $ ch1s12_catCare = False
        jump ch1_s12_3

label ch1_s12_2:
    $ cmood = 'neutral'
    show catalina at flipLeftish with move
    $ maxwithG = False
    "Before Diedriech does anything rash, I take Graciella off of Maximiano's arms."
    $ mmood = 'neutral'
    show catalina at flipCenter with move
    "She purrs happily, trying to get me to pet her. I stroke her behind her ear."
    m "See? She prefers Miss Catalina to treat her."
    d "Catalina, you really shouldn't-"
    $ cmood = 'sad'
    c "It's okay, I'll take care of it quickly."

    $ vmood = 'neutral'
    scene bg vet sunset
    show valencia at right
    with fade
    show diedriech at offscreenleft
    show max at offscreenleft
    show catalina at center with dissolve

    "I enter the doctor's room to see Valencia awake. She stands in the middle of the room, yawning."
    c "Valencia, could I ask you to do one more thing for me, before we retire for the night? Please hold Graciella for me."
    $ vmood = 'sad'
    v "Sure, sure."

    $ dmood = 'angry'
    $ mmood = 'angry'

    show catalina at rightish
    show max at flipLeftish
    show diedriech at flipLeft
    with move
    "Diedriech and Maximiano enter the room after me, staring daggers at each other."
    "My rival really shouldn't treat my patient's owners like that. I need to speak to him about it. Later... when I'm less tired."
    jump ch1_s12_4

label ch1_s12_3:
    "Diedriech knows what he's doing - he's a mythical animal healer too."
    show catalina at flipRight
    show diedriech at center
    with move
    $ maxwithG = False
    "I let him take Graciella, who puffs and tries to scratch him with her claws on the way to the doctor's room."
    m "Hey! Will you really let this stranger manhandle my precious Graciella?!"
    $ cmood = 'angry'
    c "\"This stranger\" is a healer like me. He knows what he's doing."
    $ dmood = 'happy'
    show diedriech at flipCenter
    "Diedriech looks at me with a happy smile. Maximiano looks as angry as his pet. It would be funny if I wasn't so tired."

    scene bg vet sunset
    show valencia at right
    with fade

    $ cmood = 'neutral'
    $ vmood = 'neutral'
    show catalina at leftish
    show diedriech at flipRightish
    show max at flipLeft
    with dissolve

    "We enter the doctor's room to see Valencia awake and standing in the middle, yawning."
    d "Valencia, could I ask you to do something for me - can you hold this ball of fur?"
    $ dmood = 'neutral'
    d "What kind of treatment does this little monster need?"
    m "What did you call my Princess?!"
    $ dmood = 'happy'
    $ cmood = 'happy'
    show diedriech happy talk
    "Diedriech laughs at Maximiano admitting he treats his pet like royalty. I can't help the smile that appears on my face. So cute."
    $ vmood = 'happy'
    $ cmood = 'neutral'
    show diedriech
    v "Graciella needs this injection."
    "Valencia passes the syringe along to Diedriech and he gives the injection."
    $ vmood = 'neutral'
    "Graciella makes unhappy sounds throughout the process, but at least that distracts her from the jab."
    $ gmood = 'sad'
    show diedriech at leftish
    show catalina at flipRightish
    with move
    pause 0.5
    $ maxwithG = True
    "Before long, she's released from the doctor's \"clutches\" and jumps into Maximiano's arms."
    m "Thank you... I guess."
    d "Oh, you're very welcome."
    $ dmood = 'angry'
    "The two of them continue to stare daggers at each other. What in the world is going on between them?"
    jump ch1_s12_4

label ch1_s12_4:
    $ mmood = 'surprised'
    m "Whoa!"
    $ dmood = 'neutral'
    $ cmood = 'neutral'
    $ vmood = 'neutral'
    show valencia
    "I realize that the phoenix is still lying on the surgery table, and the room is a mess from the operation."
    m "That's a... phoenix!"
    "I'm surprised he recognizes what the bird is."

menu:
    "Comment on Maximiano's knowledge of mythical animals":
        $ cmood = 'surprised'
        show catalina at flipRightish with dissolve
        c "I'm surprised you know that it's a phoenix..."
        m "Ah! I..."
        $ mmood = 'shy'
        m "I saw it in a painting one time..."
        "That's even more suspicious. Where would he find a painting with such a rare mythical creature?"
        jump ch1_s12_5
    "You're too tired to care about it.":
        "I'm too tired to hold a conversation. I'll ignore his comment for now."
        jump ch1_s12_5

label ch1_s12_5:
    "Diedriech looks at Maximiano suspiciously, but I shake my head and he drops the subject."

    if ch1s12_catCare:
        $ mmood = 'neutral'
        $ cmood = 'neutral'
        $ vmood = 'neutral'
        "Valencia holds Graciella for me, and I give the injection before she realizes what's happening to her."
        "She squeals in surprise, then jumps back into Maximiano's arms."
        $ mmood = 'happy'
        $ gmood = 'surprised'
        $ maxwithG = True
        m "Thank you, Miss Catalina!"

    $ mmood = 'happy'
    $ gmood = 'neutral'
    m "I'll come by again tomorrow!"
    $ cmood = 'sad'
    c "Yes, but around four pm please. We will be resting, and the clinic will be closed again."
    c "As you can see, we've been dealing with an emergency patient."
    $ mmood = 'neutral'
    m "Okay! 'Til tomorrow then!"

    hide max with dissolve
    show diedriech at flipLeft
    show catalina at flipCenter
    show valencia at right
    with move
    "We say our goodbyes and Maximiano leaves."
    $ dmood = 'neutral'
    $ vmood = 'neutral'
    d "Who in the world was that entitled brat?"
    $ cmood = 'sad'
    c "Maximiano Rozario. He's been a client of mine as long as I have had the clinic open."
    d "Hmm..."
    $ cmood = 'neutral'
    "Diedriech looks like he wants to say something, but when I give him the 'shut-up look', he closes his mouth."
    "I have no energy to deal with this right now."
    c "Alright team, let's go to sleep and meet again for a check-in tomorrow at eight am."
    c "Both of you can have one of my three guestrooms."
    "I live in an apartment above the clinic. It's a bit big for just me."
    "Honestly I would be fine with one bedroom, a bathroom, dining room and kitchen."
    "I keep the rest of the rooms as guest rooms, in case Valencia or one of the patient's owner's need to stay over."
    $ vmood = 'sad'
    v "Thank you, I think I'm too tired to walk home right now."
    $ dmood = 'sad'
    d "Me too, I feel like I could collapse any moment."

    scene bg waiting night with fade
    "We close the clinic and go upstairs. Diedriech and Valencia each take one of the free rooms and I go to mine."
    "All I can do is take off my clothes. I don't even have it in me to freshen up."
    "As soon as I collapse on the bed, I fall asleep."
    jump ch1_s13
