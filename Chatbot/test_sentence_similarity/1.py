from sentence_transformers import SentenceTransformer, util
import os
import re

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')


def get_similar_use_case(query: str):
    root_dir = r"Similar_check_TextFiles"
    file_names = os.listdir(root_dir)
    allscore = []
    for file_name in file_names:
        file_path = os.path.join(root_dir, file_name)
        with open(f"{file_path}", 'r') as f:
            text = f.read()
        sentences = [sentence.strip() for sentence in re.split(r'[.!?]', text) if sentence.strip()]
        mscore = -10
        for sen in sentences:
            embed1 = model.encode(sen, convert_to_tensor=True)
            embed2 = model.encode(query, convert_to_tensor=True)
            cosine_score = util.pytorch_cos_sim(embed2, embed1)
            mscore = max(mscore,cosine_score)
        allscore.append([mscore,file_name])
    temp = [i for i,j in allscore]
    result = [[msc, fname] for msc, fname in allscore if msc == max(temp)]
    return result[0]

a = get_similar_use_case('I need to apply for my accounts information')
e1 = model.encode('I want to know about the fee payment details of the campus', convert_to_tensor=True)
e2 = model.encode('I want to file a request for fee receipt information ', convert_to_tensor=True)
print(util.pytorch_cos_sim(e1,e2))
