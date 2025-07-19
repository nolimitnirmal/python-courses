import random 

def person_new(name, age, eyes, job):
    job_stats = {
        "boxer":{"hp":100, "damage": 20}, 
        "teacher":{"hp":70, "damage": 10}, 
        "baby":{"hp":30, "damage": 5}, 
    }

    stats = job_stats.get(job, {"hp": 50, "damage": 8})  # default stats

    person = {
        "name": name, 
        "age": age,
        "eyes": eyes,
        "job": job, 
        "hit_points": stats["hp"], 
        "damages": stats["damages"],
    }

    def talk(words):
        print(f"I am {person['name']}, a {person['job']}, and {words}")

    def hit (other):
        if person["hit_person"] <= 0:
            print(f"{person['name']}) can't fight. They're already out!")


        damage = random.randint(1, person[damage])

        
        