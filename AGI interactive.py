# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 1.8
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
token = "."
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
        for word in words:
            for i in range(0, len(sentences) - 3, 6):            
                if sentences[i].lower().find(word) > -1 and  len(''.join(''.join(sentences[i].split(word)[0]).split()))>2 and len(sentences[i].split(word))>2 and len(''.join(sentences[i].split(word)[1]).split())>2:
                   output.append(' '.join(''.join(sentences[i].split(word)[0]).split()[-4:-1]))
                   output.append(' '.join(''.join(sentences[i].split(word)[1]).split()[-4:-1]))
                   output.append(' '.join(''.join(sentences[i].split(word)[2]).split()[-4:-1]))
        if len(' '.join(output).split()) > size:
            output = ' '.join(output)        
            print("\nusing:", file.strip(), "answering:", user, "\nAI:", output, "\n\n")
            with open(filename, "a", encoding="utf8") as f:
                f.write("\nusing: " + file.strip() + " answering: " + user + "\n" + output + "\n")
            break