"""
Демонстрационная программа для работы с FASTA файлами
"""
import sys
import os
import time

# Добавляем папку src в путь Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from fasta_reader import FastaReader

def demonstrate_fasta_reader(file_path):
    """Демонстрация работы с FASTA файлом"""
    print(f"\n=== Обработка файла: {os.path.basename(file_path)} ===")
    
    try:
        reader = FastaReader(file_path)
        
        # Проверка формата
        is_valid = reader.is_valid_fasta()
        print(f"✅ Файл соответствует формату FASTA: {is_valid}")
        
        if not is_valid:
            print("❌ Файл невалидный, пропускаем...")
            return
        
        # Чтение последовательностей
        sequence_count = 0
        total_length = 0
        
        print("\n📊 Последовательности в файле:")
        print("-" * 50)
        
        start_time = time.time()
        
        for seq in reader.read_sequences():
            sequence_count += 1
            total_length += len(seq)
            
            print(f"🎯 {sequence_count}. {seq.header}")
            print(f"   📏 Длина: {len(seq)} символов")
            print(f"   🔤 Тип: {seq.get_alphabet()}")
            print(f"   👀 Префикс: {seq.sequence[:30]}...")
            print()
        
        end_time = time.time()
        
        # Статистика
        print("=" * 50)
        print(f"📈 СТАТИСТИКА:")
        print(f"   Всего последовательностей: {sequence_count}")
        print(f"   Общая длина: {total_length} символов")
        print(f"   Время обработки: {end_time - start_time:.2f} секунд")
        if sequence_count > 0:
            print(f"   Средняя длина: {total_length/sequence_count:.1f} символов")
        
    except Exception as e:
        print(f"❌ Ошибка при обработке файла: {e}")

def main():
    """Основная функция демонстрации"""
    print("🔬 ДЕМОНСТРАЦИЯ FASTA READER")
    print("=" * 60)
    
    # Тестовые файлы (относительные пути от папки demo)
    test_files = [
        "test_insulin.fasta"    # Наш новый файл с инсулином
    ]
    
    for file_name in test_files:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        
        if os.path.exists(file_path):
            demonstrate_fasta_reader(file_path)
        else:
            print(f"⚠️  Файл {file_name} не найден")

if __name__ == "__main__":
    main()