#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular
#+ expression matching all the following except the second line
# hbn
# hbon
# hbtn
# hbttn
# hbtttn
# hbttttn

puts ARGV[0].scan(/\bh(?!bon)\w+\b/).join
