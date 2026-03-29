import random

class ActionAgent:
    def execute(self, step, decision):
        print(f"Executing action for {step} with decision: {decision}")

        # Simulate random failure for demo
        if random.randint(1, 10) <= 2:
            print("Simulated failure!")
            return {"status": "failed"}

        return {"status": "success"}