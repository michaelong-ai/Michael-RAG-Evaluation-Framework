import json
with open("eval/v1_results.json") as f:
    v1_results = json.load(f)
with open("eval/v2_results.json") as f:
    v2_results = json.load(f)
with open("eval/v3_results.json") as f:
    v3_results = json.load(f)

v1_total_score = sum(item["total"] for item in v1_results)
v2_total_score = sum(item["total"] for item in v2_results)
v3_total_score = sum(item["total"] for item in v3_results)
v1_factual = sum(item["factual_correctness"] for item in v1_results)
v1_groundedness = sum(item["groundedness"] for item in v1_results)
v1_completeness = sum(item["completeness"] for item in v1_results)
v2_factual = sum(item["factual_correctness"] for item in v2_results)
v2_groundedness = sum(item["groundedness"] for item in v2_results)
v2_completeness = sum(item["completeness"] for item in v2_results)
v3_factual = sum(item["factual_correctness"] for item in v3_results)
v3_groundedness = sum(item["groundedness"] for item in v3_results)
v3_completeness = sum(item["completeness"] for item in v3_results)

print("=" * 50)
print("     RAG EVAL REPORT — BASIC FINANCIAL PLANNING GUIDE")
print("=" * 50)
print("Overall Scores")
print("-" * 50)
max_score = len(v1_results) * 9
print(f"Prompt V1 (sabotaged):   {v1_total_score:3d} / {max_score} ({v1_total_score / max_score * 100:5.1f}%)")
print(f"Prompt V2 (production):  {v2_total_score:3d} / {max_score} ({v2_total_score / max_score * 100:5.1f}%)")
print(f"Prompt V3 (improved):    {v3_total_score:3d} / {max_score} ({v3_total_score / max_score * 100:5.1f}%)")
scores = [v1_total_score, v2_total_score, v3_total_score]
winner_idx = scores.index(max(scores))
winners = ["V1", "V2", "V3"]
print(f"\nWinner: Prompt {winners[winner_idx]}")
print("\n" + "=" * 50)
print("SCORES BY DIMENSION")
print("=" * 50)
print(f"{'Metric':<20} {'V1':<15} {'V2':<15} {'V3':<15}")
print("-" * 50)
print(f"{'Factual Correctness':<20} {v1_factual}/{len(v1_results)*3:<13} {v2_factual}/{len(v2_results)*3:<13} {v3_factual}/{len(v3_results)*3:<13}")
print(f"{'Groundedness':<20} {v1_groundedness}/{len(v1_results)*3:<13} {v2_groundedness}/{len(v2_results)*3:<13} {v3_groundedness}/{len(v3_results)*3:<13}")
print(f"{'Completeness':<20} {v1_completeness}/{len(v1_results)*3:<13} {v2_completeness}/{len(v2_results)*3:<13} {v3_completeness}/{len(v3_results)*3:<13}")
