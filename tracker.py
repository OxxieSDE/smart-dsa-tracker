import json
import os

FILE_NAME = "data.json"

# Load data
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add a new problem
def add_problem():
    topic = input("Enter topic (Array/String/DP/etc): ")
    name = input("Enter problem name: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ")

    data = load_data()
    data.append({
        "topic": topic,
        "name": name,
        "difficulty": difficulty,
        "revised": 0
    })
    save_data(data)
    print("✅ Problem added successfully!")

# View all problems
def view_problems():
    data = load_data()
    if not data:
        print("No problems added yet.")
        return

    for i, p in enumerate(data, 1):
        print(f"{i}. {p['name']} | {p['topic']} | {p['difficulty']} | Revised: {p['revised']}")

# Revise a problem
def revise_problem():
    data = load_data()
    view_problems()
    index = int(input("Enter problem number to revise: ")) - 1

    if 0 <= index < len(data):
        data[index]["revised"] += 1
        save_data(data)
        print("🔁 Revision updated!")
    else:
        print("❌ Invalid choice")

# Analytics
def analytics():
    data = load_data()
    print(f"📊 Total problems solved: {len(data)}")

    easy = sum(1 for p in data if p["difficulty"] == "Easy")
    medium = sum(1 for p in data if p["difficulty"] == "Medium")
    hard = sum(1 for p in data if p["difficulty"] == "Hard")

    print(f"Easy: {easy}, Medium: {medium}, Hard: {hard}")

# Menu
while True:
    print("\n--- Smart DSA Tracker ---")
    print("1. Add Problem")
    print("2. View Problems")
    print("3. Revise Problem")
    print("4. View Analytics")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_problem()
    elif choice == "2":
        view_problems()
    elif choice == "3":
        revise_problem()
    elif choice == "4":
        analytics()
    elif choice == "5":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice")
