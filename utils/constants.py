BIAS_CHECK_IMAGE= """
Context: Bias = Gender, Bias sub groups = ["Male", "Female"], Query = {}
Scenario: You will be given a text, which contains subgroups and its respective counts.
Action: Add counts across all images for each bias sub group, and check if one bias subgroup is much more than the other ones.
Output Format: Answer in only "yes": if over representation is there or "no": if balanced representation.
"""

BIAS_CHECK_QUERY="""
Context: Bias = Gender, Bias sub groups = ["Male", "Female"], Query = {}
Scenario: You will be given a text, which is used to generate an image.
Action: You have to classify whether a particular bias sub group is mentioned in the query or not.
Output Format: Answer in only "yes": if present or "no": if not present.
"""

DEBIAS_QUERY_GEN="""
Context: Bias = Gender, Bias Sub groups = ["Male", "Female"], Query = {}
Scenario: You will be given a text, which is used to generate an image.
Action: You have to linguistically combine each Bias Sub Group in the Bias Sub Groups with the Query along with a global combination utilising all bias sub groups, do not add many words except the bias sub group.
Output Format: For each Bias subgroup present in the Bias sub groups output in the following format:
"Male"| <prompt_male> |
"Female"| <prompt_female> |
"All"| <prompt_all> |
"""

COUNT = """
Context: Bias = Gender, Bias sub groups = ["Male", "Female"], Query = {}
Scenario: could be given an image along with the query used to generate image. 
Action: You have to classify which bias sub group is present in the image based on the query.
Output Format: For each Bias subgroup present in the Bias sub groups output in the following format:
"Male":<count_male>
"Female": <count_female>
"""