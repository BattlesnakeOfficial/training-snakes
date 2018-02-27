from utils.vector import directions


class IncreaseBoardControl(object):

    def increase_board_control(self, gs):
        my_board_control = []
        for d in directions:
            coord = gs.me.head + d
            if not gs.is_safe(coord):
                continue
            next_gs = gs.next_gamestate([(gs.me.id, d)])
            board_control = self.board_control(next_gs)
            my_control = board_control.get(gs.me.id)
            my_board_control.append((my_control, d))
        my_board_control.sort(reverse=False)
        print ", ".join("%s:%s" % (d.direction(), c) for c,d in my_board_control)

        if len(my_board_control) == 0:
            return

        return my_board_control[1][1]

        # if any of those states has a boarder disappear by the time I get to it, it's infinitely good.
        ## unless... another snake's head is in there as well.

    def board_control(self, gs):
        snake_ids = [s.id for s in gs.all_snakes]

        per_snake_travel_times = {}
        for snake in gs.all_snakes:
            per_snake_travel_times[snake.id] = gs.travel_times(snake.head)

        def get_travel_times_to_square(coord):
            travel_times = []
            for snake_id in snake_ids:
                travel_time = per_snake_travel_times[snake_id].get(coord)
                travel_times.append((travel_time, snake_id))
            travel_times.sort()
            return travel_times

        all_keys = set()
        for snake_id in snake_ids:
            all_keys = set(per_snake_travel_times[snake_id].keys())

        control_count = {}
        for key in all_keys:
            time_to_square = get_travel_times_to_square(key)
            if len(time_to_square) == 0:
                continue
            if len(time_to_square) == 1:
                _, snake_id = time_to_square[0]
                control_count[snake_id] = control_count.get(snake_id, 0) + 1
                continue
            time_1, snake_1_id = time_to_square[0]
            time_2, snake_2_id = time_to_square[1]
            if time_1 == time_2:
                continue
            control_count[snake_1_id] = control_count.get(snake_1_id, 0) + 1

        return control_count
