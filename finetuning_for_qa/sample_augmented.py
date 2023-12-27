# sample_augmented(squad2_file, input_augmented_file, output_sampled_file, number_of_questions, seed)
#
# example usage:
# from sample_augmented import sample_augmented
# sample_augmented('/data/users/vgautam/albert-qa/squad2.json', '/data/users/vgautam/albert-qa/squad_all_ppl.json', 'test.json', 100, 131719)

import json
import random

def sample_augmented(human_generated_file, input_file, output_file, n_qs, seed):
    random.seed(seed)

    with open(human_generated_file, encoding='utf-8') as f:
        dataset_json1 = json.load(f)
        squad2 = dataset_json1['data']

    with open(input_file, encoding='utf-8') as f:
        dataset_json2 = json.load(f)
        aug = dataset_json2['data']

    # first go through the whole thing once and count how many non-human-generated unanswerable questions there are
    counter = 0
    for i,topic in enumerate(squad2):
        for j,paragraph in enumerate(topic['paragraphs']):
            human_impossible_qs = [qa for qa in paragraph['qas'] if qa['is_impossible'] == True]
            aug_qs = [qa for qa in aug[i]['paragraphs'][j]['qas'] if qa['is_impossible'] == True and qa not in human_impossible_qs]
            counter += len(aug_qs)

    # then pick a random sample of n_qs from that number
    possibilities = list(range(counter))
    sample = set(random.sample(possibilities, n_qs))

    # go through again and pick according to whether they're in the sample or not
    counter = 0
    for i,topic in enumerate(squad2):
        for j,paragraph in enumerate(topic['paragraphs']):
            new_qas = [qa for qa in paragraph['qas']]
            human_impossible_qs = [qa for qa in paragraph['qas'] if qa['is_impossible'] == True]
            aug_qs = [qa for qa in aug[i]['paragraphs'][j]['qas'] if qa['is_impossible'] == True and qa not in human_impossible_qs]
            for qa in aug_qs:
                if counter in sample:
                    new_qas.append(qa)
                counter += 1
            paragraph['qas'] = new_qas
    
    # write the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset_json1, f, indent='    ')
