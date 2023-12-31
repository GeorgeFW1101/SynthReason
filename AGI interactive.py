# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 3.0
# BSD 2-Clause License
# 
# Copyright (c) 2023, George Wagenknecht
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
import random
import re
import math

token = " and "
size = 25

with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.read().splitlines()

print("SynthReason - Synthetic Dawn")

with open("questions.conf", encoding='ISO-8859-1') as f:
    questions = f.read().splitlines()

while True:
    user = re.sub('\W+', ' ', input("USER: ").lower())
    random.shuffle(files)

    for file in files:
        with open(file, encoding='UTF-8') as f:
            text = f.read()

        sentences = text.split(token)
        sentences = [sentence for sentence in sentences if any(word in sentence for word in user.split())]
        random.shuffle(sentences)

        sine_frequency, cosine_frequency, amplitude, phase = 5.2, 0.5, 0.4, 1.1  # Adjust as needed

        sine_values = [amplitude / math.atan(4 / math.pi / sine_frequency * i + phase) for i in reversed(range(len(sentences)))]
        degrees_values = [amplitude / math.degrees(2 / math.pi / cosine_frequency * i + phase) for i in sine_values]

        combined_wave = [s + c for s, c in zip(sine_values, degrees_values)]

        # Define a custom sorting function based on the wave values
        def custom_sort(item):
            sentence, wave_value = item
    # First, sort by wave_value in descending order
    # If wave values are equal, then sort by sentence length in ascending order
            return (-wave_value, len(sentence))


        sentences_with_wave = sorted(zip(sentences, combined_wave), key=custom_sort, reverse=True)
        selected_sentences = [' '.join(sentence.split()[:3]) for sentence, _ in sentences_with_wave][:size]

        output_with_wave = ' '.join(selected_sentences)

        print("\nusing:", file.strip(), "answering:", user, "\nAI:", output_with_wave, "\n\n")

        filename = "Compendium#" + str(random.randint(0, 10000000)) + ".txt"
        with open(filename, "a", encoding="utf8") as f:
            f.write("\nusing: " + file.strip() + " answering: " + user + "\n" + output_with_wave + "\n")

        break
