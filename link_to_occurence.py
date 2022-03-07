import json
import glob
import argparse

from totoify_grafeas.totoifylib import GrafeasInTotoOccurrence
from in_toto.models.metadata import Metablock
from in_toto.models.link import Link


def link_to_occurence(path_to_link_meta, project_id, note_id):
    with open(path_to_link_meta, 'r') as f:
        link_dict = json.load(f)

    link = Link.read(link_dict["signed"])
    sig = link_dict["signatures"]
    metablock = Metablock(signed=link,signatures=sig)

    occurence = GrafeasInTotoOccurrence.from_link(metablock,f"projects/{project_id}/notes/{note_id}", path_to_link_meta)
    print(occurence.to_json())
    return occurence

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert in-toto link to Grafeas Occurance")
    parser.add_argument("path", help="path to link file")
    parser.add_argument("project_id", help="Grafeas project id")
    parser.add_argument("note_id", help="Grafeas note id")

    try:
        args = parser.parse_args()
        file_path = args.path

        link_files = glob.glob(file_path)
        if len(link_files) != 1:
            raise Exception(f"multiple link files: {link_files}")
        
        project_id = args.project_id
        note_id = args.note_id

        link_to_occurence(file_path, project_id, note_id)

    except Exception as e:
        print(f"Conversion failed {e}")
