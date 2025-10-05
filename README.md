# FASTA Reader 🧬

Python библиотека для чтения и анализа FASTA файлов с биологическими последовательностями.

## 📋 О проекте

Этот проект реализует два класса для работы с FASTA файлами:
- **Seq** - для работы с отдельными последовательностями
- **FastaReader** - для чтения и валидации FASTA файлов

## ✨ Возможности

- 📁 Чтение FASTA файлов любого размера
- 🧬 Автоматическое определение типа последовательности (нуклеотид/белок)
- ⚡ Поддержка больших файлов через генераторы
- ✅ Валидация формата FASTA
- 📚 Полная документация в HTML формате
- 🧪 Автоматические тесты

## 🏗️ Структура проекта
fasta_project/
├── src/fasta_reader.py # Основные классы Seq и FastaReader
├── demo/demo.py # Демонстрационная программа
├── tests/test_fasta.py # Тесты
├── docs/ # Документация (Sphinx)
├── uml_diagram.png # UML диаграмма классов
└── INSTRUCTIONS.md # Инструкция по установке

## 🚀 Быстрый старт

### Установка
```bash
git clone https://github.com/PolyaGribok/fasta-reader.git
cd fasta-reader

## 🎬 Запуск демо-программы
cd demo
python demo.py

##✅ Запуск тестов
cd tests
python test_fasta.py

##📖 Просмотр документации
cd docs/build/html
start index.html  # 🪟 Windows
