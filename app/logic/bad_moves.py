

class BadMoves(object):

    def bad_move(self, move, gs):
        if move is None:
            return True
        coord = gs.me.head + move
        if gs.me.neck == coord:
            return True
        if gs.me.coords[-2] == coord:
            return True
        if not gs.is_empty(coord) and coord not in gs.all_tails:
            return True
        if coord in gs.possible_death_coords:
            return True
        return False

