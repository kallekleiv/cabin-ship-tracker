import asyncio
import sys
from ais_connection import connect_to_ais_stream
import logging


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stderr)],
    )
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Starting script...")

    asyncio.run(connect_to_ais_stream())


if __name__ == "__main__":
    main()
