from crewai import Agent, Crew
import subprocess
import threading

class MicrostructureAnalyst(Agent):
    def __init__(self):
        super().__init__(
            name="MicrostructureAnalyst",
            role="Signal Evaluator",
            goal="Detect spoofing, imbalance, or stale book conditions",
            backstory="An AI trained in market microstructure theory to evaluate crypto trading environments in real time."
        )

    def run(self):
        print("[Crew] MicrostructureAnalyst launched")
        subprocess.Popen(["python", "crew_ai/agents/microstructure_agent.py"])


class OrderBookSniper(Agent):
    def __init__(self):
        super().__init__(
            name="OrderBookSniper",
            role="Book Depth Monitor",
            goal="Track order book changes and spoofing patterns",
            backstory="A sniper AI that detects liquidity vacuums and spoof activity in Binance order book feeds."
        )

    def run(self):
        print("[Crew] OrderBookSniper launched")
        subprocess.Popen(["python", "core/bookwatcher.py"])


analyst = MicrostructureAnalyst()
sniper = OrderBookSniper()

crew = Crew(name="MicrostructureOps", agents=[sniper, analyst])

if __name__ == "__main__":
    print("[mission_control] Deploying AI crew...")
    threading.Thread(target=crew.kickoff).start()
