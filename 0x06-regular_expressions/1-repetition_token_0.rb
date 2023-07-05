#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular
#+ expression matching the following
# hbn
# hbtn
# hbttn   (1)
# hbtttn   (2)
# hbttttn   (3)
# hbtttttn   (4)
# hbttttttn   (5)
# hbtttttttn

puts ARGV[0].scan(/\bhbt{2,5}n\b/).join
