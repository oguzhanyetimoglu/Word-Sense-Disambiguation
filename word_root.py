import jpype
import os
import re

jar = os.getcwd()+'/zemberek-tum-2.0.jar'
args = '-Djava.class.path=%s' % jar
jvm_path = jpype.getDefaultJVMPath()
# start JVM
jpype.startJVM(jvm_path, args)
# Prepare the necessary class to analyze according to Turkey Turkish
Tr = jpype.JClass('net.zemberek.tr.yapi.TurkiyeTurkcesi')
# Create object tr
tr = Tr()
# Download zemberek class
Zemberek = jpype.JClass('net.zemberek.erisim.Zemberek')
# Create zemberek object
zemberek = Zemberek(tr)

def get_roots(words):
    roots = []
    for word in words:
        if word.strip()>'':
            response = zemberek.kelimeCozumle(word)
            if response:
                #print('{}'.format(response[0]))
                r = re.findall(r'Kok: (.*?) tip:',str(response[0]))[0]
                flag = re.findall(r'tip:(.*?)}',str(response[0]))[0]
                if flag == 'FIIL':
                    last_vowel = [a for a in r if a in 'aeıioöuü'][-1]
                    if last_vowel in 'aıou':
                        r += 'mak'
                    if last_vowel in 'eiöü':
                        r += 'mek'
                roots.append(r)
            else:
                print('Word <{}> failed. '.format(word))
    return roots

words = ['merhabalaştık','dalgalarının','habercisi','tırmalamışsa', 'öldürdü', 'oldurdu', 'aradı']
print(get_roots(words))

#close JVM 
jpype.shutdownJVM()
