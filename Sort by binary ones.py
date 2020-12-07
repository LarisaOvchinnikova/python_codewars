https://www.codewars.com/kata/59eb28fb0a2bffafbb0000d6
def sort_by_binary_ones (num_list):
    num_list = sorted(num_list)
    return sorted(num_list, key=lambda el: bin(el).count('1'), reverse=True)