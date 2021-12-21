label ch1_s13:
    scene bg white with fade
    "I thought my night would be dreamless, after a long tiring day of work."
    "But images still come to me, and again I'm aware that I'm dreaming."
    "I've had lucid dreams since I could remember."
    "I didn't train myself to have them, nor did I try to influence them. I'm simply myself in those dreams, I'm present."
    "The difference is, I know the things that are happening aren't real."
    scene bg road sunset dream with fade
    "I'm walking through the forest again, following the road I was on the other day."
    "It seems to be dusk, the sun setting through the foliage."
    "???" "Catalina!"
    "I hear someone calling me, but I don't recognize the voice."
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
    m "Miss Catalina!"
    "I see Maximiano in front of me. He's alone and looks happy to see me."
    # CHANGE JUST THE BG
    scene bg road day dream with Fade(0.5, 0, 0.5)
    c "Whoa!"
    "The scenery changes, surprising me. We are in the same forest but in broad daylight."
    m "Is everything okay?!"
    "Maximiano runs closer to me and touches my hand. His touch is warm, and it doesn't feel unpleasant."
    "Wait, this is a dream. Do I want to touch Maximiano more in real life? But... why?"
    m "Miss Catalina..."
    "I realize my lack of response is making Maximiano worry. I squeeze his hand and smile brightly."
    c "Everything's okay. I'm happy to see you!"
    "Where's Graciella though? I always see Maximiano with his pet. It's weird to be here with him all alone."
    "But it's also nice in a sense. He has no reason to be here today - Graciella is fine."
    "He's not here to have me heal her. He's not worried about his pet either."
    "He's here for me. And I... like that."
    "It makes me want to hug him!"
    m "Ahhh!"
    "I embrace Maximiano tightly and he blushes furiously. It feels so nice to hug someone... him."
    "After a moment of hesitation he hugs me back."
    m "Miss Catalina..."
    "There's longing in his voice. I look up in his eyes and he leans down to me and..."
    "Wait! What exactly am I dreaming about?!"
    "I'm so shocked I wake up."
    jump ch1_s14

label ch1_s13_diedriech:
    d "Catalina..."
    "I see Diedriech in front of me. Why is he blushing so much though?"
    c "Do you have a fever or something, Diedriech?"
    d "I... no, I'm not ill..."
    d "I just thought you looked beautiful, illuminated by the setting sun like that..."
    "Is my subconscious playing tricks with me? Do I actually want Diedriech to say such corny lines in real life?"
    c "You must really be sick. Something's wrong with your head."
    "He stares at me surprised, then starts laughing as if I said the funniest thing in the world."
    c "Diedriech, what's wrong with you...?!"
    d "Nothing. I'm simply happy you are you, Catalina."
    c "Huh?!"
    d "You're the most wonderful person I know. Just being around you makes me happy."
    "What?! But we bicker all the time. Wait, this is a dream. Do- do I want Diedriech to talk to me like this?."
    c "..."
    "Suddenly I want to cry. Diedriech would never want to say such things to me in real life."
    "And that makes me so sad. I really wish things were different between us..."
    d "Catalina, why are you crying?"
    c "I... don't know..."
    "That's a lie. Now that I've seen Diedriech after a year, and he came running to me without hesitation, the pent-up feelings I have towards him will explode in my face again."
    "I hope he goes back home soon, then I won't have to face them."
    d "Catalina..."
    "Diedriech walks towards me, his hand outstretched as if he wants to touch my face."
    "But I'm not ready for this so I force myself to wake up."
    jump ch1_s14

label ch1_s13_edmundo:
    e "Catalina!"
    "I notice Edmundo in his human form in front of me. He seems genuinely happy to see me."
    "He looks around the forest with an expression of longing on his face."
    e "The forest is so beautiful, so lush, so... alive."
    "I wonder why he comments on that."
    c "The wasteland I saw the first time we shared a dream... is it a real place?"
    e "You won't find it if you look for it today. But yes, it's very real."
    "What does he mean? I look at him confused."
    "Edmundo takes a step closer to me, then another, until I have to raise my head to look up in his eyes. He's so much taller than me."
    "I blush. Again, it hits me how handsome he is, in his regal, timeless way."
    e "Back in the year 995, when King Leonardo ruled the country, women couldn't be doctors."
    e "When I see how excellent you are at your job, I see what a mistake that was."
    "I blush even harder. Compliments about how good I am at healing animals are something I very much like to hear."
    "But wait... I'm dreaming. Is Edmundo just saying what I want to hear? Do I want to hear it from him in particular?"
    "How vain must I be to want a centuries-old creature to compliment me."
    "Displeased, I force myself to wake up."
    jump ch1_s14

label ch1_s14:
    scene bg white with fade
    "Ten minutes later the clock strikes eight in the morning."

    show bg dining day with fade
    "I'm lost in thought as I make myself a bowl of oatmeal with fresh berries for breakfast."
    "I don't eat meat - it's hard not to be a vegan if your job is healing animals."
    "Fortunately there are plenty of other delicious things to eat  and cook for myself."
    "I make my way to the dining room - a place I use both for welcoming guests and for eating meals."
    "It's by far the grandest of my rooms, but very comfortable nonetheless."
    "I sit down to eat, but I'm not even halfway through when Diedriech enters the room."
    if ch1_dream == 'diedriech':
        "I blush, remembering the dream with him in it. Diedriech avoids my gaze, red in the face himself. Wait, what's wrong with him?"
        "I open my mouth to ask him again if he has a fever, but think better of it. If he's sick he'll tell me himself."
    d "Do you have more of that to eat?"
    "Diedriech points at my oatmeal and I nod."
    "I made enough for the three of us, knowing we're all vegan and like our oatmeal with berries on."
    "My guest goes to the kitchen and returns with his own bowl. Soon Valencia joins us too."
    "We eat in silence. We're still fatigued after using up so much magic."
    c "We should take it easy today. I don't feel well enough to start a normal day at the clinic yet."
    "After we've finished our food, I break the silence."
    d "Is everything okay? I can fill in for you, if you need to open..."
    c "No, you're tired yourself."
    v "I agree with Cat. Let's just go down to check on the phoenix and not open the clinic today."
    v "We're good for money, so no need to overwork ourselves."
    v "If there will be any special care patients, we can let them in."
    d "Just not that purrbear owner from yesterday..."
    c "Maximiano will probably come..."
    "Diedriech glares at his empty bowl. Why does he dislike Maximiano so much?"
    "It feels like there's more to it than simply being annoyed at having to heal Graciella despite being tired."
    show bg vet day with dissolve
    "With the dishes cleaned up, we go down to the clinic."
    "Edmundo is sleeping peacefully on the surgery table. We change his bandages to see that his wounds are already healed nicely."
    d "Great job."
    c "It's all due to the fact that we worked on the healing together."
    v "True."
    jump ch1_s15

label ch1_s15:
    "We spend the day in the clinic talking and reorganizing things. The day goes by peacefully with no clients needing immediate healing."
    scene bg vet sunset with fade
    "It's around four pm when we hear a knock on the door."
    "Diedriech sighs annoyed. Before he can move in to open the door, I quickly make my way to it."
    show bg waiting sunset with dissolve
    "I unlock the door and open it to see Maximiano with Graciella on the other side."
    if ch1_dream == 'max':
        "He blushes when he sees me, and I can't help but do the same as I remember the dream."
    c "Come in!"
    scene bg vet sunset with fade
    "I lead Maximiano to the doctor's room."
    "When he sees Diedriech, leaning against the surgery table, his disposition gets several degrees colder."
    "The two men glare daggers at each other."
    "I sigh. Why do they have to be so difficult?"
    "Valencia takes Graciella away from our client and holds her as I give the injection."
    c "There! She should feel perfectly healthy by tomorrow!"
    m "Thank you, Miss Catalina."
    "Maximiano pays for the injection and Valencia takes the money from him. He turns to leave, but before he can..."
    "There is a sound of flapping wings and a loud whoosh of magic, and when we all turn around to the surgery table, we see Edmundo in his human form."
    "He looks all healed up and smiles at us brightly."
    jump ch1_s16

label ch1_s16:
    e "Wonderful to have you all here. Healer..."
    "He nods to me."
    e "Healer's right hand..."
    "He points at Valencia. She curtsies."
    e "Healer's rival..."
    "Now he gestures at Diedriech, who smirks at being called that."
    e "And you, Prince Maximiano..."
    "We all look at Maximiano, shocked."
    c "Wait, Prince?!"
    m "Haha, well..."
    e "Ah, so you didn't know?"
    e "This is Maximiano Rosario, the Prince of the Kingdom of Girasol and the heir to the throne."
    "I continue to stare at Maximiano with my mouth gaping."
    c "Why did you not tell me?!"
    m "I prefered the anonymity of just being Maximiano to you."
    "A part of me feels betrayed, but I understand his reasoning."
    c "Well... okay..."
    m "Miss Catalina! Don't be sad!"
    "I shake my head. I don't want to continue talking about this. Not until I've processed this new piece of information."
    "Maximiano looks dejected, but he must have realized that I don't want to hear anymore because he doesn't pressure me."
    "Edmundo claps his hands."
    e "Well, since we are all gathered here, I need to ask the four of you for help."
    e "You see, the Kingdom of Girasol, no... the whole world is in grave danger."
    "We focus on Edmundo, seeing how serious he is."
    c "Is that why you were so hurt?"
    e "You could say that. I'm a time traveler. The world you've seen in the dream we shared - it's our world in the future, destroyed."
    c "What?! But that place..."
    e "Yes, it's broken beyond repair. I'm trying to prevent this future and you've been prophesied by the Oracle. Only you four can help me."
    e "So I ask you, Catalina, Valencia, Diedriech and Maximiano... will you help me save the world?"
    scene black with fade
    "Healer & Phoenix: End of Demo"
    "Thank you for playing! Look forward to the full version of the game!"


return
