"""
Main entry point for the Instagram Content Agent
"""
if __name__ == "__main__":
    print(" Starting Instagram Content Agent for you page")
    print("=" * 60)

    # Import and run the scheduler
    from scheduler import start_scheduler

    try:
        start_scheduler()
    except Exception as e:
        print(f" Failed to start agent: {e}")
        print("Please check your .env file and API credentials")
        exit(1)