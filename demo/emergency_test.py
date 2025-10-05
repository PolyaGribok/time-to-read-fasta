"""
Экстренное тестирование - проверяем работу без валидации формата
"""
import sys
import os

# Добавляем папку src в путь Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from fasta_reader import FastaReader

def emergency_test():
    print("🚀 ЭКСТРЕННОЕ ТЕСТИРОВАНИЕ")
    print("=" * 50)
    
    # Тестовые файлы
    test_files = [
        "simple_test.fasta",    # Простой тестовый файл
        "test_insulin.fasta"    # Твой оригинальный файл
    ]
    
    for file_name in test_files:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        
        print(f"\n🎯 Тестируем файл: {file_name}")
        print(f"📁 Полный путь: {file_path}")
        print(f"📊 Файл существует: {os.path.exists(file_path)}")
        
        if not os.path.exists(file_path):
            print("❌ Файл не найден, пропускаем...")
            continue
        
        try:
            reader = FastaReader(file_path)
            
            # Пробуем прочитать последовательности
            sequences = list(reader.read_sequences())
            
            print(f"✅ УСПЕХ! Прочитано последовательностей: {len(sequences)}")
            
            # Показываем информацию о каждой последовательности
            for i, seq in enumerate(sequences, 1):
                print(f"   {i}. {seq.header}")
                print(f"      Длина: {len(seq)}")
                print(f"      Тип: {seq.get_alphabet()}")
                print(f"      Начало: {seq.sequence[:20]}...")
                
        except Exception as e:
            print(f"❌ ОШИБКА: {e}")

if __name__ == "__main__":
    emergency_test()