
def rename_events(g, event_map):
    """
    Rename the events of an automaton according to a given dictionary or map.
    """
    g.es['label'] = [event_map.get(e['label']) for e in g.es]
    g.generate_out()
    g.events = {event_map[event] for event in g.events}