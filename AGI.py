# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 2.1
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
token = " to "
size = 25
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.read().splitlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
    questions = f.read().splitlines()
filename = "Compendium#" + str(random.randint(0, 10000000)) + ".txt"
random.shuffle(questions)
for question in questions:
    user = re.sub('\W+', ' ', question.lower())
    random.shuffle(files)
    for file in files:
        with open(file, encoding='UTF-8') as f:
            text = f.read()
        output = []
        words = user.split()
        sentences = text.split(token)
        random.shuffle(sentences)
        # Define sine and cosine wave parameters
        sine_frequency = 1.2  # Adjust as needed
        cosine_frequency = 0.8  # Adjust as needed
        amplitude = 0.5  # Adjust as needed
        phase = 1.1  # Adjust as needed
        
        # Generate sine and cosine wave values
        sine_values = [amplitude * math.cos(2 * math.pi * sine_frequency * i + phase) for i in range(len(sentences))]
        cosine_values = [amplitude * math.degrees(2 * math.pi * cosine_frequency * i + phase) for i in range(len(sentences))]
        
        # Combine sine and cosine waves element-wise
        combined_wave = [s + c for s, c in zip(sine_values, cosine_values)]
        
        # Create a list of sentences along with their combined wave values
        sentences_with_wave = list(zip(sentences, combined_wave))
        
        # Sort sentences based on the combined wave values in descending order
        sentences_with_wave.sort(key=lambda x: x[1])
        
        # Select the first 2 words of each sentence
        selected_sentences = [' '.join(sentence.split()[:int(round(wave_val * 10))]) for sentence, wave_val in sentences_with_wave][:size]

        output_with_wave = ' '.join(selected_sentences)
        
        print("\nusing:", file.strip(), "answering:", user, "\nAI:", output_with_wave, "\n\n")
        
        # Write to the output file
        with open(filename, "a", encoding="utf8") as f:
            f.write("\nusing: " + file.strip() + " answering: " + user + "\n" + output_with_wave + "\n")
        
        break
