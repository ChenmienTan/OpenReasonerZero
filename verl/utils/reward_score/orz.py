from math_verify import parse, verify

def compute_score(
    data_source,
    solution_str,
    ground_truth,
    extra_info
):
    return verify(parse(ground_truth), parse(solution_str))