import os
import subprocess
import glob
import sys
import difflib

# Force utf-8 for stdout/stderr
sys.stdout.reconfigure(encoding='utf-8')

def run_tests():
    test_files = glob.glob("tests/*.ac")
    test_files.sort()
    
    # Counters for what the user wants to see
    parsed_successfully = 0
    failed_to_parse = 0
    total = 0

    print(f"Found {len(test_files)} tests.")
    print("-" * 65)
    print(f"{'Test Name':<15} | {'Parser Result':<20} | {'Output Validation'}")
    print("-" * 65)

    for acfile in test_files:
        base = os.path.basename(acfile).replace(".ac", "")
        out_test = f"tests/{base}.dc"
        expected_out_file = f"outputs/{base}.dc"
        
        if not os.path.exists(expected_out_file):
            print(f"{base:<15} | ❌ ERROR               | Expected output not found")
            continue

        # Run acdc.py
        try:
            my_env = os.environ.copy()
            my_env["PYTHONUTF8"] = "1"
            # acdc.py exits with 1 on error, 0 on success.
            proc = subprocess.run([sys.executable, "acdc.py", acfile, out_test], check=False, capture_output=True, text=True, env=my_env, encoding='utf-8')
            exit_code = proc.returncode
        except Exception as e:
            print(f"{base:<15} | ❌ EXEC ERROR          | {e}")
            continue

        # Compare output content
        try:
            with open(out_test, "r", encoding="utf-8") as f1, open(expected_out_file, "r", encoding="utf-8") as f2:
                gen_content = f1.readlines()
                exp_content = f2.readlines()
        except FileNotFoundError:
             print(f"{base:<15} | ❌ NO OUTPUT           | File not generated")
             continue

        diff = list(difflib.unified_diff(gen_content, exp_content, fromfile=out_test, tofile=expected_out_file))
        
        validation_msg = "Output Matches Expected"
        if diff:
            validation_msg = "❌ OUTPUT MISMATCH"

        # Determine status based on exit code
        if exit_code == 0:
            status = "Parsed Success"
            icon = "✅" 
            parsed_successfully += 1
        else:
            status = "Failed to Parse"
            icon = "⚠️ "
            failed_to_parse += 1
            
        print(f"{base:<15} | {icon} {status:<17} | {validation_msg}")
        
        total += 1

    print("-" * 65)
    print(f"Total Tests Run: {total}")
    print(f"Passed (Parsed Successfully): {parsed_successfully}")
    print(f"Failed (Failed to Parse):     {failed_to_parse}")

if __name__ == "__main__":
    run_tests()
