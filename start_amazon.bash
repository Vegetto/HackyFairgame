#!/bin/bash

screen -d -m bash -c "pipenv shell; python app.py amazon --no-image --checkshipping --focus-group 21"
screen -d -m bash -c "pipenv shell; python app.py amazon --no-image --checkshipping --focus-group 22"
#for GROUP in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
#for GROUP in 0 1 2 3 4 5 6 7 8 9
#do
	#screen -d -m bash -c "pipenv shell; python app.py amazon --no-image --checkshipping --focus-group ${GROUP}"
	#sleep 10
#done
#python app.py amazon --no-image --checkshipping
