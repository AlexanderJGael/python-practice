'''
problem statement:
You have so many blocks
each layer will use one less block
you can't use more blocks than you have
if you have 6 blocks, you can only make a pyramid with 3 layers
'''
class Solver:
    def plusOne(self, digits):
            output = []
            carry = 1 # presetting the carry is the same as adding one to the end
            N = len(digits)
            for i in range(N):
                if not carry:
                    break
                carry = 1 if digits[N-i-1] == 9 else 0
                digits[N-i-1] = (digits[N-i-1] + 1) % 10

            return [1] + digits if carry else digits

if __name__ == '__main__':
    solver = Solver()
    print(solver.plusOne([2,3,9,1,9]))
