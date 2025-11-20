import threading
import random
import time

PPU = 10
NUM_R = 5
NUM_A = 10
NUM_W = 4

class Warehouse:
    def __init__(self, n, m):
        self.name, self.meds = n, m
        self.lock = threading.Lock()

    def steal(self, a):
        with self.lock:
            if self.meds == 0:
                return 0
            if random.random() < 0.15:
                return 0
            
            stolen = min(a, self.meds)
            self.meds -= stolen
            return stolen

class Runner(threading.Thread):
    def __init__(self, n, ws):
        super().__init__()
        self.name, self.warehouses = n, ws
        self.total_profit = 0

    def run(self):
        for _ in range(NUM_A):
            w = random.choice(self.warehouses)
            amount = random.randint(10, 30)
            stolen = w.steal(amount)
            self.total_profit += stolen * PPU
            time.sleep(random.uniform(0.1, 0.5))
            
        print(f"Runner {self.name} finished. Total profit: {self.total_profit}")

def Simulation(id):
    print("="*30)
    print(f"Simulation #{id} started")
    print("="*30)
    
    ws = [Warehouse(f"W-{i+1}", random.randint(100, 300)) for i in range(NUM_W)]
    
    initial_meds = sum(w.meds for w in ws)
    print(f"Initial Meds Total: {initial_meds}")
    
    rs = []

    for i in range(NUM_R):
        r = Runner(f"R={i+1}", ws) 
        rs.append(r)
        r.start()
        
    for r in rs:
        r.join()

    earnings = sum(r.total_profit for r in rs)
    return earnings

if __name__ == "__main__":
    results = {f"Simulation #{i}": Simulation(i) for i in range(1, 4)}
    
    print("Final Summary")
    for sim_id, earnings in results.items():
        print(f"{sim_id}: {earnings}") 