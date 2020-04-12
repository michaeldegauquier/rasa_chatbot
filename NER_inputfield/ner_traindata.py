def get_train_data():
    # ct = character trait
    # age = age of the person
    # gender = gender of the person
    # glasses = is the person wearing glasses (true or false)
    # ety = ethnicity (caucasian, african, southern, asian)

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

        ("I want a person who isn't happy, not aggressive, but rude",
         {"entities": [(22, 31, "ct"), (33, 47, "ct"), (53, 57, "ct")]}),

        ("I want a person who is Chinese, is happy and is wearing glasses.",
         {"entities": [(23, 30, "ety"), (35, 40, "ct"), (48, 63, "glasses")]}),

        ("I want a person who is not wearing glasses and is always friendly to me.",
         {"entities": [(23, 42, "glasses"), (57, 65, "ct")]}),

        ("I want somebody who is an African and 45 years old. He must be a happy person who is sometimes aggressive.",
         {"entities": [(26, 33, "ety"), (38, 40, "age"), (52, 54, "gender"), (65, 70, "ct"), (95, 105, "ct")]}),

        ("I want a woman who is aggressive and is wearing glasses.",
         {"entities": [(9, 14, "gender"), (22, 32, "ct"), (40, 55, "glasses")]}),

        ("I want a woman who is happy and friendly. She must wear glasses and an age of 26.",
         {"entities": [(9, 14, "gender"), (22, 27, "ct"), (32, 40, "ct"), (51, 63, "glasses"), (78, 80, "age")]}),

        ("I want a man who is 38 years old and who is Japanese.",
         {"entities": [(9, 12, "gender"), (20, 22, "age"), (44, 52, "ety")]}),

        ("I want a man who is rude and is not wearing glasses. He must have an age of 48.",
         {"entities": [(9, 12, "gender"), (20, 24, "ct"), (32, 51, "glasses"), (53, 55, "gender"), (76, 78, "age")]}),

        ("I want somebody who is a woman and has children. She must wear glasses and she is very aggressive.",
         {"entities": [(25, 30, "gender"), (49, 52, "gender"), (58, 70, "glasses"), (75, 78, "gender"),
                       (87, 97, "ct")]}),

        ("I want somebody who is aggressive and is not wearing glasses. He must be a very happy person sometimes and has to be a Chinese.",
         {"entities": [(23, 33, "ct"), (41, 60, "glasses"), (62, 64, "gender"), (80, 85, "ct"), (119, 126, "ety")]}),

        ("I want to talk to somebody who is a woman. She must be a happy and friendly person. Her nationality is Belgian and she has 3 children.",
         {"entities": [(36, 41, "gender"), (43, 46, "gender"), (57, 62, "ct"), (67, 75, "ct"), (103, 110, "ety"),
                       (115, 118, "gender")]}),

        ("I want a person who is happy. He must be a Japanese and must wear glasses.",
         {"entities": [(23, 28, "ct"), (30, 32, "gender"), (43, 51, "ety"), (61, 73, "glasses")]}),

        ("She must wear glasses and must be an aggressive chinese woman.",
         {"entities": [(0, 3, "gender"), (9, 21, "glasses"), (37, 47, "ct"), (48, 55, "ety")]}),

        ("I want somebody who is Japanese and does not wear glasses. She must be very happy all the time and has an age of 34.",
         {"entities": [(23, 31, "ety"), (41, 57, "glasses"), (59, 62, "gender"), (76, 81, "ct"), (113, 115, "age")]}),

        ("She is a very happy person. Sometimes she is very aggressive and rude to people. She has an age of 55.",
         {"entities": [(0, 3, "gender"), (14, 19, "ct"), (38, 41, "gender"), (50, 60, "ct"), (65, 69, "ct"),
                       (99, 101, "age")]}),

        ("I want a person who is rude and does wear glasses. He is a Chinese business man and has a great house in the middle of nowhere.",
         {"entities": [(23, 27, "ct"), (37, 49, "glasses"), (51, 53, "gender"), (59, 66, "ety"), (76, 79, "gender")]}),

        ("He has an age of 65. He is an old business man who has children. His nationality is Belgian. He is very friendly to everybody but has an aggressive dark side.",
         {"entities": [(0, 2, "gender"), (17, 19, "age"), (21, 23, "gender"), (43, 46, "gender"), (65, 68, "gender"),
                       (84, 91, "ety"), (93, 95, "gender"), (104, 112, "ct"), (137, 147, "ct")]}),

        ("I want a person who's 30 years old and he must be happy, also aggressive, sometimes rude. Why you gotta be so rude.",
         {"entities": [(22, 24, "age"), (50, 55, "ct"), (62, 72, "ct"), (84, 88, "ct"), (110, 114, "ct")]}),

        ("The woman wears glasses. She is a very happy and friendly person. Sometimes she is very pushy but that's it. And yes she is from belgium. She also lives in a mansion.",
         {"entities": [(4, 9, "gender"), (10, 23, "glasses"), (25, 28, "gender"), (39, 44, "ct"), (49, 57, "ct"),
                       (76, 79, "gender"), (88, 93, "ct"), (117, 120, "gender"), (129, 136, "ety"),
                       (138, 141, "gender")]}),

        ("She must have a big house. She is somebody who is very aggressive and pushy. Sometimes she is rude, but not more.",
         {"entities": [(0, 3, "gender"), (27, 30, "gender"), (55, 65, "ct"), (70, 75, "ct"), (87, 90, "gender"),
                       (94, 98, "ct")]}),

        ("I want somebody who is lazy and rude. She must wear glasses and must have an age of 34.",
         {"entities": [(23, 27, "ct"), (32, 36, "ct"), (47, 59, "glasses"), (84, 86, "age")]}),

        ("He is somebody who lives in a big mansion on the west coast in america. He is a person who is very aggressive, but most of the time happy and lazy. When he read a book, he wear glasses.",
         {"entities": [(0, 2, "gender"), (72, 74, "gender"), (99, 109, "ct"), (132, 137, "ct"), (142, 146, "ct"),
                       (172, 184, "glasses")]}),

        ("Her nationality is belgian. She is a very happy woman, but sometimes lazy. and she is 45 years old.",
         {"entities": [(19, 26, "ety"), (28, 31, "gender"), (42, 47, "ct"), (69, 73, "ct"), (79, 82, "gender"),
                       (86, 88, "age")]}),

        ("She is very smart. She is all the time happy and friendly to everybody. Sometimes she wears glasses and she is 26 years old. She is from belgium.",
         {"entities": [(0, 3, "gender"), (19, 22, "gender"), (39, 44, "ct"), (49, 57, "ct"), (82, 85, "gender"),
                       (86, 99, "glasses"), (104, 107, "gender"), (111, 113, "age"), (125, 128, "gender"),
                       (137, 144, "ety")]}),

    ]
    return TRAIN_DATA

# K. Jaiswal. Custom Named Entity Recognition Using Spacy. Geraadpleegd via
# https://towardsdatascience.com/custom-named-entity-recognition-using-spacy-7140ebbb3718
# Geraadpleegd op 4 april 2020

# M. Murugavel. How to Train NER with Custom training data using spaCy. Geraadpleegd via
# https://medium.com/@manivannan_data/how-to-train-ner-with-custom-training-data-using-spacy-188e0e508c6
# Geraadpleegd op 4 april 2020

# M. Murugavel. Train Spacy ner with custom dataset. Geraadpleegd via
# https://github.com/ManivannanMurugavel/spacy-ner-annotator
# Geraadpleegd op 4 april 2020
