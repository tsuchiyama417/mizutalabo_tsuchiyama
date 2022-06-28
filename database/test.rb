require 'csv'

vec = Array.new
num = Array.new
hash = Hash.new(0)
cnt = 0
CSV.foreach("aaindex_corr.csv") do |row|
    if cnt == 0 then
        row[1..].each do |s|
            num << s
        end
    else
        key = row[0]
        row[1..].each_with_index do |val, index|
            hash[[key, num[index+1]]] = val.to_f
        end
    end
    cnt += 1
end
num.combination(3).each do |vec|
    sum = 0
    vec.each do |elm|
        print "#{elm} "
    end
    print ":"
    #p vec
    vec.combination(2).each do |pvec|
        sum += hash[pvec].abs
    end
    p sum
end