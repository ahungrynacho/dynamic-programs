from copy import deepcopy

class Job:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value
        
def schedule(jobs):
    table = [j.value for j in jobs]
    result = []
    
    for i in range(0, len(jobs)):
        for j in range(0, i):
            total = jobs[i].value + table[j]
            if (jobs[j].end <= jobs[i].start or jobs[i].end <= jobs[j].start) and total > table[i]:
                table[i] = total
        result.append(deepcopy(table))
        
    return result

if __name__ == "__main__":
    jobs = [Job(1,3,5), Job(2,5,6), Job(4,6,5), Job(6,7,4), Job(5,8,11), Job(7,9,2)]
    jobs2 = [Job(1,3,5), Job(2,5,6), Job(5,8,11), Job(4,6,5), Job(6,7,4), Job(7,9,2)]
    
    for line in schedule(jobs):
        print(line)
    
    
    