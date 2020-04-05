import spacy
import random
from NER_inputfield import ner_traindata


def train_spacy(data, iterations):
    TRAIN_DATA = data
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)

    # add labels
    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations):
            print("Starting iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update(
                    [text],  # batch of texts
                    [annotations],  # batch of annotations
                    drop=0.2,  # dropout - make it harder to memorise data
                    sgd=optimizer,  # callable to update weights
                    losses=losses)
            print(losses)
    return nlp


def get_character_traits(all_entities):
    character_traits_chatbot = {"friendly", "happy", "aggressive", "rude", "lazy", "pushy"}
    character_traits = []

    for entity in all_entities:
        for ct in character_traits_chatbot:
            if entity == ct and entity not in character_traits:
                character_traits.append(ct)

    if len(character_traits) == 0:
        character_traits.append("friendly")

    json_data = {"Id": 1, "character_traits": character_traits}

    print(json_data)

    return json_data


def get_json_data_from_input(text_input):
    TRAIN_DATA = ner_traindata.get_train_data()
    try:
        spacy.load('NER_inputfield/ner_model')
        print("TEST")
        trainable = False  # Must be False
    except IOError:
        trainable = True

    if trainable:
        print("TRAINING")
        prdnlp = train_spacy(TRAIN_DATA, 20)

        # Save our trained Model
        prdnlp.to_disk('NER_inputfield/ner_model')
    else:
        print("NO TRAINING")
        nlp = spacy.load('NER_inputfield/ner_model')

        prdnlp = nlp

    test_text = text_input
    doc = prdnlp(test_text)

    all_entities = []

    for ent in doc.ents:
        all_entities.append(ent.text)
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

    return get_character_traits(all_entities)
