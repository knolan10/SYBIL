import argparse

def main_parser():
    parser = argparse.ArgumentParser(description="Simulate Fermi GBM triggers")
    parser.add_argument(
        "--LIGO_sim_dir", 
        type=str, 
        help="Directory of Simulated LIGO data to base GBM skymaps off of"
    )
    parser.add_argument(
        "--save_dir", 
        type=str, 
        help="Directory to save GBM skymaps"
    )
    # parser.add_argument(
    #     "prob_obs",
    #     type=float,
    #     default=0.1666666667,
    #     help="Probability of GBM detection",
    # )
    return parser

def main_parser_args():
    args = main_parser().parse_args()
    return args
