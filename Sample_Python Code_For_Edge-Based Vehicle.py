#Python Example: Edge-Based Vehicle Diagnostics (Safe Simulation)Requirements

#Runs on an embedded edge device
#Uses simulated CAN-bus data
#Detects anomalies & potential system weaknesses

import time
import random

# Simulated CAN messages
def generate_can_message():
    return {
        "speed": random.randint(0, 200),
        "rpm": random.randint(500, 7000),
        "brake_status": random.choice([0, 1]),
        "steering_angle": random.randint(-45, 45)
    }

# Simple rule-based anomaly detection on the edge
def detect_anomalies(msg):
    issues = []

    # Example logic rules
    if msg["speed"] > 180:
        issues.append("Unusual speed detected")

    if msg["rpm"] > 6500:
        issues.append("High RPM risk")

    if msg["speed"] > 0 and msg["brake_status"] == 1:
        issues.append("Brake engaged while moving")

    if abs(msg["steering_angle"]) > 40:
        issues.append("Dangerous steering angle")

    return issues

# Basic edge analytics for identifying potential loopholes
def identify_loopholes(system_health_data):
    loopholes = []

    # Loophole 1: No message authentication
    if not system_health_data.get("auth_enabled"):
        loopholes.append("Missing CAN message authentication – system vulnerable to spoofing")

    # Loophole 2: No rate limiting
    if system_health_data.get("msg_rate") > 500:
        loopholes.append("High message rate – potential for CAN flooding attacks")

    # Loophole 3: Lack of encryption
    if not system_health_data.get("encryption"):
        loopholes.append("CAN data unencrypted – susceptible to sniffing")

    # Loophole 4: No edge firmware integrity check
    if not system_health_data.get("firmware_secure_boot"):
        loopholes.append("Secure boot disabled – risk of malicious firmware")

    return loopholes


# MAIN EDGE LOOP
system_health = {
    "auth_enabled": False,
    "msg_rate": 650,   # simulated values
    "encryption": False,
    "firmware_secure_boot": False
}

print("Edge Vehicle Diagnostic Module Running...\n")

for _ in range(10):  # simulate 10 messages
    msg = generate_can_message()
    anomalies = detect_anomalies(msg)
    loopholes = identify_loopholes(system_health)

    print("CAN MESSAGE:", msg)
    if anomalies:
        print("⚠️  Anomalies Detected:", anomalies)
    if loopholes:
        print("🔓 Potential Loopholes:", loopholes)
    print("—" * 40)
    time.sleep(0.5)