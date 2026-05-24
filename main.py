from analyzer.text_analyzer import (
    count_words,
    count_characters,
    count_sentences,
    count_paragraphs,
    longest_word,
    longest_sentences,
    longest_paragraphs
    
)

text = "Hola mundo, esta es una fase de prueba escrita directamente en el codigo."

print(f"Palabras:", count_words(text))
print(f"Caracteres:", count_characters(text))
print(f"Oraciones:", count_sentences(text))
print(f"Parrafos:", count_paragraphs(text))
print(f"Palabras mas larga:", longest_word(text))
print(f"Oracion mas larga:", longest_sentences(text))
print(f"Parrafo mas largo:", longest_paragraphs(text))