def get_k_max(inputs,k):
    if len(inputs) < k or len(inputs) == 0:
        return inputs

    heap = inputs[:k]

    build_min_heap(heap)

    for i in range(k,len(inputs)):
        if heap[0] < inputs[i]:
            heap[0] = inputs[i]
            min_heapify(heap,k,0)

    return heap


def build_min_heap(heap):
    length = len(heap)

    for i in range(int(length/2 -1),-1,-1):
        min_heapify(heap,length,i)


def min_heapify(heap,length,root):
    min = root
    left = 2 * root + 1
    right = 2* root + 2

    if  length > left and heap[min] > heap[left] :
        min = left
    if length > right and heap[min] > heap[right]:
        min = right
    if min != root:
        heap[root],heap[min] = heap[min],heap[root]
        min_heapify(heap,len(heap),min)
    

if __name__ == "__main__":
    inputs = [16,1,2,3,1,5,4,7,8,9,22,3,54,13,11,20,12,4,5,6,25]
    k = 6
    print(get_k_max(inputs,k))