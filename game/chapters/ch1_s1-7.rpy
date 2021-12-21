label start:
    #scene wasteland with fade

    "The Oracle" "Once again the world is destroyed, ravaged by evil magic."
    "The Oracle" "How many times do you have to try, Phoenix, before you understand you can't save the world alone?"
    "Phoenix" "..."
    "Phoenix" "The gods made me the protector of this world."
    "The Oracle" "And you thought you'd have to bear this burden alone."
    "Phoenix" "Yes, but it's no use. I'm too weak..."
    "The Oracle" "You are not weak. Still, now you've seen it's an impossible task for one creature, no matter how powerful it is."
    "Phoenix" "I can't heal the infected animals. I need the help of a healer!"
    "Phoenix" "Oracle-"
    "The Oracle" "Once again, I'll send you back in time to a location in which a Healer will find you."
    "The Oracle" "But I too, am tired."
    "The Oracle" "I grow weary as my life force dwindles, thus I cannot bear the burden of using this kind of powerful magic anymore."
    "The Oracle" "This will be the last time I can help you this way, I am afraid I will have to use your own life force to do so."
    "The Oracle" "You will arrive hurt and dying."
    "Phoenix" "I understand, thank you for your help."
    "The Oracle" "Pray to the gods she finds you in time."
    # show oracle at [position], flash
    # play music sound

    jump ch1_s2

label ch1_s2:
    # show max cg
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
    scene bg vet day with fade
    # sprites of Catalina Neutral, Valencia Worried, and Maximiano Sad with hurt Graciella"
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

    # INSERT MINIGAME
    "INSERT MINIGAME HERE"

    v "I'll hold Graciella for you."
    "Valencia grabs Graciella so that she can't see me coming to her from behind with the syringe."
    "Before the pet notices anything, I inject it."
    c "There, all done!"
    "Graciella makes purring sounds, trying to get Valencia to pet her."
    v "Good girl!"
    "Valencia hugs the purrbear to her. Graciella sounds like one happy purrbear. It makes me so pleased to see an animal be so joyful."
    m "You really are a wonderful healer, Miss Catalina..."
    "I look at Maximiano and smile brightly."
    m "Oh!"
    "He yelps, surprised."
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
    "I approach Valencia, who has Graciella in her arms, and hug them both."
    "Graciella seems to be happy with being between the two of us."
    m "...how sweet."
    c "Come join us!"
    "I smile at Maximiano brightly, urging him to join us in the hug, but he shakes his head."
    m "Thank you, but I'm good."
    c "Daw..."
    "I make a sound of disappointment."
    "Eventually, we stop hugging. Valencia approaches Maximiano with his pet in her arms and hands Graciella over."
    jump ch1_s2_5

label ch1_s2_3:
    "I approach Maximiano and before he can stop me from hugging him, I embrace him tightly."
    m "Whoa!"
    "He's beet red, all the way to his ears."
    c "Hugging is healthy!"
    "Though I'm not doing it because I'm a healer. I simply wanted to hug Maximiano. He's just so cute!"
    m "Ahhhh....!"
    "Like now, when he's having a meltdown, waving his arms in the air, not knowing where to put them."
    "I let him go before his brain explodes."
    m "Miss Catalina..."
    "He has such pretty green eyes."
    v "E-hem."
    "Valencia approaches us with Graciella in her arms. She hands the pet over to Maximiano."
    jump ch1_s2_5

label ch1_s2_4:
    "Maybe I shouldn't do it. It might feel too invasive to others if I suddenly embrace them."
    "As much as I like hugging, I need consent to do it."
    "Eventually, Valencia approaches Maximiano with Graciella in her arms. She hands the pet over to her owner."
    jump ch1_s2_5

label ch1_s2_5:
    v "The payment?"
    m "Ah, right."
    "Maximiano pays for our service, then exits the room."
    if hugMax:
        v "He's pretty cute, isn't he?"
        c "That he is."
        "We giggle happily like two schoolgirls."
        "What? There's nothing wrong with appreciating how handsome our clients are. After all, we're helping their pets, not them."
    "It's time for us to take on the next patient."
    c "I really love this job."
    "I say randomly, feeling very happy about healing another pet.."
    "I've been a mythical animal healer for a year now."
    "I graduated from a top university, and ever since then I've been running my own clinic with the help of my best friend Valencia."
    v "I love this job too."
    jump ch1_s3

label ch1_s3:
    "INSERT CH 1 SCENE 4"
    jump ch1_s4

label ch1_s4:
    scene bg vet day with fade
    "Later that day, after we've already closed the clinic for the day, and started our clean-up routine, Valencia smiles at me brightly."
    v "Another day of work successfully completed!"

    # GRAB MINIGAME RESULTS LATER
    # 1 for great, 0 for bad
    $ minigameResult = 1

    if minigameResult > 0:
        c "Today was a great day!"
        "I can't help the bright smile that appears on my face. I love my job and it brings me a lot of satisfaction."
        v "Yes, and no major surgeries-"
        "Our happiness is interrupted by loud banging on the entrance door."
        "It's past opening hours, but that's not the first time we find ourselves in this situation."
        "I can't say I'm surprised. Everything has gone too smoothly today."
    else:
        c "Today could have been better, but at least we made no major mistakes."
        "I smile at her softly. It certainly hasn't been the best day in the history of the clinic, but still, I love my job."
        v "Yes, and no major surgeries-"
        "Our conversation is interrupted by loud banging on the entrance door. It's past opening hours, but that's not the first time we find ourselves in this situation."
        "I can't say I'm surprised."

    c "You might have said that too soon."
    v "Oh no..."

    scene bg waiting day with fade

    "I make my way to the entrance door, Valencia following me closely behind."
    "???" "Healer! We need your help!"
    "There is a panicked man wearing a hard hat and plaid shirt on the outside of the entrance."
    "A lumberjack? But I see no sick animal with him. Oh no, is this an emergency call?"
    c "I'm here. How can I help?"
    "Lumberjack" "There's a burning bird in the forest just outside of town!"
    "Lumberjack" "We were working -  cutting trees and we found it there, lying there in a clearing!"
    "Lumberjack" "I swear we've done nothing! But it's on fire!"
    "That can't be what I think it is. I exchange a worried glance with Valencia."
    c "Hold on, please don't panic. I'm not blaming you for anything."
    c "Tell me the state of the patient. Does it have any wounds?"
    "Lumberjack" "I don't know..."
    c "Has no one looked closely at the creature?"
    "Lumberjack" "No one dared to approach it! It's an inferno!"
    "The man looks shocked at my suggestion. I sigh, too tired to hide my annoyance."
    "Well, sometimes indifference is better than messing something up while trying to help."
    c "Val, get the flying stretcher, my toolbox and four fire resistance potions."
    v "On it!"
    "Valencia leaves to prepare what we need to help our new patient."
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
    c "Thank you for your faith in me."
    "Lumberjack" "Of course, you're known as the best animal healer in town!"
    "I nod, happy that my fame is spreading. Though with great fame comes great responsibility, as I think I'm about to discover..."
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
    "After a while, Valencia comes back, the stretcher flying behind her."
    v "I have everything you've requested."
    c "Then let's go! No time to waste!"
    jump ch1_s5

label ch1_s5:
    scene bg road day with fade
    "We follow the man on the road leading out of town and soon we enter the forest. The trees rustle and move in the wind gently."
    "Nothing seems to indicate something bad has happened here."
    v "So... what do you think it is?"
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
    v "But no one has seen a phoenix in decades!"
    c "That's one of the things that worries me. Will we be able to heal it?"
    v "I've only learned phoenix anatomy in books..."
    c "Same here. I have no practical experience with such advanced beings."
    "I was present once when a dragon was cured, but the only thing used back then was a lot of magic."
    c "And I really mean it when I say a lot of magic."
    c "They had to use a huge magical crystal and ten people had to channel healing magic through it."
    c "Only then did the spell to have enough power to not burn out mid-way."
    v "Oh no..."
    c "I hope I can do something for the phoenix, anything before it's too late."
    v "Let's not lose hope just yet. You're an excellent healer!"
    c "Thank you, but sometimes skill itself isn't enough."
    c "There's one more thing worrying me..."
    v "Yes?"
    c "Why is a phoenix on the brink of death in the first place? What was strong enough to cause such an injury?"
    "We stare at each other in grim silence. There's few animals I consider strong enough to cause harm to a phoenix..."
    "And the presence of any of them so close to human homes is worrying."
    v "I hope we'll be able to find out from the type of injuries it has."
    c "Indeed."
    "The lumberjack stops in front of us, and gestures to the left."
    "Lumberjack" "We need to get off this path here! Come on, ladies!"
    v "We're coming!"
    "We leave the road and enter the forest proper. After walking for a few minutes we hear the worried voices of multiple people."
    "A few steps more and we see a clearing with lumberjacks gathered around a campfire."
    "Lumberjack" "The healer is here!"
    "The people greet us with excitement."
    "After saying hello, we follow the man who took us here a bit further into the forest... until we reach another clearing."
    jump ch1_s6

label ch1_s6:
    # PHOENIX CG
    "Shock paralyses me when I see the phoenix lying in the middle of the foliage."
    "Power is radiating off the creature -  a magnificent, fearsomely beautiful being."
    "I force myself to approach, knowing that even when hurt it could so easily kill me."
    "I remind myself it's my job to help no matter what."
    "When I see the extent of the phoenix' injuries, I wonder how it's still alive. It must be in a lot of pain."
    "Numerous cuts all around its body, feathers plucked out. It lies there unconscious."
    "There is also some sort of magic attached to its body. It's floating around the wounds, a dark shadow."
    "Curiosity overwhelmed me, I put my finger into the swirling mass."
    c "Ow!"
    "Rather than a burn, it feels like a bite. But when I examine my hand there is no sign of injury. Did it bite my magical aura directly?"
    "For a moment I worry it might damage me somehow, but soon it stops hurting altogether."
    c "Valencia, please bring the stretcher."
    v "On it!"
    "We brought the fire resistance potions with us, but if it's a phoenix there is no point in using them."
    "The creature won't burn the stretcher. Even in this severely wounded condition it seems to have control over its own flames."
    "Phoenixes only burn things with their fire when they want to."
    "The will of this one must be strong, since it's still protecting the world from itself."
    c "Hey! Could you help us pack the creature onto the stretcher?"
    c "It won't burn you, but watch out for the swirling black magic! It's painful."
    scene bg road day
    "The lumberjacks look scared, but the man who walked us here and another approach."
    "Lumberjack" "Understood. We'll help."
    "I direct the two men on how to grab the bird properly. In no time it's on our stretcher and we set it to floating again."
    "We say our goodbyes. The lumberjacks seem relieved that the problem is out of their hands now."
    "The stretcher floats behind it as we make our way back to the clinic."
    jump ch1_s7

label ch1_s7:
    scene bg vet day
    c "Let's lay the phoenix on the table."
    v "Yes!"
    "We carefully move the patient from the stretcher to the surgery table."

    # MINIGAME
    " INSERT SCENE 7 MINIGAME"

    scene bg vet sunset with fade
    "We try everything we can. Hours pass by. Whenever we manage to heal a wound, it opens again."
    c "It must be the dark magic that's attached to the phoenix' body."
    v "You're right. We need someone magically stronger than us to join us and help detach whatever that darkness is from the patient."
    "Someone magically stronger... but whom should I call? I'm stronger than all the other healers in town."
    v "How about Die-"
    c "No."
    "I answer quickly. I don't want to call on that person for any reason."
    c "He's in Gerla anyway. Do you think he would come to Selia just because I need something?"
    v "Yes, he will."
    "Valencia answers with a bright smile. I stare at her like she just grew a second head."
    c "Do you hear yourself? He lives in Gerla's capital now, that's a week's journey from here!"
    v "Not if he uses a portal!"
    c "But that's so expensive!"
    v "Diedriech isn't exactly poor, is he?"
    "Well no, he certainly isn't poor. Diedriech is about as rich as I am."
    "My parents gifted me this whole building when I graduated with flying colors."
    "Considering that, Diedriech definitely has the money for a portal."
    c "I still don't think that's a good idea."
    v "If he can't come, no biggie. But trust me, he will be happy that you want to rely on him for something."
    "I can't understand why he would be."
    "Diedriech and I have been rivals throughout all of our university years. We were like fire and water, always bickering."
    "Somehow the Garlan never left me alone, always coming to me to tease me about this and that."
    "When university ended, I moved back to my parents' hometown of Zalila."
    "Diedriech returned to Gerla to take over his parents' healing clinic for mythical creatures."
    "It's been a year since I last heard from him."
    "And now suddenly I'm supposed to contact him, because I'm in distress?"
    "I look at the phoenix, lying there on my table, hurt and dying."
    "The thing that's stopping me from calling Diedriech is... pride. And that's stupid. I have to put those uncomfortable feelings aside."
    c "I'll call him."
    v "Great! I'll stay here."
    "I nod at Valencia and step out of the room."
    jump ch1_s8
