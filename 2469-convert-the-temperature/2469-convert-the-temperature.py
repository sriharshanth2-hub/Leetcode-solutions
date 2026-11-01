class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans = []
        kelvin = celsius + 273.15
        far = celsius * 1.80 + 32.00
        ans.append(kelvin)
        ans.append(far)
        return ans