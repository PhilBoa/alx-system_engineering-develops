#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular
#+ expression matching the first and second lines of the following
# htn
# hbtn
# hbbtn
# hbbbtn

puts ARGV[0].scan(/(hb?tn)/).join
