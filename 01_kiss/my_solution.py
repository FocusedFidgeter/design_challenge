import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def count_fruits(fruits: list[str]) -> dict[str, int]:
    fruit_bowl: dict[str, int] = {}
    for fruit in fruits:
        logger.info(fruit)
        if fruit in fruit_bowl:
            logger.info(f"{fruit} incremented to {fruit_bowl[fruit] + 1}")
            fruit_bowl[fruit] += 1
        else:
            logger.info(f"{fruit} set to 1")
            fruit_bowl[fruit] = 1
    return fruit_bowl


def main() -> None:
    result = count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    )
    logger.info(f"Result: {result}")
    assert result == {"apple": 4, "banana": 3, "cherry": 4}

    result = count_fruits([])
    logger.info(f"Result: {result}")
    assert result == {}

    result = count_fruits(
        [
            "apple",
            "blueberry",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    )
    logger.info(f"Result: {result}")
    assert result == {"apple": 4, "blueberry": 1, "banana": 2, "cherry": 4}


if __name__ == "__main__":
    main()
