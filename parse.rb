require 'anystyle/parser'
require 'json/ext'

Anystyle.dictionary.options[:mode] = :redis
Anystyle.dictionary.options[:host] = 'localhost'

b = Anystyle.parse('Poe, Edgar A. Essays and Reviews. New York: Library of America, 1984.',
                   format=:citeproc)
puts b[0].to_json
