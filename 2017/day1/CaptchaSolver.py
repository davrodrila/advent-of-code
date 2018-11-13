class CaptchaSolver():

    def solveCaptcha(self, input):
        digitsToSum = 0
        for index in range(len(input)):
            try:
                if input[index] == input[index+1]:
                    digitsToSum += int(input[index])
            except IndexError:
                if (input[index] == input[0]):
                    digitsToSum += int(input[index])
        return digitsToSum
