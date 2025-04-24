import os
import streamlit.web.cli as stcli
import sys

def main():
    # Run Streamlit with the app.py script, listening on the port assigned by Render
    sys.argv = [
        "streamlit",
        "run",
        "app.py",
        "--server.port",
        os.getenv("PORT", "8501"),
        "--server.address",
        "0.0.0.0"
    ]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()
