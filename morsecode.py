# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input: str):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    upper_input = user_input.upper()
    result = True if upper_input == "H" or upper_input == "HELP" else False

    return result
    # ==================================


def is_validated_english_sentence(user_input: str):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
          3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_english_sentence("Hello 123")
        False
        >>> mc.is_validated_english_sentence("Hi!")
        True
        >>> mc.is_validated_english_sentence(".!.")
        False
        >>> mc.is_validated_english_sentence("!.!")
        False
        >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    for c in user_input:
        if c.isdigit():
            return False
        for tuk in "_@#$%^&*()-+=[]{}\"';:\|`~":
            if c == tuk:
                return False
    out_tuk_input = user_input.replace("?","").replace("!","").replace(".","").replace(",","")
    if out_tuk_input.replace(" ","") == "":
        return False
    return True
    # ==================================


def is_validated_morse_code(user_input: str):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_morse_code("..")
        True
        >>> mc.is_validated_morse_code("..-")
        True
        >>> mc.is_validated_morse_code("..-..")
        False
        >>> mc.is_validated_morse_code(". . . .")
        True
        >>> mc.is_validated_morse_code("-- -- -- --")
        True
        >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    for c in user_input:
        if c != "-" and c != "." and c != " ":
            return False

    char_to_morse_dict = get_morse_code_dict()
    morse_to_char_dict = dict()
    for c, m in char_to_morse_dict.items():
        morse_to_char_dict[m] = c

    user_morses_l = user_input.split(" ")

    for user_morse in user_morses_l:
        if user_morse not in morse_to_char_dict and user_morse not in "-. ":
            return False

    return True
    # ==================================



def get_cleaned_english_sentence(raw_english_sentence: str):
    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        >>> import morsecode as mc
        >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정

    return raw_english_sentence.replace("?","").replace("!","").replace(".","").replace(",","").strip()
    # ==================================


def decoding_character(morse_character):
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_character("-")
        'T'
        >>> mc.decoding_character(".")
        'E'
        >>> mc.decoding_character(".-")
        'A'
        >>> mc.decoding_character("...")
        'S'
        >>> mc.decoding_character("....")
        'H'
        >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    char_to_morse_dict = get_morse_code_dict()
    morse_to_char_dict = dict()
    for c, m in char_to_morse_dict.items():
        morse_to_char_dict[m] = c

    return morse_to_char_dict[morse_character]
    # ==================================


def encoding_character(english_character):
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_character("G")
        '--.'
        >>> mc.encoding_character("A")
        '.-'
        >>> mc.encoding_character("C")
        '-.-.'
        >>> mc.encoding_character("H")
        '....'
        >>> mc.encoding_character("O")
        '---'
        >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()

    return morse_code_dict[english_character.upper()]
    # ==================================


def decoding_sentence(morse_sentence: str):
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_sentence_l = morse_sentence.split(" ")
    char_to_morse_dict = get_morse_code_dict()
    result = ''
    for e in morse_sentence_l:
        if e == '' and result[-1] != ' ':
            result += ' '
        elif e in char_to_morse_dict.values():
            result += decoding_character(e)
    return result
    # ==================================


def encoding_sentence(english_sentence):
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    clean_english_sentence = get_cleaned_english_sentence(english_sentence)
    result = ""
    for c in clean_english_sentence:
        if c == " " and result[-2:] != '  ':
            result += " "
        elif c.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result += encoding_character(c)
            result += ' '

    return result
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    run = True
    while run:
        user_input = input("Input your message(H - Help, 0 - Exit): ")
        if user_input == "0":
            run = False
        elif is_help_command(user_input):
            print(get_help_message())
        elif is_validated_english_sentence(user_input):
            # 영어에서 모스로 변환시작
            clean_eng_input = get_cleaned_english_sentence(user_input)
            encoding_morse = encoding_sentence(clean_eng_input)
            print(encoding_morse)
        elif is_validated_morse_code(user_input):
            # 모스에서 영어로 변환 시작
            decoding_eng = decoding_sentence(user_input)
            print(decoding_eng)
        else:
            print("Wrong Input")


    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
