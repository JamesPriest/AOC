
def addr(register, register_index_1, register_index_2, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] + register_copy[register_index_2]
    register_copy[store_index] = val
    return register_copy

def addi(register, register_index_1, value, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] + value 
    register_copy[store_index] = val
    return register_copy


def mulr(register, register_index_1, register_index_2, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] * register_copy[register_index_2]
    register_copy[store_index] = val
    return register_copy

def muli(register, register_index_1, value, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] * value 
    register_copy[store_index] = val
    return register_copy


def banr(register, register_index_1, register_index_2, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] & register_copy[register_index_2]
    register_copy[store_index] = val
    return register_copy

def bani(register, register_index_1, value, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] & value 
    register_copy[store_index] = val
    return register_copy


def borr(register, register_index_1, register_index_2, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] | register_copy[register_index_2]
    register_copy[store_index] = val
    return register_copy

def bori(register, register_index_1, value, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1] | value 
    register_copy[store_index] = val
    return register_copy



def setr(register, register_index_1, register_index_2, store_index):
    register_copy = list(register)
    val = register_copy[register_index_1]
    register_copy[store_index] = val
    return register_copy

def seti(register, register_index_1, value, store_index):
    register_copy = list(register)
    val = register_index_1
    register_copy[store_index] = val
    return register_copy

def gtir(register, A, B, C):
    register_copy = list(register)
    val = (A > register[B])*1 
    register_copy[C] = val
    return register_copy

def gtri(register, A, B, C):
    register_copy = list(register)
    val = (register[A] > B)*1
    register_copy[C] = val
    return register_copy

def gtrr(register, A, B, C):
    register_copy = list(register)
    val = (register[A] > register[B])*1
    register_copy[C] = val
    return register_copy


def eqir(register, A, B, C):
    register_copy = list(register)
    val = (A == register[B])*1
    register_copy[C] = val
    return register_copy

def eqri(register, A, B, C):
    register_copy = list(register)
    val = (register[A] == B)*1
    register_copy[C] = val
    return register_copy

def eqrr(register, A, B, C):
    register_copy = list(register)
    val = (register[A] == register[B])*1
    register_copy[C] = val
    return register_copy



