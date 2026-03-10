import json
import glob
import shutil

with open('./pahcer/best_scores.json', 'r') as f:
    best_scores = json.load(f)

logs = glob.glob('./pahcer/json/*')
logs.sort()

last_log = logs[-1]

with open(last_log, 'r') as f:
    last_scores = json.load(f)


updates = []

for data in last_scores['cases']:
    index = str(data['seed']).zfill(4)
    score = data['score']
    if best_scores[index] == score:
        print(index,score)
        updates.append(index)
    

for index in updates:
    result_path = f"./tools/out/{index}.txt"
    output_path = f"./best/{index}.txt"

    print("copy:", result_path, "->", output_path)
    shutil.copy(result_path, output_path)




