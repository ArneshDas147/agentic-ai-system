from agents.orchestrator import Orchestrator

if __name__ == "__main__":
    print("Starting AutoFlow AI System...\n")

    orchestrator = Orchestrator()
    orchestrator.start_workflow("employee_onboarding")

    print("\nWorkflow execution finished.")