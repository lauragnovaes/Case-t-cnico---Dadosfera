import csv

# Função para dividir o csv em pedaços aceitos pelo chatgpt
def create_chat_files(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        # Pula o header
        header = next(csv_reader, None)
        entries = 10 # quantidade de linhas selecionadas

        for i, row in enumerate(csv_reader):
            with open(f'chat_archive_{(i+1)//entries}.txt', 'a+') as chat_file:
                # Escreve as linhas no novo arquivo
                chat_file.write(', '.join(row))
                chat_file.write('\n')
            if i // entries > 100:
                break


csv_filename = 'product-search-corpus.csv'  # arquivo original

create_chat_files(csv_filename)