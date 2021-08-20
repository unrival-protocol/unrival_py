def get_interpretations(universe_parts, namespace_parts, addresses=False):
    """
    Return a list of possible interpretations for a given namespace within a given universe

    Args:
      universe_parts (list): parts of universe in which namespace can be interpreted
      namespace_parts (list): parts of namespace from which interpretations can be made
      addresses (bool): return addresses if set to true
    Returns:
      list: addresses
    """
    raise NotImplementedError
