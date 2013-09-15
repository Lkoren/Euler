sum_square = (1..100).inject() {|sum, n| sum += n*n}
square_sum = (1..100).inject() {|sum, n| sum += n}
square_sum = square_sum * square_sum

puts "sum squared: #{sum_square}, squared sum: #{square_sum}, difference: #{square_sum - sum_square}"

#Gauss may have discovered sum of geometric series shortcut as a child: 1..100 = (101 * 50). 
#There's also a formula for the sum of squares. 