def get_train_data():
    # ct = character_trait
    # hc = hair_color
    # eyc = eye_color
    # skin = skin_color
    # ...

    TRAIN_DATA = [
        ("I want a person who is very aggressive and happy sometimes",
         {"entities": [(28, 38, "ct"), (43, 48, "ct")]}),

        ("I want a person who is very happy and friendly sometimes",
         {"entities": [(28, 33, "ct"), (38, 46, "ct")]}),

        ("I want a person who is very aggressive, rude and happy sometimes",
         {"entities": [(28, 38, "ct"), (40, 44, "ct"), (49, 54, "ct")]}),

        ("I want a person who is happy all the time.",
         {"entities": [(23, 28, "ct")]}),

        ("I want a person who is friendly all the time.",
         {"entities": [(23, 31, "ct")]}),

        ("I want a person who is rude all the time.",
         {"entities": [(23, 27, "ct")]}),

        ("I want a person who is aggressive all the time.",
         {"entities": [(23, 33, "ct")]}),

        ("I want a person who is pushy all the time.",
         {"entities": [(23, 28, "ct")]}),

        ("I want a person who is lazy all the time.",
         {"entities": [(23, 27, "ct")]}),

        ("I want a person who is friendly, rude and lazy sometimes",
         {"entities": [(23, 31, "ct"), (33, 37, "ct"), (42, 46, "ct")]}),

        ("I want a person who is lazy and rude sometimes",
         {"entities": [(23, 27, "ct"), (32, 36, "ct")]}),

        ("I want a person who is enormous lazy and sometimes happy",
         {"entities": [(32, 36, "ct"), (51, 56, "ct")]}),

        ("I want a person who is not lazy, but happy",
         {"entities": [(23, 31, "ct"), (37, 42, "ct")]}),

        ("I want a person who is not happy, but aggressive",
         {"entities": [(23, 32, "ct"), (38, 48, "ct")]}),

        ("I want a person who is not aggressive and not happy",
         {"entities": [(23, 37, "ct"), (42, 51, "ct")]}),

        ("I want a person who is not rude, but happy",
         {"entities": [(23, 31, "ct"), (37, 42, "ct")]}),

        ("I want a person who is not rude and not aggressive, but happy",
         {"entities": [(23, 31, "ct"), (36, 50, "ct"), (56, 61, "ct")]}),

        ("I want a person who is friendly and that's always in a happy mood",
         {"entities": [(23, 31, "ct"), (55, 60, "ct")]}),

        ("I want somebody who is aggressive and sometimes happy!",
         {"entities": [(23, 33, "ct"), (48, 53, "ct")]}),

        ("A person who is always in a happy mood",
         {"entities": [(28, 33, "ct")]}),

        ("A person who is most of the time rude to me",
         {"entities": [(33, 37, "ct")]}),

        ("I want somebody who is very aggressive, but most of the time lazy",
         {"entities": [(28, 38, "ct"), (61, 65, "ct")]}),

        ("The person must be somebody who is very friendly to me and also happy",
         {"entities": [(40, 48, "ct"), (64, 69, "ct")]}),

        ("I want somebody who is not aggressive, not rude, but all the time happy",
         {"entities": [(23, 37, "ct"), (39, 47, "ct"), (66, 71, "ct")]}),

        ("I want a person who is not pushy, but friendly",
         {"entities": [(23, 32, "ct"), (38, 46, "ct")]}),

        ("I want somebody who isn't aggressive, but very friendly",
         {"entities": [(22, 36, "ct"), (47, 55, "ct")]}),

        ("I want somebody who isn't happy and isn't rude, but friendly",
         {"entities": [(22, 31, "ct"), (38, 46, "ct"), (52, 60, "ct")]}),

        ("I want a person who isn't happy, not aggressive, but rude",
         {"entities": [(22, 31, "ct"), (33, 47, "ct"), (53, 57, "ct")]}),

        ]
    return TRAIN_DATA
