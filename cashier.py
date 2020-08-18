def main():
	# write code here
	list=[]
	name=""
	while name!="done":
		name=input("Item (enter done when finished):")
		if name =="done":
			break
		else:
			price=input("Price:")
			quantity=input("Quantity:")
			#list=[]
			d={"quantity":quantity,"name":name ,"price":price }
			list.append(d)
		#dictionary_copy = d.copy()
		#list.append(dictionary_copy)

	#print(list)
	#print(list[])
	#-------------------
	print ("-------------------")
	print("receipt")
	print ("-------------------")
	p=0
	for i in list:
		#j=1
		#for j in i:
			#print(j)
			#if j==0:
		p=p+int(i["quantity"])*int(i["price"])
		p1=int(int (i["quantity"])*int(i["price"]))
		print(i["quantity"]+". "+i["name"]+"  "+str(p1)+"KD" )

		#	else:
		#		break
	print ("-------------------")
	print ("Total Price:"+str(p)+"KD")
		#print(q , name , q*price)
		#print(ii)
		#print(i)
	#for key,values in list.items():
	#	for v in values:
		#	print(key," : ",v)
		#for k in dictionary:
    #print("key: %s" % k)
    #print("value: %s" % dictionary[k])

		#pass

if __name__ == '__main__':
	main()
