# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 2.0
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
while True:
    user = re.sub('\W+', ' ', input("USER: ").lower())
    random.shuffle(files)
    for file in files:
        with open(file, encoding='UTF-8') as f:
            text = f.read()
        output = []
        words = user.split()
        sentences = text.split(token)
        sentences = sorted(sentences, key=lambda x: len(x)*(len(set(x))))        
        for word in words:
            for i in range(0, len(sentences) - 3):            
                if sentences[i].lower().find(word) > -1:
                    
                   output.append(' '.join(sentences[i].split()[0:4]))
                   middle_index = len(output) // 2
        output = sorted(output, key=lambda x: len(set(output)) * (len(set(sentences[i].split()))))

# Split the sorted list into two halves
        beginning_half = output[:middle_index]
        end_half = output[middle_index:]
        interleaved_output = []
        for i in range(middle_index):
            interleaved_output.append(beginning_half[i])
            interleaved_output.append(end_half[i])
            interleaved_output.extend(end_half[middle_index:])
            output = interleaved_output

        if len(' '.join(output).split()) > size:
            output = ' '.join(output)        
            print("\nusing:", file.strip(), "answering:", user, "\nAI:", output, "\n\n")
            with open(filename, "a", encoding="utf8") as f:
                f.write("\nusing: " + file.strip() + " answering: " + user + "\n" + output + "\n")
            break