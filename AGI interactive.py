# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 1.3
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
token = " to "
size = 100
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.read().splitlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
    questions = f.read().splitlines()
filename = "Compendium#" + str(random.randint(0, 10000000)) + ".txt"
random.shuffle(questions)
while(True):
    user = re.sub('\W+', ' ', input("USER: ").lower())
    random.shuffle(files)
    for file in files:
        with open(file, encoding='UTF-8') as f:
            text = f.read()
        output = []
        words = user.split()
        sentences = text.split(token)
        random.shuffle(sentences)
        for i in range(size):
            output.append(' '.join(sentences[i].split()[0:4]) + " ")
        for i in range(0, len(sentences) - 3, 3):
            for word in words:
                for item in set.intersection(set(sentences[i-1].split(word))
                ,set(sentences[i].split(word))
                 ,set(sentences[i+1].split(word))):             
                    index_before = ' '.join(output).rfind(item)
                    index_after = sentences[i+1].find(item)
                    dot = sentences[i].find(".")
                    comma = sentences[i].find(",")
                    if index_before != comma and index_after < dot:
                        if index_before == index_after:
                            output.append(' '.join(sentences[i+1].split(word)[0].split()[comma:comma+4]) + " ")
                            break        
        output = ''.join(output)        
        print("\nusing:", file.strip(), "answering:", user, "\nAI:", output, "\n\n")
        with open(filename, "a", encoding="utf8") as f:
            f.write("\nusing: " + file.strip() + " answering: " + user + "\n" + output + "\n")
        break