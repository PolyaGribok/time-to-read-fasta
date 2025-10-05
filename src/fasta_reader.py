"""
Модуль для работы с FASTA файлами.
"""

class Seq:
    """
    Класс для работы с биологическими последовательностями.
    """
    
    NUCLEOTIDE_ALPHABET = set('ATCGUNatcgun-')
    PROTEIN_ALPHABET = set('ACDEFGHIKLMNPQRSTVWYacdefghiklmnpqrstvwy-*')
    
    def __init__(self, header, sequence):
        self.header = header.strip()
        self.sequence = sequence.replace('\n', '').replace(' ', '').upper()
    
    def __str__(self):
        return f">{self.header}\n{self.sequence}"
    
    def __len__(self):
        return len(self.sequence)
    
    def get_alphabet(self):
        seq_chars = set(self.sequence)
        
        if seq_chars.issubset(self.NUCLEOTIDE_ALPHABET):
            return 'nucleotide'
        elif seq_chars.issubset(self.PROTEIN_ALPHABET):
            return 'protein'
        else:
            return 'unknown'
    
    def __repr__(self):
        return f"Seq(header='{self.header}', sequence='{self.sequence[:20]}...')"


class FastaReader:
    """
    Класс для чтения FASTA файлов.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def is_valid_fasta(self):
        """
        Проверяет базовое соответствие файла формату FASTA.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline().strip()
                return bool(first_line) and first_line.startswith('>')
        except Exception:
            return False
    
    def read_sequences(self):
        """
        Генератор, который читает файл и возвращает последовательности.
        """
        current_header = None
        current_sequence = []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    
                    if not line:
                        continue
                    
                    if line.startswith('>'):
                        if current_header is not None:
                            yield Seq(current_header, ''.join(current_sequence))
                        
                        current_header = line[1:]
                        current_sequence = []
                    
                    else:
                        current_sequence.append(line)
                
                if current_header is not None:
                    yield Seq(current_header, ''.join(current_sequence))
            
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            raise