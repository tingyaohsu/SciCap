import json
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu
from pprint import pprint
from nltk.tokenize import word_tokenize



ground = 'TEST_IMG_CAPTIONS_LIST.json'
with open(ground,'r',encoding='utf-8') as f:
	data = json.load(f)

cap_list = []
for k, v in data.items():
	cap_list.append(v['ori_cap'])

cap_list = sorted(cap_list)
# print(len(cap_list))
# print(cap_list[:5])



gen_data = 'none_gen_results/none_all_sent_1_eval_results.json'

with open(gen_data,'r',encoding='utf-8') as f:
	data = json.load(f)

hypo_list = []
for v in data['gold']:
	hypo_list.append(v)

hypo_list = sorted(hypo_list)
# print(len(hypo_list))
# print(hypo_list[:5])


bleu4 = 0
for (h,g) in zip(data['hypo'],data['gold']):
	print(h)
	print(g)

	hypo = word_tokenize(h)
	ref = [word_tokenize(g)]
	print('bleu score:',sentence_bleu(ref,hypo))
	print()
	# print(hypo,ref)
	bleu4 += sentence_bleu(ref,hypo)


print(bleu4/len(data['hypo']))
exit()

print(len(data['hypo']))


print()
print(len(data['gold']))
