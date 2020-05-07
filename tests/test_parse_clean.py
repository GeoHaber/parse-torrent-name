#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

import PTN

if __name__ == '__main__':

    Expecto = [ 'title', 'year', 'season', 'episode' , 'codec', 'audio', 'resolution' ]

    json_input = os.path.join(os.path.dirname(__file__), 'files/input.json')
    with open(json_input) as input_file:
        torrents = json.load(input_file)

    for torrent in torrents :
        message = ''
        result = PTN.parse( torrent )
#        print ( Expecto )
        print ( f"\n{result}" )
        for keyval in Expecto :
#            print (keyval)
            if keyval not in result.keys() :
#               print (f"\n {keyval} ! Not found")
                continue
            else :
                if keyval == 'season' :
                    message += f" S{result[keyval]:02d}"
                elif keyval == 'episode' :
                    message += f"E{result[keyval]:02d} "
                elif keyval == 'year' :
                    message += f"({result[keyval]}) "
                elif keyval == 'resolution' :
                    message += f"[{result[keyval]}] "
                else:
                    message += f"{result[keyval]} "
        print (message)

    input(' qwqwqwq ')
