class Solution:
    def isPalindrome(self, s: str) -> bool:
        left:int = 0
        right:int = len(s) - 1

        while left < right:

            # Ignora caracteres não alfanuméricos da esquerda
            while left < right and s[left].isalnum() is False:
                left += 1

            # Ignora caracteres não alfanuméricos da direita
            while left < right and s[right].isalnum() is False:
                right -= 1

            # Compara ignorando maiúsculas/minúsculas
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":

    texto = "# ! R A D A R & #"

    solution = Solution()
    resultado = solution.isPalindrome(texto)
    print(f'"{texto}" é palindrome? {resultado}')
