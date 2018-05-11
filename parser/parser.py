#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Parser:

    def load(self, file):
        """
        Loads instance from .psa file, returns array containing the following:
        - distance matrix
        - array of time window constraints
        """
        def _map_fn(func, xs):
            return list(map(lambda x: list(map(func, x)), xs))

        data = []

        with open(file) as fd:
            problem = fd.read().split('\n')

            num_locations = int(problem[0])

            data.append(_map_fn(float, map(
                lambda x: x.split(), problem[1:num_locations+1])))

            data.append(_map_fn(int, map(lambda x: x.split(),
                                         problem[num_locations+1:num_locations*2+1])))

            # TODO - Append capacity constraints

        return data
