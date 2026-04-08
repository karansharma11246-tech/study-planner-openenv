from study_env import StudyEnv

env = StudyEnv()

def test_env():
    # Reset environment
    reset_res = env.reset()
    print("Reset Response:", reset_res)

    # Sample step
    action = ["Math", "Physics", "English"]
    reward = env.step(action)
    print("Step Response:", reward)

def main():
    test_env()

if __name__ == "__main__":
    main()
