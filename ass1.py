import random

words = ["BAAHUBALI THE BEGINNING",
    "BAAHUBALI 2 THE CONCLUSION",
    "RRR",
    "PUSHPA THE RISE",
    "PUSHPA 2 THE RULE",
    "ARJUN REDDY",
    "JERSEY",
    "MAGADHEERA",
    "SALAAR",
    "KALKI 2898 AD",
    "DEVARA",
    "POKIRI",
    "BUSINESSMAN",
    "JANATHA GARAGE",
    "HANU MAN",
    "VIKRAM",
    "LEO",
    "JAILER",
    "ENTHIRAN",
    "TWO POINT ZERO",
    "KAITHI",
    "MASTER",
    "THUPPAKKI",
    "GHILLI",
    "MERSAL",
    "PONNIYIN SELVAN",
    "ASURAN",
    "JAI BHIM",
    "SOORARAI POTTRU",
    "VADA CHENNAI",
    "NINETY SIX",
    "ANNIYAN",
    "SIVAJI",
    "MANKATHA",
    "THANI ORUVAN",
    "VIKRAM VEDHA",
    "MINNALE",
    "INDIAN",
    "AYAN",
    "KARNAN",
    "DRISHYAM",
    "MANJUMMEL BOYS",
    "TWO THOUSAND EIGHTEEN",
    "PREMAM",
    "LUCIFER",
    "AAVESHAM",
    "BANGALORE DAYS",
    "KUMBALANGI NIGHTS",
    "AYYAPPANUM KOSHIYUM",
    "PULIMURUGAN",
    "MALAIKOTTAI VAALIBAN",
    "BHEESHMA PARVAM",
    "KURUP",
    "MINNAL MURALI",
    "DRISHYAM TWO",
    "UYARE",
    "CHARLIE",
    "USTAD HOTEL",
    "PREMALU",
    "DRIVING LICENCE",
    "NERU",
    "THALLUMAALA",
    "TAKE OFF",
    "MAHESHINTE PRATHIKAARAM",
    "JOSEPH",
    "AADUJEEVITHAM",
    "BRAMAYUGAM",
    "RORSHACH",
    "KISHKINDHA KAANDAM",
    "VARSHANGALKKU SHESHAM",
    "AATTAM",
    "NAYATTU",
    "ANJAAM PATHIRAA",
    "TRAFFIC",
    "CLASSMATES",
    "THANMATRA",
    "AADU",
    "KGF CHAPTER ONE",
    "KGF CHAPTER TWO",
    "KANTARA",
    "777 CHARLIE",]
word = random.choice(words)
guessed = ""
lives = 6

while lives > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    print(display, "| Lives:", lives)

    if display == word:
        print("You won!")
        break

    guess = input("Guess a letter: ")

    if guess in word:
        guessed += guess
    else:
        lives -= 1

if lives == 0:
    print("You lost! Word was:", word)















