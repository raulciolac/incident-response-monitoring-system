import os
print("Restarting app...")
os.system("kubectl rollout restart deployment incident-app")
