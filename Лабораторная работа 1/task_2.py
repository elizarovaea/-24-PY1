total_symbols = 100*50*25
bytes_for_one_book = total_symbols*4
bytes_disc = 1.44*1024**2

print("Количество книг, помещающихся на дискету:", int(bytes_disc//bytes_for_one_book))
