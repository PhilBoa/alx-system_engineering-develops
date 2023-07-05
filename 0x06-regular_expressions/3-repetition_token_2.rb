#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular
#+ expression matching all the following except the first line
# hbn
# hbtn
# hbttn
# hbtttn
# hbttttn

puts ARGV[0].scan(/(hbt{1,}n)/).join
