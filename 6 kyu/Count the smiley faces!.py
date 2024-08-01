#Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

#Rules for a smiling face:

#Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
#A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
#Every smiling face must have a smiling mouth that should be marked with either ) or D
#No additional characters are allowed except for those mentioned.

#Valid smiley face examples: :) :D ;-D :~)
#Invalid smiley faces: ;( :> :} :]

#Example
#countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
#countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
#countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
#Note
#In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

def count_smileys(arr):
    s = ":;-~)D"

    num = 0
    for p in arr:
        smile=p
        if smile[0] in s[0:2]:
            if smile[1] in s[2:4]:
                if smile[2] in s[4::]:
                    num+=1
            elif smile[1] in s[4::]:
                num+=1
        else:
            num=0
    return num