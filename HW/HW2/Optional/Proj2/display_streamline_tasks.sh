#!/bin/bash


grep 'Name:' /var/log/syslog | sed 's/.*Name: \(.*\)/Name: \1/'

