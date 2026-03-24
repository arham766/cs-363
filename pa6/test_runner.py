import os
import subprocess

tests_dir = "tests"
outputs_dir = "outputs"
passed = 0
failed = 0

print("Testing passing cases:")
for i in range(15):
    ac_file = f"{tests_dir}/test{i}.ac"
    my_dc = f"{tests_dir}/test{i}.dc"
    gold_dc = f"{outputs_dir}/test{i}.dc"

    try:
        subprocess.run(["python", "acdc.py", ac_file, my_dc], check=True, capture_output=True)
    except Exception as e:
        print(f"Test test{i}.ac FAIL (Compilation error)")
        failed += 1
        continue

    with open(my_dc, 'r') as f:
        my_out = f.read().strip()
    with open(gold_dc, 'r') as f:
        gold_out = f.read().strip()

    if my_out == gold_out:
        print(f"Test test{i}.ac PASS")
        passed += 1
    else:
        print(f"Test test{i}.ac FAIL")
        print("--- Expected ---")
        print(gold_out)
        print("--- Got ---")
        print(my_out)
        failed += 1

print("\nTesting expected failure cases:")

for i in range(15):
    ac_file = f"{tests_dir}/testfail{i}.ac"
    my_dc = f"{tests_dir}/testfail{i}.dc"

    result = subprocess.run(["python", "acdc.py", ac_file, my_dc], capture_output=True)

    if result.returncode != 0:
        print(f"Test testfail{i}.ac PASS (Correctly failed to compile)")
        passed += 1
    else:
        print(f"Test testfail{i}.ac FAIL (Should have failed to compile, but succeeded)")
        failed += 1

print(f"\n{passed} total tests passed, {failed} total tests failed")
