from pydantic import BaseModel
from typing import List

class EuclidStep(BaseModel):
    a: int
    b: int
    quotient: int
    remainder: int
    explanation: str

class EuclidResponse(BaseModel):
    steps: List[EuclidStep]
    gcd: int
    iterations: int
    input_numbers: List[int]

class EuclidAlgorithm:
    @staticmethod
    def calculate_gcd(a: int, b: int) -> EuclidResponse:
        original_a, original_b = a, b
        
        # Работаем с положительными числами для корректности объяснений
        a_calc, b_calc = abs(a), abs(b)
        
        if a_calc < b_calc:
            a_calc, b_calc = b_calc, a_calc
        
        steps = []
        iterations = 0
        
        # Если одно из чисел 0, НОД — это другое число
        if b_calc == 0:
            return EuclidResponse(
                steps=[],
                gcd=a_calc,
                iterations=0,
                input_numbers=[original_a, original_b]
            )

        while b_calc != 0:
            iterations += 1
            quotient = a_calc // b_calc
            remainder = a_calc % b_calc
            
            if remainder == 0:
                explanation = f"Делим {a_calc} на {b_calc}. Получаем {quotient} и остаток {remainder}. Так как остаток 0, {b_calc} является НОД."
            else:
                explanation = f"Делим {a_calc} на {b_calc}. Получаем {quotient} и остаток {remainder}. Теперь делим {b_calc} на {remainder}."
            
            steps.append(EuclidStep(
                a=a_calc,
                b=b_calc,
                quotient=quotient,
                remainder=remainder,
                explanation=explanation
            ))
            
            a_calc, b_calc = b_calc, remainder
        
        return EuclidResponse(
            steps=steps,
            gcd=a_calc,
            iterations=iterations,
            input_numbers=[original_a, original_b]
        )