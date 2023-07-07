#!/usr/bin/env ruby
# A Ruby script that accepts data from TextMe app text messages
#+ transactions log file and passes it to a regular expression
#+ matching method and show this output:
# [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
