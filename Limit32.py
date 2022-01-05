import sys
import pysrt

# Limits the text in each line of an srt file to 32 characters in compliance
# with broadcast 608/708
# input: srt file name

def limit32(file):
    f = pysrt.open(file, encoding='iso-8859-1')
    out = open("new" + file, "w")
    count = 1
    oldCount = 1
    for i in f:
        if len(i.text) > 32:
            j = len(i.text) // 2
            while not i.text[j].isspace():
                if j < len(i.text) - 1:
                    j += 1
                else:
                    j = len(i.text) // 2 - 1
                    while not i.text[j].isspace():
                        if j > 0:
                            j -= 1
                        else:
                            j = len(i.text)
                            break
                    break
            one = i.text[0:j]
            two = i.text[j + 1:]
            if len(one) > 32:
                print("Line {} could not be limited to 32 characters.\n"
                                .format(count))
            if len(two) > 32:
                print("Line {} could not be limited to 32 characters.\n"
                                .format(count + 1))
            start1 = i.start
            start2 = i.start
            if oldCount >= len(f):
                end1 = i.end
                end2 = i.end
            else:
                end1 = f[oldCount].start
                end2 = f[oldCount].start
            if not len(one) == 0:
                out.write(
                    "{}\n{} --> {}\n{}\n\n".format(count, start1, end1, one))
                count += 1
            if not len(two) == 0:
                out.write(
                    "{}\n{} --> {}\n{}\n\n".format(count, start2, end2, two))
                count += 1
        else:
            out.write("{}\n{} --> {}\n{}\n\n".format(
                count, i.start, i.end, i.text))
            count += 1
        oldCount += 1
    out.close()


limit32(sys.argv[1])
print("All files generated successfully.\n")
