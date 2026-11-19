import json
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def polynomial(value):
    return value**4 - value**3 - value**2 - value + 1


def sequence(length):
    terms = [0, 0, 0, 1]
    for index in range(4, length):
        radicand = sum(value**2 for value in terms[-3:]) - terms[-4] ** 2
        require(radicand >= 0, f"nonnegative radicand at index {index + 1}")
        floor_root = isqrt(radicand)
        rounded = floor_root + (radicand > floor_root**2 + floor_root)
        require(
            (2 * rounded - 1) ** 2 < 4 * radicand < (2 * rounded + 1) ** 2,
            f"strict nearest-integer interval at index {index + 1}",
        )
        require(rounded >= terms[-1], f"monotonicity at index {index + 1}")
        require(rounded <= sum(terms[-2:]), f"Fibonacci bound at index {index + 1}")
        require(
            abs(rounded**2 - radicand) <= 2 * terms[-1],
            f"square-error bound at index {index + 1}",
        )
        terms.append(rounded)
    return terms


def norm_sequence(initial, length):
    terms = list(initial)
    width = len(initial)
    while len(terms) < length:
        radicand = sum(value**2 for value in terms[-width:])
        floor_root = isqrt(radicand)
        rounded = floor_root + (radicand > floor_root**2 + floor_root)
        require(rounded >= terms[-1], "positive-norm monotonicity")
        require(abs(rounded**2 - radicand) <= 2 * terms[-1], "positive-norm square error")
        require((2 * rounded - 1)**2 < 4 * radicand < (2 * rounded + 1)**2, "positive-norm rounding interval")
        terms.append(rounded)
    return terms


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return result


def sibling_checks():
    two = norm_sequence([1, 2], 512)
    three = norm_sequence([0, 0, 1], 512)
    expected_two = [1,2,2,3,4,5,6,8,10,13,16,21,26,33,42,53,68,86,110,140,178,226,288,366,466,593,754,959,1220,1552,1974,2511,3194,4063,5168,6574,8362,10637,13530,17211,21892,27847,35422,45057,57314,72904,92736,117962,150050]
    expected_three = [0,0,1,1,1,2,2,3,4,5,7,9,12,17,23,31,42,57,77,105,142,193,262,355,482,653,886,1202,1630,2211,2998,4066,5514,7478,10142,13754,18654,25298,34309,46530,63104,85582,116067,157410,213480,289522,392651,532514,722197]
    require(two[:len(expected_two)] == expected_two, "A063827 displayed source terms")
    require(three[:len(expected_three)] == expected_three, "A400644 displayed source terms")
    seed_data = []
    for width, terms, index, expected, lower, growth in [(2, two, 11, 21, Fraction(8,5), Fraction(3,2)), (3, three, 17, 57, Fraction(9,5), Fraction(7,4))]:
        seed = terms[index]
        require(seed == expected, "positive-norm seed")
        require(lower**width - sum(lower**power for power in range(width)) < 0, "positive-root lower bound")
        require((growth - Fraction(1,2*seed))**2 > width, "eventual positive-norm growth bound")
        margin = seed**2 - 2 * seed / (lower - growth)
        require(margin > 0, "positive-norm entire-tail margin")
        for offset, value in enumerate(terms[index:]):
            require(value <= seed * growth**offset, "positive-norm finite growth")
        seed_data.append({"width":width,"zero_based_index":index,"value":seed,"margin_lower_bound":str(margin)})
    quartic = [1, -1, -1, -1, 1]
    require(multiply([1,0,0,1], quartic) == [1,-1,-1,0,0,-1,-1,1], "H denominator identity")
    require(multiply([1,-1,1], quartic) == [1,-2,1,-1,1,-2,1], "rounded-linear generating function identity")
    require(multiply([-2,0,-2], quartic) == [-2,2,0,4,0,2,-2], "Hohn sum identity")
    auxiliary = []
    def at(index):
        return auxiliary[index] if index >= 0 else 0
    for index in range(512):
        auxiliary.append(1 if index == 0 else at(index-1)+at(index-2)+at(index-5)+at(index-6)-at(index-7))
        require(auxiliary[-1] >= (auxiliary[-2] if index else 0), "auxiliary monotonicity")
    increasing = [sum(coefficient * at(index-shift) for shift, coefficient in [(0,1),(1,2),(2,1),(7,1),(8,2),(9,1)]) for index in range(512)]
    coefficients = [(-1)**index * ((9*(index+1))//7 + (2*((9*(index+1)) % 7) > 7)) for index in range(512)]
    for index in range(512):
        require(sum(coefficients[shift] * increasing[index-shift] for shift in range(index+1)) == (1 if index == 0 else 0), "A289916 NAME inverse series")
        if index:
            require(increasing[index] > increasing[index-1], "A289916 strict increase")
    expected_increasing = [1,3,5,8,13,22,39,69,120,206,353,607,1046,1803,3106,5348,9208,15856,27306,47025,80982,139457,240155,413566,712196,1226463,2112073,3637166,6263503,10786276,18574872,31987488,55085136,94861220,163358969,281317834,484452887]
    require(increasing[:len(expected_increasing)] == expected_increasing, "A289916 displayed source terms")
    companion = {0:0,1:0,2:0,3:1}
    for index in range(4,515):
        companion[index] = companion[index-1]+companion[index-2]+companion[index-3]-companion[index-4]
    for index in range(-1,-513,-1):
        companion[index] = companion[index+3]+companion[index+2]+companion[index+1]-companion[index+4]
    for index in range(-512,513):
        require(companion[index] == -companion[2-index], "Somos integer-index reversal")
    return {"A063827":{"terms_checked":512,"source_terms_matched":len(expected_two)},"A400644":{"terms_checked":512,"source_terms_matched":len(expected_three)},"A289916":{"terms_checked":512,"source_terms_matched":len(expected_increasing),"strictly_increasing":True},"positive_norm_seeds":seed_data,"A116732_reversal_range":[-512,512],"algebraic_identities":"exact coefficient equalities"}


def main():
    terms = sequence(512)
    expected = [
        0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28,
        37, 48, 63, 83, 109, 143, 188, 247, 324, 425, 558, 732,
        961, 1261, 1655, 2172, 2850, 3740, 4908, 6441, 8452,
        11092, 14556, 19101, 25066, 32894, 43166, 56646, 74336,
        97549, 128012, 167988, 220447, 289289,
    ]
    require(terms[: len(expected)] == expected, "all 51 displayed OEIS terms")
    seed = terms[25]
    require(seed == 324, "a(26) = 324")
    lower = Fraction(17, 10)
    upper = Fraction(7, 4)
    growth = Fraction(5, 3)
    require(polynomial(lower) < 0 < polynomial(upper), "quartic endpoint signs")
    require(lower - growth == Fraction(1, 30), "geometric tail denominator")
    require(growth**2 > growth + 1, "growth induction coefficient")
    require(upper - 1 < upper / 2, "A < 1/2")
    require(0 < lower**2 - lower - 1, "B > 0")
    require(1 - 1 / upper - 1 / upper**2 < Fraction(1, 5), "B < 1/5")
    require(1 / lower**4 < Fraction(1, 8), "C < 1/8")
    require(Fraction(1, 2) + Fraction(2, 5) == Fraction(9, 10), "contraction coordinate 1")
    require(Fraction(1, 5) + Fraction(3, 20) <= Fraction(9, 10) * Fraction(2, 5), "contraction coordinate 2")
    require(Fraction(1, 8) <= Fraction(9, 10) * Fraction(3, 20), "contraction coordinate 3")
    positivity_margin = Fraction(7, 17) * seed**2 - 120 * seed
    require(positivity_margin == Fraction(73872, 17) > 0, "positive infinite-tail margin")
    require(Fraction(7,17) * 292**2 - 120 * 292 == Fraction(1168,17) > 0, "large-data signed entire-tail margin")
    for index in range(25, len(terms)):
        require(terms[index] <= 2 * seed * growth ** (index - 25), "finite growth bound")
    root_lower = Fraction(1722083805739, 10**12)
    root_upper = Fraction(1722083805740, 10**12)
    require(polynomial(root_lower) < 0 < polynomial(root_upper), "refined quartic interval signs")
    require(lower < root_lower < root_upper < upper, "refined quartic interval location")
    sample = [Fraction(7, 5), Fraction(2), Fraction(13, 7)]
    for parameter in sample:
        values = [3, 7, 11, 19, 31]
        error = values[4] - values[3] - values[2] - values[1] + values[0]
        def projection(offset):
            return (
                values[offset + 3] + (parameter - 1) * values[offset + 2]
                + (parameter**2 - parameter - 1) * values[offset + 1]
                - values[offset] / parameter
            )
        require(
            projection(1) - parameter * projection(0) - error
            == -values[1] * polynomial(parameter) / parameter,
            "projection polynomial identity control",
        )
    require(isqrt(2) == 1 and 2 <= 1**2 + 1, "constant-one stationary control")
    with localcontext() as context:
        context.prec = 65
        radical = (1 + Decimal(13).sqrt() + (2 * Decimal(13).sqrt() - 2).sqrt()) / 4
        limiting_ratio = radical.sqrt()
        observed_ratio = Decimal(terms[-1]) / Decimal(terms[-2])
        result = {
            "status": "ALL_CHECKS_OK",
            "terms_checked": len(terms),
            "oeis_terms_matched": len(expected),
            "seed": {"index": 26, "value": seed},
            "positivity_margin_lower_bound": str(positivity_margin),
            "signed_large_data_threshold": {"last_initial_term":292,"margin_lower_bound":"1168/17"},
            "squared_limit_interval": [str(root_lower), str(root_upper)],
            "limiting_ratio_decimal": str(limiting_ratio),
            "observed_ratio_a512_over_a511": str(observed_ratio),
            "siblings": sibling_checks(),
            "coverage": "Exact finite rounding, growth, projection, source-term and algebraic checks; infinite asymptotics, general initial data and monotonicity are proved in note.tex.",
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
