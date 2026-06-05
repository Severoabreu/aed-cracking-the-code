from time import sleep

import big_o

from challenges.group_anagrams import (
    group_anagrams,
)

from tests.complexities import (
    NOTATIONS,
    ComplexityInferenceData,
    infer_complexity,
    measure_execution_times,
)

from tests.generators import (
    generate_group_anagrams,
)


def test_evaluate_time_group_anagrams():

    highest_acceptable_complexity = (
        big_o.complexities.Linearithmic
    )

    for _ in range(3):

        data = ComplexityInferenceData(
            analyzed_function=group_anagrams,
            generation_function=generate_group_anagrams,
            order_of_magnitude=5,
            initial_order=3,
            base_of_magnitude=3,
            execution_quantity=20,
            times_to_repeat=3,
        )

        results = measure_execution_times(data)

        observed_complexity = infer_complexity(
            results.registered_sizes,
            results.registered_times,
        )

        if (
            observed_complexity
            <= highest_acceptable_complexity
        ):
            break

        sleep(3)

    else:

        assert False, (
            "Seu algoritmo parece ser "
            f"{NOTATIONS[observed_complexity.__class__]}"
            ", mas deveria ser no máximo "
            f"{NOTATIONS[highest_acceptable_complexity]}"
        )
