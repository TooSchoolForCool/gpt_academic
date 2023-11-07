# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
import importlib
from toolbox import clear_line_break


def customize_functionals(functionals):
    # Set visibility of original core functionals
    functionals["英语学术润色"]["Visible"] = True
    functionals["中文学术润色"]["Visible"] = True
    functionals["查找语法错误"]["Visible"] = False
    functionals["中译英"]["Visible"] = True
    functionals["学术中英互译"]["Visible"] = True
    functionals["英译中"]["Visible"] = True
    functionals["找图片"]["Visible"] = False
    functionals["解释代码"]["Visible"] = False
    functionals["参考文献转Bib"]["Visible"] = False

    # add customize core functionals
    functionals.update({
        "Explain Code": {
            "Prefix":   r"I want you to act as a professional programmer, explain following code for me：" + "\n```\n",
            "Suffix":   "\n```\n",
        },
        "Generate Code": {
            "Prefix":   r"I want you to act as a professional programmer, tell me how to implement following functions：" + "\n\n",
            "Suffix":   r"",
        },
        "[General] Polish": {
            "Prefix":   r"I want you to act as a professional writer, help me streamline following paragraph：" + "\n\n",
            "Suffix":   r"",
        },
        "[General] Write": {
            "Prefix":   r"I want you to act as a professional writer, write me a paragraph in terms of following points：" + "\n\n",
            "Suffix":   r"",
        },
        "[Academic] Write": {
            "Prefix":   r"I want you to act as a professional academic writer. I will provide you a list of key points, " +
                        r"write me a paragraph using formal language and ensuring clarity, coherence, and readability." + "\n\n",
            "Suffix":   r"",
        },
        "[Academic] Review": {
            "Prefix":   r"You are a researcher in Artificial Intelligence, Robotics, and Computer Vision, " +
                        r"write me a summary and a thorough assessment of the strengths and weaknesses of a paper." + 
                        r"The paper abstract is as following: "  + "\n\n",
            "Suffix":   r"",
        }
    })

    return functionals