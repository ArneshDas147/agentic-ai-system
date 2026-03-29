from agents.planner_agent import PlannerAgent
from agents.data_agent import DataAgent
from agents.decision_agent import DecisionAgent
from agents.action_agent import ActionAgent
from agents.verification_agent import VerificationAgent
from agents.audit_agent import AuditAgent
import time

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.data = DataAgent()
        self.decision = DecisionAgent()
        self.action = ActionAgent()
        self.verify = VerificationAgent()
        self.audit = AuditAgent()

    def start_workflow(self, workflow_name):
        self.audit.log(f"Workflow started: {workflow_name}")

        steps = self.planner.plan(workflow_name)

        for step in steps:
            print(f"\nExecuting: {step}")
            self.audit.log(f"Step started: {step}")

            try:
                data = self.data.get_data(step)
                decision = self.decision.make_decision(step, data)

                result = self.action.execute(step, decision)

                verified = self.verify.verify(step, result)

                if not verified:
                    self.audit.log(f"Verification failed. Retrying: {step}")
                    print("Retrying step...")
                    result = self.action.execute(step, decision)

                self.audit.log(f"Step completed: {step}")

            except Exception as e:
                self.audit.log(f"Error in step {step}: {str(e)}")
                print("Error occurred, skipping step.")

            time.sleep(1)

        self.audit.log("Workflow completed successfully")