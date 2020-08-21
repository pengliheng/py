import preprocess
import engine
import ast_example


def main():
    # with open("ast_example.py", "r") as source:
    #     code = source.read()
    code = ast_example.rule['R_INV_1']
    code = preprocess.add_field_declaration(code)
    # print(code)
    code = preprocess.warp_function(code)
    # print(code)
    print(engine.run(code))
    code = preprocess.un_warp_function(code)
    # print(code)
    code = preprocess.remove_field_declaration(code)
    # print(code)


if __name__ == "__main__":
    main()
