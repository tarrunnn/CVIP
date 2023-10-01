import time

def typing_speed_test():
    text = "The quick brown fox jumps over the lazy dog"
    print("Type the following text:")
    print(text)

    input("Press Enter when you're ready to start...")
    start_time = time.time()

    user_input = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_per_minute = len(text.split()) / (elapsed_time / 60)

    print("\nTime taken:", round(elapsed_time, 2), "seconds")
    print("Your typing speed:", round(words_per_minute), "words per minute")

typing_speed_test()
