import json
import glob
import argparse

from totoify_grafeas.totoifylib import GrafeasInTotoOccurrence
from in_toto.models.metadata import Metablock
from in_toto.models.link import Link


def occurence_to_link(path, step_name):
    g = GrafeasInTotoOccurrence.load(path)
    link = g.to_link(step_name)
    print(link)
    return link


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Grafeas Occurance to in-toto link")
    parser.add_argument("path", help="path to Occurence file")
    parser.add_argument("step_name", help="in-toto step name")

    try:
        args = parser.parse_args()
        path = args.path
        step_name = args.step_name

        occurence_to_link(path, step_name)

    except Exception as e:
        print(f"Conversion failed {e}")
