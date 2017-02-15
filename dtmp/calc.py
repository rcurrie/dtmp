#!/usr/bin/env python2
import sys
import time
import logging
import argparse


def main():
    """
    Tumor Map Calc Agent
    """
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("-i", "--interval", type=int, default=0,
                        help="Minutes between calc, default calc once and exits")
    args = parser.parse_args()

    while True:
        start = time.time()
        logging.info("Starting calc at {}".format(time.asctime(time.localtime(start))))

        try:
            logging.info("Do something here")

            end = time.time()
            logging.info("Finished calc at {} taking {} seconds".format(
                time.asctime(time.localtime(end)), end - start))
        except Exception as e:
            logging.error("Problems calc: {}".format(e))

        if args.interval:
            logging.info("Sleeping for {} minutes...".format(args.interval))
            time.sleep(args.interval * 60)
        else:
            break


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    main()
