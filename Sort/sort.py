import time

class sort:
    def __init__(self,lst):
        self.lst=lst

    def bubble_sort(self,count):
        if count==len(self.lst):
            print("Bubble sort:")
            print(self.lst)
            return
        for i in range(len(self.lst)-1):
            if self.lst[i]>self.lst[i+1]:
                temp=self.lst[i]
                self.lst[i]=self.lst[i+1]
                self.lst[i+1]=temp
        count+=1
        self.bubble_sort(count)

    def Hoare_sort(self,pivot):
        start=pivot+1
        end=len(self.lst)-1
        i=0
        j=0
        while i in range(len(self.lst)):
            if pivot==end:
                return True
            if start + i >end - j:
                temp = self.lst[pivot]
                self.lst[pivot] = self.lst[end - j]
                self.lst[end - j] = temp
                if self.Hoare_sort(pivot):
                    return True

            if self.lst[start+i]>self.lst[pivot]:
                while j in range(len(self.lst)):
                    if start + i > end - j and end - j != pivot:
                        temp = self.lst[pivot]
                        self.lst[pivot] = self.lst[end - j]
                        self.lst[end - j] = temp
                        if self.Hoare_sort(pivot):
                            return True
                    if end-j==pivot:
                        pivot+=1
                        if self.Hoare_sort(pivot):
                            return True
                    if self.lst[end-j]<self.lst[pivot]:
                        temp=self.lst[start+i]
                        self.lst[start+i]=self.lst[end-j]
                        self.lst[end-j]=temp
                        break
                    j += 1
            i+=1
        return True

    def Lomuto_sort(self,pivot):
        p_index=0
        while p_index in range(len(self.lst)):
            if pivot==0:
                return True
            if self.lst[p_index]>self.lst[pivot]:
                i_index=p_index+1
                while i_index in range(len(self.lst)):
                    if self.lst[i_index]<=self.lst[pivot]:
                        temp=self.lst[p_index]
                        self.lst[p_index]=self.lst[i_index]
                        self.lst[i_index]=temp
                        break
                    i_index+=1
            if p_index==pivot and pivot!=0:
                pivot-=1
                if self.Lomuto_sort(pivot):
                    return
            p_index+=1

    def insertion_sort(self,key):
        for i in range(key,-1,-1):
            if self.lst[i]>self.lst[key]:
                temp=self.lst[key]
                self.lst[key]=self.lst[i]
                self.lst[i]=temp
                key-=1
                self.insertion_sort(key)
        if key==len(self.lst)-1:
            return
        key += 1
        self.insertion_sort(key)

    def selection_sort(self,min,count):
        for i in range(count,len(self.lst)):
            if self.lst[min]>self.lst[i]:
                temp=self.lst[min]
                self.lst[min]=self.lst[i]
                self.lst[i]=temp
        min+=1
        count+=1
        if count==len(self.lst):
            print("Selection_sort:")
            print(self.lst)
            return
        self.selection_sort(min,count)

    def shell_sort(self,div,comp=0):
        mid=len(self.lst)//div
        mid_1=mid
        while mid_1 in range(len(self.lst)):
            if self.lst[comp]>self.lst[mid_1]:
                temp = self.lst[comp]
                self.lst[comp] = self.lst[mid_1]
                self.lst[mid_1] = temp
            comp+=1
            mid_1+=1
        if mid==1:
            print("Shell sort:")
            print(self.lst)
            return
        div=div*2
        self.shell_sort(div)




lst_sort=sort([10,28,30,29,15,9,50,83])
lst_sort.bubble_sort(0)
lst_sort.Hoare_sort(0)
print("Hoare scheme:")
print(lst_sort.lst)
lst_sort.Lomuto_sort(len(lst_sort.lst)-1)
print("Lomuto scheme:")
print(lst_sort.lst)
print("Insertion sort:")
lst_sort.insertion_sort(1)
print(lst_sort.lst)
lst_sort.selection_sort(0,0)
lst_sort.shell_sort(2)