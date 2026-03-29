class DecisionAgent:
    def make_decision(self, step, data):
        print("Making decision...")

        if step == "Verify Documents":
            if data.get("documents") == "submitted":
                return "approved"
            return "rejected"

        if step == "Assign Department":
            if data.get("role") == "Engineer":
                return "Engineering Department"
            return "General"

        return "proceed"