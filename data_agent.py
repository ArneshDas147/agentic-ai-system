class DataAgent:
    def get_data(self, step):
        print("Fetching data...")

        dummy_data = {
            "Verify Documents": {"documents": "submitted"},
            "Create Employee Account": {"username": "new_employee"},
            "Assign Department": {"role": "Engineer"},
            "Send Welcome Email": {"email": "employee@example.com"}
        }

        return dummy_data.get(step, {})