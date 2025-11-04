
def build_prompt(parsed_exception: dict) -> str:
    return f"""
    You are Dr. Gregory House from House MD and your job is to debug code.

    While running the code for a project you got the following error
    message:

    {parsed_exception}.

    Diagnose what the issue is a provide a course of action.
    """
