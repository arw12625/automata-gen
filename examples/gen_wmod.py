"""
This file seeks to find an example of an automaton whose shortest non-opaque string is much larger than a minimal attack
"""
from automata_gen.erdos_renyi import gen_erdos_renyi
from automata_gen.desops_gen import gen_desops
from automata_gen.filter import filter_gen
from automata_gen.util import rename_events

import DESops as d
from DESops.file.wmod_to_igraph import write_wmod, write_wmod_multi

import os
from pathlib import Path


def write_random_wmod(num_automata, num_states,
                      num_events=None, events=None, events_uc=None,
                      output_directory="output", filename_prefix=""):
    if events_uc is None:
        events_uc = set()
    if events:
        if events_uc and not events_uc.issubset(events):
            raise ValueError("Uncontrollable events must be a subset of the event set.")

    Path(output_directory).mkdir(parents=True, exist_ok=True)  # Ensure output directory exists

    # Use these lines for simple generation method
    # gen = gen_erdos_renyi(
    #     num_states=num_states, num_events=num_events, events=events,
    #     marked_prob=1 - 1 / num_states, trans_prob=0.5 / num_states,
    #     num_init_states=1)

    # Use these lines for complex generation method
    gen = gen_desops(num_states=num_states, num_events=num_events, events=events)

    # You can use this line in combination with one of the above generators
    # to ensure automata are accessible/coaccessible and that they have nonempty initial/marked state sets
    # This may change the number of states in the automata
    gen = filter_gen(gen, accessible=True, coaccessible=True, ensure_nonempty_init=True, ensure_nonempty_marked=True)

    print(f"Starting generation of {num_automata} automata")
    for i in range(num_automata):
        filename = os.path.join(output_directory, f"{filename_prefix}{i}.wmod")
        print(f"Generating automaton #{i}. Writing to '{str(filename)}'")

        g = next(gen)  # generate an automaton
        g.vs['name'] = [str(i) for i in g.vs.indices]  # ensure state names are strings
        event_map = {e: str(e) for e in g.events}
        rename_events(g, event_map)  # ensure event names are strings
        g.Euc = {str(e) for e in events_uc}  # set uncontrollable events

        write_wmod(filename, g)

    print("Finished generation")


# This is the code that is executed when the file is run
if __name__ == "__main__":
    write_random_wmod(num_automata=1, num_states=8,
                      events={'a', 'b', 'c'}, events_uc={'a'},
                      output_directory="output", filename_prefix="ex")
