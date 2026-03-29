class VerificationAgent:
    def verify(self, step, result):
        print("Verifying result...")

        if result.get("status") == "success":
            print("Verification passed")
            return True

        print("Verification failed")
        return False