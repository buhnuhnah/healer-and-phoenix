label ch1_s13:
    scene black with fade
    "I thought my night would be dreamless, after a long tiring day of work."
    "But images still come to me, and again I'm aware that I'm dreaming."
    "I've had lucid dreams since I could remember."
    "I didn't train myself to have them, nor did I try to influence them. I'm simply myself in those dreams, I'm present."
    "The difference is, I know the things that are happening aren't real."
    $ cmood = 'neutral'
    scene bg road sunset dream
    show catalina at center
    with fade
    "I'm walking through the forest again, following the road I was on the other day."
    "It seems to be dusk, the sun setting through the foliage."
    "???" "Catalina!"
    $ cmood = 'surprised'
    "I hear someone calling me, but I don't recognize the voice."
    $ cmood = 'neutral'
    show catalina at right with move
    show catalina at flipRight with dissolve
    "It echoes, as if it were multiple people but when I turn around, I see only one figure."

menu:
    "Maximiano?":
        $ ch1_dream = 'max'
        jump ch1_s13_max
    "Diedriech?":
        $ ch1_dream = 'diedriech'
        jump ch1_s13_diedriech
    "Edmundo?":
        $ ch1_dream = 'edmundo'
        jump ch1_s13_edmundo

label ch1_s13_max:
    $ maxwithG = False
    $ mmood = 'happy'
    show max at flipLeft with dissolve
    m "Miss Catalina!"
    "I see Maximiano in front of me. He's alone and looks happy to see me."
    show bg road day dream with dissolve
    $ cmood = 'surprised'
    c "Whoa!"
    "The scenery changes, surprising me. We are in the same forest but in broad daylight."
    $ mmood = 'surprised'
    m "Is everything okay?!"
    $ cmood = 'neutral'
    show max at flipCenter with move
    "Maximiano runs closer to me and touches my hand. His touch is warm, and it doesn't feel unpleasant."
    $ cmood = 'surprised'
    "Wait, this is a dream. Do I want to touch Maximiano more in real life? But... why?"
    $ mmood = 'worried'
    m "Miss Catalina..."
    $ cmood = 'happy'
    "I realize my lack of response is making Maximiano worry. I squeeze his hand and smile brightly."
    $ mmood = 'happy'
    c "Everything's okay. I'm happy to see you!"
    "Where's Graciella though? I always see Maximiano with his pet. It's weird to be here with him all alone."
    "But it's also nice in a sense. He has no reason to be here today - Graciella is fine."
    "He's not here to have me heal her. He's not worried about his pet either."
    "He's here for me. And I... like that."
    "It makes me want to hug him!"
    show max behind catalina
    show catalina at flipRightish with move
    $ mmood = 'shy'
    m "Ahhh!"
    "I embrace Maximiano tightly and he blushes furiously. It feels so nice to hug someone... him."
    "After a moment of hesitation he hugs me back."
    m "Miss Catalina..."
    "There's longing in his voice. I look up in his eyes and he leans down to me and..."
    $ cmood = 'surprised'
    "Wait! What exactly am I dreaming about?!"
    "I'm so shocked I wake up."
    jump ch1_s14

label ch1_s13_diedriech:
    $ dmood = 'shy'
    show diedriech at flipLeft with dissolve
    d "Catalina..."
    $ cmood = 'surprised'
    "I see Diedriech in front of me. Why is he blushing so much though?"
    c "Do you have a fever or something, Diedriech?"
    $ cmood = 'neutral'
    d "I... no, I'm not ill..."
    $ cmood = 'surprised'
    d "I just thought you looked beautiful, illuminated by the setting sun like that..."
    "Is my subconscious playing tricks with me? Do I actually want Diedriech to say such corny lines in real life?"
    $ cmood = 'angry'
    c "You must really be sick. Something's wrong with your head."
    $ dmood = 'surprised'
    show diedriech
    pause 0.5
    $ dmood = 'happy'
    show diedriech
    "He stares at me surprised, then starts laughing as if I said the funniest thing in the world."
    $ cmood = 'surprised'
    c "Diedriech, what's wrong with you...?!"
    d "Nothing. I'm simply happy you are you, Catalina."
    c "Huh?!"
    d "You're the most wonderful person I know. Just being around you makes me happy."
    "What?! But we bicker all the time. Wait, this is a dream. Do- do I want Diedriech to talk to me like this?"
    $ cmood = 'sad'
    c "..."
    $ dmood = 'surprised'
    "Suddenly I want to cry. Diedriech would never want to say such things to me in real life."
    "And that makes me so sad. I really wish things were different between us..."
    $ dmood = 'sad'
    d "Catalina, why are you crying?"
    c "I... I don't know..."
    "That's a lie. I've seen Diedriech after a year, and he came running to me without hesitation."
    "Now the pent-up feelings I have towards him will explode in my face again."
    "I hope he goes back home soon, then I won't have to face them."
    d "Catalina..."
    show diedriech at flipCenter with move
    "Diedriech walks towards me, his hand outstretched as if he wants to touch my face."
    "But I'm not ready for this so I force myself to wake up."
    jump ch1_s14

label ch1_s13_edmundo:
    $ emood = 'happy'
    show edmundo at flipLeft with dissolve
    e "Catalina!"
    "I notice Edmundo in his human form in front of me. He seems genuinely happy to see me."
    "He looks around the forest with an expression of longing on his face."
    $ emood = 'sad'
    e "The forest is so beautiful, so lush, so... alive."
    $ cmood = 'worried'
    "I wonder why he comments on that."
    c "The wasteland I saw the first time we shared a dream... is it a real place?"
    e "You won't find it if you look for it today. But yes, it's very real."
    "What does he mean? I look at him confused."
    show edmundo at flipCenter with move
    $ emood = 'neutral'
    "Edmundo takes a step closer to me, then another, until I have to raise my head to look up in his eyes. He's so much taller than me."
    $ cmood = 'shy'
    show catalina
    "I blush. Again, it hits me how handsome he is, in his regal, timeless way."
    e "Back in the year 995, when King Leonardo ruled the country, women couldn't be doctors."
    $ emood = 'happy'
    e "When I see how excellent you are at your job, I see what a mistake that was."
    "I blush even harder. Compliments about how good I am at healing animals are something I very much like to hear."
    $ cmood = 'neutral'
    show catalina
    "But wait... I'm dreaming. Is Edmundo just saying what I want to hear? Do I want to hear it from him in particular?"
    "How vain must I be to want a centuries-old creature to compliment me."
    "Displeased, I force myself to wake up."
    jump ch1_s14

label ch1_s14:
    scene white with dissolve
    "Ten minutes later the clock strikes eight in the morning."

    $ dmood = 'neutral'
    $ cmood = 'neutral'
    show bg dining day
    show catalina at flipRight
    show diedriech at offscreenleft
    with fade

    "I'm lost in thought as I make myself a bowl of oatmeal with fresh berries for breakfast."
    "I don't eat meat - it's hard not to be a vegan if your job is healing animals."
    "Fortunately there are plenty of other delicious things to eat  and cook for myself."
    "I make my way to the dining room - a place I use both for welcoming guests and for eating meals."
    "It's by far the grandest of my rooms, but very comfortable nonetheless."
    show diedriech at flipLeft with move
    "I sit down to eat, but I'm not even halfway through when Diedriech enters the room."
    if ch1_dream == 'diedriech':
        $ cmood = 'shy'
        $ dmood ='shy'
        show diedriech
        "I blush, remembering the dream with him in it. Diedriech avoids my gaze, red in the face himself. Wait, what's wrong with him?"
        "I open my mouth to ask him again if he has a fever, but think better of it. If he's sick he'll tell me himself."
    $ dmood = 'neutral'
    d "Do you have more of that to eat?"
    $ cmood = 'neutral'
    "Diedriech points at my oatmeal and I nod."
    "I made enough for the three of us, knowing we're all vegan and like our oatmeal with berries on."

    $ vmood = 'neutral'
    show valencia at offscreenleft
    show diedriech at flipCenter
    show valencia at flipLeft
    with move

    "My guest goes to the kitchen and returns with his own bowl. Soon Valencia joins us too."
    "We eat in silence. We're still fatigued after using up so much magic."
    "After we've finished our food, I break the silence."
    c "We should take it easy today. I don't feel well enough to start a normal day at the clinic yet."
    $ dmood = 'worried'
    d "Is everything okay? I can fill in for you, if you need to open..."
    $ cmood = 'worried'
    c "No, you're tired yourself."
    v "I agree with Cat. Let's just go down to check on the phoenix and not open the clinic today."
    v "We're good for money, so no need to overwork ourselves."
    v "If there will be any special care patients, we can let them in."
    $ dmood = 'angry'
    d "Just not that purrbear owner from yesterday..."
    c "Maximiano will probably come..."
    $ vmood = 'worried'
    "Diedriech glares at his empty bowl. Why does he dislike Maximiano so much?"
    "It feels like there's more to it than simply being annoyed at having to heal Graciella despite being tired."

    $ dmood = 'neutral'
    $ vmood = 'neutral'
    $ cmood = 'neutral'
    show bg vet day
    show diedriech at flipLeft
    show catalina at center
    show valencia at right
    with fade

    "With the dishes cleaned up, we go down to the clinic."
    "Edmundo is sleeping peacefully on the surgery table. We change his bandages to see that his wounds are already healed nicely."
    $ dmood = 'happy'
    d "Great job."
    $ cmood = 'happy'
    c "It's all due to the fact that we worked on the healing together."
    $ vmood = 'happy'
    v "True."
    jump ch1_s15

label ch1_s15:
    "We spend the day in the clinic talking and reorganizing things. The day goes by peacefully with no clients needing immediate healing."
    show bg vet sunset with dissolve
    "It's around four pm when we hear a knock on the door."
    $ dmood = 'angry'
    $ cmood = 'neutral'
    $ vmood = 'neutral'
    show diedriech
    show catalina at flipCenter with dissolve
    "Diedriech sighs annoyed. Before he can move in to open the door, I quickly make my way to it."
    scene bg waiting sunset
    show catalina at flipCenter
    show max at offscreenleft
    with fade
    $ maxwithG = 'neutral'
    $ mmood = 'neutral'
    $ gmood = 'neutral'
    show max at flipLeft with move
    "I unlock the door and open it to see Maximiano with Graciella on the other side."
    if ch1_dream == 'max':
        $ mmood = 'shy'
        $ cmood = 'shy'
        show max
        show catalina
        "He blushes when he sees me, and I can't help but do the same as I remember the dream."
    $ cmood = 'happy'
    $ mmood = 'happy'
    show max
    show catalina
    c "Come in!"

    scene bg vet sunset
    show diedriech at right
    show valencia at rightish
    with fade
    show catalina at offscreenleft
    show max at offscreenleft
    with None
    $ cmood = 'neutral'
    $ mmood = 'neutral'
    show catalina at leftish
    show max at flipLeft
    with move

    "I lead Maximiano to the doctor's room."
    $ mmood = 'angry'
    $ gmood = 'angry'
    $ dmood = 'angry'
    show max
    "When he sees Diedriech, leaning against the surgery table, his disposition gets several degrees colder."
    "The two men glare daggers at each other."
    $ cmood = 'worried'
    "I sigh. Why do they have to be so difficult?"
    $ maxwithG = False
    "Valencia takes Graciella away from our client and holds her as I give the injection."
    $ cmood = 'happy'
    show catalina at flipLeftish
    c "There! She should feel perfectly healthy by tomorrow!"
    $ mmood = 'happy'
    $ gmood = 'happy'
    $ maxwithG = True
    m "Thank you, Miss Catalina."
    "Maximiano pays for the injection and Valencia takes the money from him. He turns to leave, but before he can..."
    scene white with dissolve
    $ dmood, mmood, gmood, cmood, vmood = 'surprised', 'surprised', 'surprised', 'surprised', 'surprised'
    $ emood = 'neutral'

    scene bg vet sunset
    show edmundo at center
    with dissolve
    "There is a sound of flapping wings and a loud whoosh of magic, and when we all turn around to the surgery table, we see Edmundo in his human form."
    $ emood = 'happy'
    show edmundo
    "He looks all healed up and smiles at us brightly."
    jump ch1_s16

label ch1_s16:
    e "Wonderful to have you all here. Healer..."
    $ cmood = 'happy'
    show edmundo at right with move
    show catalina at left with dissolve
    show catalina
    "He nods to me."
    e "Healer's right hand..."
    $ vmood = 'happy'
    show valencia at flipLeftish with dissolve
    "He points at Valencia. She curtsies."
    e "Healer's rival..."
    $ dmood = 'happy'
    hide valencia with dissolve
    show diedriech at flipLeftish with dissolve
    "Now he gestures at Diedriech, who smirks at being called that."
    e "And you, Prince Maximiano..."
    $ gmood = 'neutral'
    $ mmood = 'shy'
    $ cmood, vmood, dmood = 'surprised', 'surprised', 'surprised'
    hide diedriech with dissolve
    show max at flipLeftish
    show catalina
    with dissolve
    "We all look at Maximiano, shocked."
    c "Wait, Prince?!"
    m "Haha, well..."
    $ emood = 'surprised'
    e "Ah, so you didn't know?"
    $ emood = 'neutral'
    e "This is Maximiano Rosario, the Prince of the Kingdom of Girasol and the heir to the throne."
    "I continue to stare at Maximiano with my mouth gaping."
    c "Why did you not tell me?!"
    m "I prefered the anonymity of just being Maximiano to you."
    $ cmood = 'sad'
    $ dmood, vmood = 'neutral', 'neutral'
    "A part of me feels betrayed, but I understand his reasoning."
    c "Well... okay..."
    $ mmood = 'surprised'
    m "Miss Catalina! Don't be sad!"
    "I shake my head. I don't want to continue talking about this. Not until I've processed this new piece of information."
    $ mmood = 'sad'
    show max
    "Maximiano looks dejected, but he must have realized that I don't want to hear anymore because he doesn't pressure me."
    hide max with dissolve
    "Edmundo claps his hands."
    show edmundo at rightish with move
    e "Well, since we are all gathered here, I need to ask the four of you for help."
    e "You see, the Kingdom of Girasol, no... the whole world is in grave danger."
    $ cmood = 'neutral'
    show catalina
    "We focus on Edmundo, seeing how serious he is."
    $ cmood = 'worried'
    c "Is that why you were so hurt?"
    e "You could say that. I'm a time traveler. The world you've seen in the dream we shared - it's our world in the future, destroyed."
    $ cmood = 'surprised'
    c "What?! But that place..."
    $ emood = 'sad'
    e "Yes, it's broken beyond repair. I'm trying to prevent this future and you've been prophesied by the Oracle. Only you four can help me."
    $ emood = 'neutral'
    $ mmood,  dmood, vmood = 'surprised', 'surprised', 'surprised'
    e "So I ask you, Catalina, Valencia, Diedriech and Maximiano... will you help me save the world?"
    scene black with fade
    "Healer & Phoenix: End of Demo"
    "Thank you for playing! Look forward to the full version of the game!"


return
