class PlannerAgent:
    def plan(self, workflow_name):
        if workflow_name == "employee_onboarding":
            return [
                "Verify Documents",
                "Create Employee Account",
                "Assign Department",
                "Send Welcome Email"
            ]
        return []