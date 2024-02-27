"""
This file seeks to find an example of an automaton whose shortest non-opaque string is much larger than a minimal attack
"""
from automata_gen.erdos_renyi import gen_erdos_renyi
from automata_gen.desops_gen import gen_desops
from automata_gen.filter import filter_gen

import DESops as d
from DESops.file.wmod_to_igraph import write_wmod, write_wmod_multi

def write_random_wmod(num_automata, num_states, num_events, file_prefix="output/"):
    gen = gen_erdos_renyi(
        num_states=num_states, num_events=num_events,
        marked_prob=1 - 1 / num_states, trans_prob=0.5 / num_states,
        num_init_states=1)
    print(f"Starting generation of {num_automata} automata")
    for i in range(num_automata):
        print(f"Generating #{i}")
        filename = f"{file_prefix}{i}.wmod"
        print(filename)

        g = next(gen)
        g.vs['name'] = [str(i) for i in g.vs.indices]
        event_map = {e: str(e) for e in g.events}
        _rename_events(g, event_map)
        write_wmod(filename, g)
    print("Finished generation")


def _rename_events(g, event_map):
    """
    Rename the events of an automaton according to a given dictionary or map.
    """
    g.es['label'] = [event_map.get(e['label']) for e in g.es]
    g.generate_out()
    g.events = {event_map[event] for event in g.events}

if __name__ == "__main__":
    ex = write_random_wmod(num_automata=1, num_states=8, num_events=4, file_prefix="output/ex")
    #print(ex)
