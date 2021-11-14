
class Solution(object):

    def switcher(self, letter):
            # switcher:
        switcher = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        return switcher.get(letter,"Invalid input 2")


    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        example: VI
        example 2: IV
        """
        current_number = 0
        previous_number = 0
        progress_number = 0
        final_number = 0
        current_letters = ""
        i = 0
        
        for letter in s:
            i += 1
            print("STEP: ", i)
            current_number = self.switcher(letter)
            
            print("CURRENT NUMBER IS ", current_number)
            print("PREVIOUS NUMBER IS ", previous_number)
            current_letters = current_letters + letter
    
            if (current_number > previous_number):
                print(" current is bigger letter: ", letter)
                print(" current progress roman letters: ", current_letters)
                print("progress number = current number : ", current_number, 
                " - previous number: ", previous_number, " = ", current_number - previous_number)

                progress_number = current_number - previous_number 
                final_number = final_number + progress_number - previous_number
                progress_number = 0

                print("FINAL number after extraction ", final_number)

            elif current_number <= previous_number:
                print(" current is bigger letter: ", letter)
                print(" current progress roman letters: ", current_letters)
                
                progress_number = progress_number + current_number + previous_number          
                final_number = final_number + progress_number - previous_number
                progress_number = 0

                print("FINAL number ", final_number)

            previous_number = current_number
            
        print(s)
        return final_number

            
#s = "CDVIII"
s = "MCMXCIV" #1994
#s = "III"
#s = "IV"
solution = Solution()
print(solution.romanToInt(s))



        