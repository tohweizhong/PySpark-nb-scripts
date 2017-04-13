# combineByKey
x = sc.parallelize([('B',1),('B',2),('A',3),('A',4),('A',5)])

createCombiner = (lambda el: [(el,el**2)]) 

mergeVal = (lambda aggregated, el: aggregated + [(el,el**2)]) # append to aggregated

mergeComb = (lambda agg1,agg2: agg1 + agg2 )  # append agg1 with agg2

y = x.combineByKey(createCombiner,mergeVal,mergeComb)

print(x.collect())

print(y.collect())


# create k-v pair, with v being a list of values
x = sc.parallelize([('B',1),('B',2),('A',3),('A',4),('A',5)])
createCombiner = (lambda el: [(el)])
mergeVal = (lambda aggregated, el: aggregated + [(el)])
mergeComb = (lambda agg1,agg2: agg1 + agg2 )  # append agg1 with agg2
y = x.combineByKey(createCombiner,mergeVal,mergeComb)
print(x.collect())
print(y.collect())

# (a_imsi, [b_imsi, count])
x = sc.parallelize([('B',['A',1]),('B',['C',2]),('A',['C',3]),('A',['B',4]),('A',['D',5])])
#xprime = x.map(lambda r: [(r[0], (r[1], r[2]))])



zeroVal = []
mergeVal = (lambda aggregated, el: aggregated + [(el)])
mergeComb = (lambda agg1,agg2: agg1 + agg2 )  # append agg1 with agg2
y = xprime.aggregateByKey(createCombiner,mergeVal,mergeComb)
print(xprime.collect())
print(y.collect())

