from logger import logger
import threading
from .splash_cash_detector import detect_splash_cash_outcome_async

def execute_comp(alert_type: str):
    """
    Execute Splash The Cash IMMEDIATE alarm message.
    This sends the "GO time! The alarm has sounded" message within 3 seconds.
    The outcome detection runs separately in background.
    
    Args:
        alert_type (str): The type of alert that triggered this competition
        
    Returns:
        tuple: (comp_name, alarm_message) - immediate alarm message for users
    """
    logger.info(f"Executing Splash The Cash ALARM with alert_type: {alert_type}")
    
    try:
        # Start background outcome detection (non-blocking)
        logger.info("Starting background outcome detection thread")
        detection_thread = threading.Thread(
            target=detect_splash_cash_outcome_async,
            args=(alert_type,),
            daemon=True
        )
        detection_thread.start()
        
        # Return immediate alarm message (this will be sent within 3 seconds)
        comp_name = "Splash The Cash"
        # This message is handled by the existing template in constants.py: MESSAGES_TEMPLATES["Splash The Cash"]
        # It will be formatted as: "Hi {name}, it's GO time! The alarm has sounded..."
        alarm_message = "ALARM"  # Placeholder - the messaging server will use the template
        
        logger.info(f"Returning immediate alarm message for: {comp_name}")
        return comp_name, alarm_message
        
    except Exception as e:
        logger.error(f"Error in Splash The Cash alarm execution: {str(e)}")
        logger.exception("Full alarm execution error traceback:")
        # Still return alarm message even if background detection fails
        return "Splash The Cash", "ALARM"