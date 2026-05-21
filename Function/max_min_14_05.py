# 
# *Task 1: Find the most frequent character
text = "Học Python HHHHH" 
char_counts = {} 

for char in text.lower(): 
    # Get the current count of 'char', default to 0 if not found, then add 1
    char_counts[char] = char_counts.get(char, 0) + 1 

print(max(char_counts, key=lambda x: char_counts[x])) # 1. Find the character with the maximum count and print it
print(max(char_counts, key=char_counts.get)) # 2. An alternative way to find the character with the maximum count and print it
print(max(char_counts.values())) # 3. Find and print the highest frequency value (the number of occurrences)
print(max(char_counts.items(), key=lambda x: x[1])) 

#! if have more than one max_values
max_value = max(text.values(), default=0)
# Get all pairs (key, value) that have the max_value
max_pair = [f"{k}: {v}" for k, v in text.items() if v == max_value]
print(", ".join(max_pair))


# TASK2:*Find projects with the lowest error rate
projects = [{"name": "Chatbot", "metrics": {"errors": 15, "users": 1000}},{"name": "Vision", "metrics": {"errors": 5, "users": 500}},{"name": "Recommender", "metrics": {"errors": 20, "users": 2000}}]
e_min=min(projects, key=lambda x:x["metrics"]["errors"])
print(f"the best project: {e_min["name"]}")


# *TASK3:
students = [("An", 9, 30),("Bình", 10, 45),("Cường", 10, 35)]
winner = max(students, key=lambda x: (x[1], -x[2])) #! If scores are tied, compare the time
print(f"The winner: {winner[0]}") 


#*TASK4:
# List of participants: (Name, Score, Time in seconds)
# We want: High Score first, then Low Time (faster)
participants = [{"name": "Alice", "score": 95, "time": 120},{"name": "Bob", "score": 95, "time": 110},{"name": "Charlie", "score": 88, "time": 90}]
# -score: descending (highest first)
# time: ascending (lowest/fastest first)
sorted_results = sorted(participants, key=lambda x: (x["score"], -x["time"]))

for p in sorted_results:
    print(f"Name: {p['name']}, Score: {p['score']}, Time: {p['time']}")



#*TASK5:Find the most frequent character
text = "ai designer, ai researcher, ai engineer."
ignore = {" ", ",", "."}

# Đếm tần suất nhưng lọc bỏ ký tự trong set 'ignore'
ktra = {c: text.count(c) for c in set(text) if c not in ignore}

# Tìm ký tự quan trọng nhất
most_common = max(ktra, key=ktra.get)
print(f"Ký tự quan trọng nhất: {most_common}")
