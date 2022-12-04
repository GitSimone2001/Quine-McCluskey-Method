import random as rand

# One_set can contain numbers from 0 to 15 (4-bit representation)
one_set = (0, 1, 2, 3, 5, 7, 11, 15)

# Generate Minterms
b_one_set = ['{0:04b}'.format(num) for num in one_set]
print('Starting one-set in Binary: ', b_one_set)
N = []


def generate_products(size, set):
    products = []
    for a in set:
        for b in set:
            literals = ''
            if ('-' * (3 - size)) in a and ('-' * (3 - size)) in b:
                pass
            else:
                continue
            if a.index('-' * (3 - size)) != b.index('-' * (3 - size)):
                continue
            for digit in range(len(a)):
                if a[digit] == b[digit]:
                    literals += a[digit]
                else:
                    literals += '-'
            if literals.count('-') == (4 - size):
                products.append(literals)
                N.append(a)
                N.append(b)
    return products


# Generate 3-Literal Products
three_literal_products = list(dict.fromkeys(generate_products(3, b_one_set)))
print('3-Literal Products: ', three_literal_products)

# Generate 2-Literal Products
two_literal_products = list(dict.fromkeys(generate_products(2, three_literal_products)))
print('2-Literal Products: ', two_literal_products)

# Generate 1-Literal Products
one_literal_products = list(dict.fromkeys(generate_products(1, two_literal_products)))
print('1-Literal Products: ', one_literal_products)

N = list(dict.fromkeys(N))
L = b_one_set + three_literal_products + two_literal_products + one_literal_products
prime_implicants = list(set(L).difference(N))
print('Prime Implicants: ', prime_implicants)
print('Non-Prime Implicants: ', N)

# Find Essential Prime Implicants
essential_prime_implicants = []
for num in b_one_set:
    covers = []
    for prime in prime_implicants:
        y = 0
        for i in range(0, len(prime)):
            if prime[i] == '-':
                y += 1
            elif prime[i] == num[i]:
                y += 1
        if y == 4:
            covers.append(prime)
    if len(covers) == 1:
        essential_prime_implicants.append(covers[0])
print('Essential Prime Implicants: ', essential_prime_implicants)

not_covered = []
for num in b_one_set:
    values = []
    for eprime in essential_prime_implicants:
        count = 0
        for i in range(4):
            if num[i] == eprime[i] or eprime[i] == '-':
                count += 1
        values.append(count)
    if max(values) < 4:
        not_covered.append(num)
print('Not Covered by EPIs: ', not_covered)

product_of_sums = [' + '.join(essential_prime_implicants)]
for num in not_covered:
    covers = []
    for prime in prime_implicants:
        count = 0
        for i in range(4):
            if num[i] == prime[i] or prime[i] == '-':
                count += 1
        if count == 4:
            covers.append(prime)
    cover = covers[rand.randint(0, 1)]
    product_of_sums.append(cover)

print(' + '.join(product_of_sums))








