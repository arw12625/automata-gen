import DESops as d
from random import random, sample


def gen_erdos_renyi(num_states,
					trans_prob,
					num_events=None, events=None,
					num_init_states=None, init_prob=None,
					num_marked_states=None, marked_prob=None):
	"""
	Create a generator of random automata in the style of Erdős–Rényi
	Whether a transition between two given states with a given event label is included in the automaton is
	modeled by a random variable. These variables are independent with the Bernouli distribution
	with probability `trans_prob`.

	This method is guaranteed to generate automata with the given number of states, initial states, and marked states.
	if specified.

	Automata are constructed from the generator with `next` or in a `for` loop.
	>>> gen = gen_erdos_renyi(num_states=4, trans_prob=0.1, num_events=4, num_init_states=1, num_marked_states=1)
	>>> g = next(gen) # a single automaton
	>>> for g in gen: # an infinite loop generating automata
	>>>		pass

	Parameters
	----------
	num_states: int
	trans_prob: float
	num_events: int or None
	events: set or None
	num_init_states: int or None
	init_prob: float or None
	num_marked_states: int or None
	marked_prob: float or None
	"""
	if num_events is None and events is None:
		raise ValueError("Must provide either `num_events` or `events`")
	if num_events is not None and events is not None:
		raise ValueError("Cannot provide both `num_events` or `events`")
		
	if num_init_states is None and init_prob is None:
		raise ValueError("Must provide either `num_init_states` or `init_prob`")
	if num_init_states is not None and init_prob is not None:
		raise ValueError("Cannot provide both `num_init_states` or `init_prob`")
		
	if num_marked_states is None and marked_prob is None:
		raise ValueError("Must provide either `num_marked_states` or `marked_prob`")
	if num_marked_states is not None and marked_prob is not None:
		raise ValueError("Cannot provide both `num_marked_states` or `marked_prob`")
	
	if events:
		events = set(events)
	else:
		events = set(range(num_events))
	
	while True:
		edges = list(zip(*[((q, qp), e) for q in range(num_states)
										for qp in range(num_states)
										for e in events if random() < trans_prob]))
		
		if num_init_states:
			# if number of initial states is specified, they are always the lowest index states
			init = list(range(num_init_states))
		else:
			init = [s for s in range(num_states) if random() < init_prob]
		if num_marked_states:
			marked = sample(list(range(num_states)), num_marked_states)
		else:
			marked = [s for s in range(num_states) if random() < marked_prob]

		g = d.NFA()
		g.events = events
		g.add_vertices(num_states)
		g.vs['init'] = False
		g.vs.select(init)['init'] = True
		g.vs['marked'] = False
		g.vs.select(marked)['marked'] = True
		if edges:
			g.add_edges(edges[0], edges[1])
		yield g
