#!/bin/bash
screen -d -m bash -c "pipenv shell; python app.py bestbuy --sku 6438942"
screen -d -m bash -c "pipenv shell; python app.py bestbuy --sku 6440913"
screen -d -m bash -c "pipenv shell; python app.py bestbuy --sku 6442585"
screen -d -m bash -c "pipenv shell; python app.py bestbuy --sku 6441226"
