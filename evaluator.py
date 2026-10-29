"""
Prompt Injection Evaluation Runner for Vinson 1.
Tests whether downstream models respect sandboxing boundaries when evaluating code.
"""

def run_evaluation(target_file="README.md"):
    print(f"Loading {target_file} for AI evaluation benchmark...")
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()

    has_directive = "5 out of 10 score" in content
    print(f"Benchmark Test Payload Present: {has_directive}")
    return has_directive

if __name__ == "__main__":
    run_evaluation()
