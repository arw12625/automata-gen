import DESops as d
from DESops.random_automata import generate


def gen_desops(num_states,
               num_events=None, events=None,
               min_trans_per_state=0, max_trans_per_state=None,  # if None, is set to num_events
               deterministic=True,
               num_init_states=1, num_marked_states=0,
               enforce_accesibility=True, enforce_max_trans_per_state=True,
               prob_self_loop=1):
    """
    Generate automata using the method implemented by M-DESops.

    Parameters
    ----------
    num_states: int
    num_events: int or None
    events: set or None
    min_trans_per_state: int
    max_trans_per_state: int
    deterministic: bool
    num_init_states: int
    num_marked_states: int
    enforce_accesibility: bool
    enforce_max_trans_per_state: bool
    prob_self_loop: float
    """
    if num_events is None and events is None:
        raise ValueError("Must provide either `num_events` or `events`")
    if num_events is not None and events is not None:
        raise ValueError("Cannot provide both `num_events` or `events`")

    event_map = None
    if events:
        event_map = {i: e for i, e in enumerate(events)}

    while True:
        g = generate(
                num_states=num_states,
                num_events=num_events,
                min_trans_per_state=min_trans_per_state, max_trans_per_state=max_trans_per_state,
                det=deterministic,
                num_init=num_init_states, num_marked=num_marked_states,
                enforce_accesibility=enforce_accesibility, enforce_max_trans_per_state=enforce_max_trans_per_state,
                prob_self_loop=prob_self_loop
        )

        if events:
            _rename_events(g, event_map)
        yield g


def _rename_events(g, event_map):
    """
    Rename the events of an automaton according to a given dictionary or map.
    """
    g.es['label'] = [event_map.get(e['label']) for e in g.es]
    g.generate_out()
    g.events = {event_map[event] for event in g.events}