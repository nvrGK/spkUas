from Language_detection import detect

all_language_codes = {
    "id": "Indonesia",
    "eng": "England",
    "spa": "Spannyol",
    "kn": "Kanada",
    "jpn": "Japanese",
    "RRC": "Republik Rakyat China"
}

input_Sintence = {
    "Saya sedang memakan nasi pecel",
    "I'm eating pecel rice ",
    "Estoy comiendo arroz pecel",
    "ನಾನು ಪೆಸೆಲ್ ರೈಸ್ ತಿನ್ನುತ್ತಿದ್ದೇನೆ",
    "ピーセルライスを食べています",
    "我在吃pecel飯"

}
lemmatizer_names = ["language_codes", "input_Sintence"]
format_text = '{:24}' * (len(lemmatizer_names)+1)
print('\n', format_text.format("Language Name", *lemmatizer_names), '\n', '='*6)
for data in input_Sintence:
    language_code = detect(data)
    sentence = [all_language_codes.get(language_code), language_code, data]
    print(format_text.format(*sentence))
