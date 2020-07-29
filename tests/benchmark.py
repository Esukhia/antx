# coding=utf-8

import pytest
from pathlib import Path
from horology import timed

from antx import transfer

data_dir = Path("C:/Users/trinley/github/annotation_transfer/tests/test1")

def get_source():
    source = (data_dir / "in" / "source_pos.txt").read_text(encoding="utf-8")
    return source

def get_pattern():
    pattern = (data_dir / "in" / "pattern.txt").read_text(encoding="utf-8")
    return [['pos','(/.+? )']]

def get_target():
    target = (data_dir / "in" / "target_plain.txt").read_text(encoding="utf-8")
    return target

@timed(unit="min")
def test_ann_transfer_non_optimized():
    transfer(
        get_source(), get_pattern(), get_target(), "txt", optimized=False
    )

@timed(unit="min")
def test_ann_transfer_optimized():
    transfer(
        get_source(), get_pattern(), get_target(), "txt"
    )

test_ann_transfer_non_optimized()
test_ann_transfer_optimized()
