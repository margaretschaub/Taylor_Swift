pip install inflect
import inflect

p = inflect.engine()
p.number_to_words(99)