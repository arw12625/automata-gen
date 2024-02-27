import DESops as d

from DESops.basic_operations.unary import construct_acc, construct_coac, construct_trim


def filter_gen(gen, accessible=True, coaccessible=True,
               ensure_nonempty_init=True, ensure_nonempty_marked=True):
    """
    This method creates a new generator from an existing one by performing accessbility computations on
    and filtering out empty automata as specified.

    If `accessible` or `coaccessible` are set to `True`, this method can alter the number of states
    in the automata produced by the original generator `gen`.

    Parameters
    ----------
    gen: Generator
    accessible: bool
    coaccessible: bool
    ensure_nonempty_init: bool
    ensure_nonempty_marked: bool
    """
    while True:
        g = next(gen)

        if accessible and coaccessible:
            g = construct_trim(g, inplace=True)
        elif accessible:
            g = construct_acc(g, inplace=True)
        elif coaccessible:
            g = construct_coac(g, inplace=True)

        if ensure_nonempty_init and len(g.vs.select(init=True)) == 0:
            continue
        if ensure_nonempty_marked and len(g.vs.select(marked=True)) == 0:
            continue

        yield g
