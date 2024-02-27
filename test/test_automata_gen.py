from automata_gen.erdos_renyi import gen_erdos_renyi
from automata_gen.desops_gen import gen_desops
from automata_gen.filter import filter_gen

from DESops.basic_operations.unary import find_non_trim


def test_gen_erdos_renyi():
	# Generation settings
	num_states = 10
	num_events = 5
	marked_prob = 0.5
	trans_prob = 0.5
	num_init_states = 1

	# Create the generator
	gen = gen_erdos_renyi(
		num_states=num_states,
		num_events=num_events,
		marked_prob=marked_prob,
		trans_prob=trans_prob,
		num_init_states=num_init_states
	)

	# Generate one automaton
	g = next(gen)

	# Check automata matches setting
	assert g.vcount() == num_states
	assert len(g.events) == num_events
	assert len(g.vs.select(init=True)) == num_init_states


def test_filter_gen():
	# Generation settings
	num_states = 10
	num_events = 5
	marked_prob = 0.1
	trans_prob = 0.5
	num_init_states = 1

	# Create the generator
	gen = gen_erdos_renyi(
		num_states=num_states,
		num_events=num_events,
		marked_prob=marked_prob,
		trans_prob=trans_prob,
		num_init_states=num_init_states
	)

	# Filter the generator to ensure automata are trim and both the generated and marked languages are nonempty
	fgen = filter_gen(gen, accessible=True, coaccessible=True, ensure_nonempty_init=True, ensure_nonempty_marked=True)
	g = next(fgen)

	# Check automata matches setting
	assert g.vcount() == num_states
	assert len(g.events) == num_events
	assert len(g.vs.select(marked=True)) != 0
	assert not find_non_trim(g)


def test_gen_desops():
	# Generation settings
	num_states = 10
	num_events = 5
	num_init_states = 1
	num_marked_states = 2
	deterministic = True

	# Create the generator
	gen = gen_desops(
		num_states=num_states,
		num_events=num_events,
		num_init_states=num_init_states,
		num_marked_states=num_marked_states,
		deterministic=deterministic,
		min_trans_per_state=1,
		max_trans_per_state=4,
		enforce_max_trans_per_state=True
	)

	# Generate one automaton
	g = next(gen)

	# Check automata matches setting
	assert g.vcount() == num_states
	assert len(g.events) == num_events
	assert len(g.vs.select(init=True)) == num_init_states
	assert len(g.vs.select(marked=True)) == num_marked_states
