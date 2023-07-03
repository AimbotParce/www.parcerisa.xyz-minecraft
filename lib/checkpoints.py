from .sql import sql


get_query = "SELECT id, name, coords, date_added FROM checkpoints;"


def get_world_checkpoints():
    checkpoints = sql(get_query)

    checkpoints.sort(key=lambda x: x[3], reverse=True)  # Sort by date added

    return checkpoints
