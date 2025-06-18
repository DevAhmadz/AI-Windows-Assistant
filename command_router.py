def run_command(intent):
    """Simulate running a system command based on detected intent."""
    
    responses = {
        "reset_network": "✔ Network reset simulated (netsh winsock reset)",
        "restart_explorer": "✔ Explorer restarted (taskkill + start explorer.exe)",
        "clear_temp": "✔ Temp files cleared (simulated)",
    }

    if intent in responses:
        return responses[intent]
    else:
        return "❌ No matching command found."
