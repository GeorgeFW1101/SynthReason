# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 1.6
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

def read_file_lines(filename, encoding='ISO-8859-1'):
    with open(filename, encoding=encoding) as file:
        return file.read().splitlines()

def generate_output_filename():
    return "Compendium#" + str(random.randint(0, 10000000)) + ".txt"

def shuffle_and_get_random_item(items):
    random.shuffle(items)
    return items[0]

def process_user_input():
    user_input = input("USER: ").lower()
    return re.sub('\W+', ' ', user_input)

def main():
    token = " to "
    size = 100
    files = read_file_lines("fileList.conf", encoding='ISO-8859-1')
    print("SynthReason - Synthetic Dawn")
    questions = read_file_lines("questions.conf", encoding='ISO-8859-1')
    filename = generate_output_filename()
    
    while True:
        user = process_user_input()
        random.shuffle(files)
        
        for file in files:
            with open(file, encoding='UTF-8') as f:
                text = f.read()
            
            output = generate_output(generate_output(generate_output(user, text, token, size)[:50], text, token, size)[:50], text,token , size)
            
            print("\nusing:", file.strip(), "answering:", user, "\nAI:", output, "\n\n")
            
            with open(filename, "a", encoding="utf8") as f:
                f.write("\nusing: " + file.strip() + " answering: " + user + "\n" + output + "\n")
                
            break  # Remove this line if you want to process all files

def generate_output(user, text, token, size):
    output = []
    words = user.split()
    sentences = text.split(token)
    shuffle_and_get_random_item(sentences)
    
    for i in range(size):
        output.append(' '.join(sentences[i].split()[0:4]) + " ")
    
    for i in range(0, len(sentences) - 3, 3):
        for item in words:
            intersection = set.difference(set(set.intersection(set(sentences[i - 1].split(item)),
                                             set(sentences[i].split(item)),
                                             set(' '.join(output).split()))),
                                             set(sentences[i].split(item)),
                                             set(' '.join(output).split()))
            for word in intersection:
                index_before = ' '.join(output).rfind(item)
                index_after = sentences[i + 1].find(item)
                dot = ' '.join(output).index(word)
                comma = sentences[i].find(",")
                
                if index_before > comma and index_after < dot:
                    if index_before == index_after + 1:
                        output.append(' '.join(sentences[i + 1].split(item)[0].split()[dot:dot + 4]) + " ")
    
    return ''.join(output)

if __name__ == "__main__":
    main()

