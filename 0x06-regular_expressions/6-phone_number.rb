#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular
#+ expression  exactly matching a 10 digit phone number

puts ARGV[0].scan(/\b^\s*(\d{10})\s*\b/).join
