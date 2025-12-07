#!/usr/bin/env python3
import requests
import time
import subprocess
import sys

def test_app():
    print("Starting Flask app...")
    proc = subprocess.Popen([sys.executable, 'app.py'], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
    time.sleep(3)
    
    try:
        print("Testing login page...")
        response = requests.get('http://127.0.0.1:5000/')
        assert response.status_code == 200
        assert 'VoiceBank Africa' in response.text
        print("✓ Login page works")
        
        print("\nAll tests passed! ✓")
        print("\nYou can now access the app at: http://127.0.0.1:5000/")
        print("Test users: jabelo or thabo")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
    finally:
        proc.terminate()
        proc.wait()

if __name__ == '__main__':
    test_app()
