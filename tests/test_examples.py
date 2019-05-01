EXPECTED = 'Hello Larry my name is Mary'


def test_01():
    from fortytwo.s01_find_action import main
    assert EXPECTED == main()


def test_01():
    from fortytwo.s01_find_action import main
    assert EXPECTED == main()


def test_02():
    from fortytwo.s02_reduce_clutter import main
    assert EXPECTED == main()


def test_03():
    from fortytwo.s03_disable_tabs import main
    assert EXPECTED == main()


def test_04():
    from fortytwo.s04_recent_file import main
    assert EXPECTED == main()


def test_05():
    from fortytwo.s05_recent_tool import main
    assert EXPECTED == main()


def test_06():
    from fortytwo.s06_navigate_symbol import main
    assert EXPECTED == main()


def test_07():
    from fortytwo.s07_navigate_file import main
    assert EXPECTED == main()


def test_08():
    from fortytwo.s08_navigate_cursor import main
    assert EXPECTED == main()


def test_09():
    from fortytwo.s09_activate_navbar import main
    assert EXPECTED == main()


def test_09():
    from fortytwo.s09_activate_navbar import main
    assert EXPECTED == main()


def test_10():
    from fortytwo.s10_navigate_files_navbar import main
    assert EXPECTED == main()


def test_11():
    from fortytwo.s11_open_file_navbar import main
    assert EXPECTED == main()


def test_12():
    from fortytwo.s12_speedsearch_navbar import main
    assert EXPECTED == main()


def test_13():
    from fortytwo.s13_create_file_navbar import main
    assert EXPECTED == main()


def test_14():
    from fortytwo.s14_find_in_path_navbar import main
    assert EXPECTED == main()


def test_15():
    from fortytwo.s15_add_line import main
    assert EXPECTED == main()


def test_16():
    from fortytwo.s16_make_extend_selection import main
    assert EXPECTED == main()


def test_17():
    from fortytwo.s17_move_block import main
    assert EXPECTED == main()


def test_18():
    from fortytwo.s18_reformat_code import main
    assert EXPECTED == main()


def test_19():
    from fortytwo.s19_optimize_imports import main
    assert EXPECTED == main()


def test_20():
    from fortytwo.s20_generate_imports import main
    assert EXPECTED == main()


def test_21():
    from fortytwo.s21_install_and_import import main
    assert 'Mary' in main()


def test_22():
    from fortytwo.s22_adding_fields import main
    assert EXPECTED == main()


def test_23():
    from fortytwo.s23_rename_file import main
    assert EXPECTED == main()


def test_24():
    from fortytwo.s24_rename_symbol import main
    assert EXPECTED == main()


def test_27():
    from fortytwo.s27_run_from_keyboard import main
    assert EXPECTED == main()


def test_28():
    from fortytwo.s28_conditional_breakpoints import main
    assert 'Mary' in main()


def test_29():
    from fortytwo.s29_evaluate_expression import main
    assert 'Mary' in main()


def test_30():
    from fortytwo.s30_split_screen import main
    assert EXPECTED == main()


def test_31():
    from fortytwo.s31_run_single_test import main
    assert EXPECTED == main()


def test_32():
    from fortytwo.s32_autorun_tests import main
    assert EXPECTED == main()


def test_33():
    from fortytwo.s33_spot_coverage_gaps_in_gutter import main
    assert EXPECTED == main()

# def test_3():
#     from fortytwo.s3 import main
#     assert EXPECTED == main()
#
